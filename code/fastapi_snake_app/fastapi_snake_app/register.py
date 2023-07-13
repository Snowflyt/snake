from fastapi import HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi_snake_app.db import engine
from fastapi.encoders import jsonable_encoder
from sqlmodel import Session, select
from fastapi_snake_app.db.user import User

from fastapi_snake_app.main import app


class Registration(BaseModel):
    username: str
    password: str


@app.post('/register')
async def register(registration: Registration):
    registration_dict = jsonable_encoder(registration)
    username = registration_dict.get('username', None)
    password = registration_dict.get('password', None)
    if len(password) < 8 or len(password) > 20:
        raise HTTPException(status_code=400, detail="密码长度必须介于8和20之间")
    with Session(engine) as session:
        existed = session.exec(select(User).where(User.username == username)).all()
        if existed:
            raise HTTPException(status_code=400, detail="用户名已被注册,请换一个!")
        user = User(username=username, password=password)
        session.add(user)
        session.commit()
        session.refresh(user)
        response = JSONResponse(content={"message": "Register Successfully"})
        response.set_cookie(key="username", value=username)
        return response
