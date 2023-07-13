import hashlib

from anyio import Path
from fastapi import HTTPException, Request, File
from fastapi.responses import JSONResponse
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


def get_host(req: Request) -> str:
    return getattr(req, "headers", {}).get("host") or "http://127.0.0.1:8000"


@app.post('/uploadProfile')
async def uploadProfile(request: Request,file: bytes = File(...)) -> JSONResponse:
    if len(file) > LIMIT_SIZE:
        raise HTTPException(status_code=400, detail="每个文件都不能大于5M")
        # 使用md5作为文件名，以免同一个文件多次写入
    filename = hashlib.md5(file).hexdigest() + ".png"
    if not await (fpath := UPLOAD_ROOT / filename).exists():
        if not await fpath.parent.exists():
            await fpath.parent.mkdir(parents=True)
        await fpath.write_bytes(file)
    host = get_host(request)
    id=request.get("id")
    path='profile'+hashlib.md5(file).hexdigest() + ".jpg"
    profile_path=host + "/" + path
    with Session(engine) as session:
        statement = select(User).where(User.id == id)
        results = session.exec(statement)
        user = results.one()
        user.profile_URL=profile_path
        session.add(user)
        session.commit()
        session.refresh(user)
        response = JSONResponse(content={"message": "用户头像更新成功", "URL": profile_path})
        return response
