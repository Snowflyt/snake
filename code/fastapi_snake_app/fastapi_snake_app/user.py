import base64
import hashlib
import io
from PIL import Image
from anyio import Path
from fastapi import HTTPException, Request, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlmodel import Session, select

from fastapi_snake_app.db import engine
from fastapi_snake_app.db.user import User
from fastapi_snake_app.main import app


@app.get('/users')
async def read_users() -> list[User]:
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        return users


@app.post('/user')
async def create_user(user: User):
    with Session(engine) as session:
        existed = session.exec(select(User).where(User.username == user.username)).all()
        if existed:
            raise HTTPException(status_code=400, detail="用户名已被注册,请换一个!")
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


BASE_DIR = Path(__file__).parent
LIMIT_SIZE = 5 * 1024 * 1024  # 5M
MEDIA_ROOT = BASE_DIR / "media"
UPLOAD_ROOT = MEDIA_ROOT / "uploads"


class UploadRequest(BaseModel):
    id: int
    host: str = "http://101.132.165.23"
    profile_base64:str


def base64_to_image(base64_data):
    try:
        # 解码 Base64 数据
        decoded_data = base64.b64decode(base64_data)

        # 创建 BytesIO 对象
        image_stream = io.BytesIO(decoded_data)

        # 打开图像
        image = Image.open(image_stream)

        return image
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Failed to convert Base64 to image: {str(e)}")


@app.post('/uploadProfile')
async def uploadProfile(upload_request: UploadRequest) -> JSONResponse:
    base64_data=UploadRequest.profile_base64
    image = base64_to_image(base64_data)
    host = upload_request.host
    path = 'profile/' + str(id)+ ".jpg"
    profile_path = host + "/" + path
    print(profile_path)
    image.save(profile_path)
    with Session(engine) as session:
        statement = select(User).where(User.id == upload_request.id)
        results = session.exec(statement)
        user = results.one()
        user.profile_URL = profile_path
        session.add(user)
        session.commit()
        session.refresh(user)
        response = JSONResponse(content={"message": "用户头像更新成功", "URL": profile_path})
        return response
