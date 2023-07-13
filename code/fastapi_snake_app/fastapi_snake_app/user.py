import base64
import hashlib
import io
from PIL import Image
from anyio import Path
from fastapi import HTTPException, Body
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlmodel import Session, select

from fastapi_snake_app.db import engine
from fastapi_snake_app.db.user import User
from fastapi_snake_app.main import app


@app.get('/users', description="从用户表中读取所有用户", tags=['用户基本操作'])
async def read_users() -> list[User]:
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        return users


@app.post('/user', description="用户表中插入新用户行", tags=['用户基本操作'])
async def create_user(user: User = Body(..., example={'id': "用户id,必填，格式要求是整型",
                                                      'username': "用户名,必填,格式要求是字符串",
                                                      'password': "密码,必填，格式要求是字符串",
                                                      'phone_number': "电话号码,必填，格式要求是字符串'",
                                                      'level': "用户等级，选填，格式要求是整型,默认值是1",
                                                      'experience': "用户当前等级经验值，选填，格式要求是整型，默认值是0",
                                                      'common_money': "用户当前蛇币余额，选填，格式要求是整型，默认为0",
                                                      'special_money': "用户当前蛇钻余额，选填，格式要求是整型，默认值为0",
                                                      'total_starts': "用户当前收集到的星星总数，选填，格式要求是整型，默认值为0",
                                                      'rank': "用户当前段位，选填，格式要求是字符串，默认值为最强青铜IV",
                                                      'score': "用户当前段位胜点，选填，格式要求是整型，默认值为0，最大值100，最小值0",
                                                      'language_excellent': "用户当前擅长的语言，选填，格式要求是字符串，默认值为全能",
                                                      'profile_URL': "用户头像在服务器存放的地址，选填，格式要求是字符串，默认值为http://127.0.0.1:"
                                                                     "8000/profiles/default_profile.jpg"})):
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
    profile_base64: str


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
        raise HTTPException(status_code=400, detail=f"Failed to convert Base64 to image: {str(e)}")


@app.post('/uploadProfile', description="用于让用户上传头像并存储在服务器中", tags=['用户基本操作'])
async def uploadProfile(
        upload_request: UploadRequest = Body(..., example={
                                                               "user_id": "用户id，必填格式要求是整型，如114514",
                                                               "host": "域名,选填，格式要求是字符串，默认值为http://101.132.165.23",
                                                               "profile_base64": "图片转换成base64后的字符串，必填，格式要求是字符串",
                                                               })) -> JSONResponse:
    base64_data = upload_request.profile_base64
    image = base64_to_image(base64_data)
    host = upload_request.host
    path = 'profile/' + str(id) + ".jpg"
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
