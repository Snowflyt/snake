import re

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
    phone_number: str


def validate_phone_number(phone_number):
    pattern = r'^1[3456789]\d{9}$'
    match = re.match(pattern, phone_number)
    if match:
        return True
    else:
        return False


@app.post('/register')
async def register(registration: Registration):
    registration_dict = jsonable_encoder(registration)
    username = registration_dict.get('username', None)
    password = registration_dict.get('password', None)
    phone_number = registration_dict.get('phone_number', None)
    if not username:
        raise HTTPException(status_code=400, detail="您还没有填写用户名")
    elif len(password) < 8 or len(password) > 20:
        raise HTTPException(status_code=400, detail="密码长度必须介于8和20之间")
    elif not phone_number:
        raise HTTPException(status_code=400, detail="您还没有填写电话号码")
    elif len(phone_number) != 11 or validate_phone_number(phone_number):
        raise HTTPException(status_code=400, detail="电话号码格式不对,请检查")
    with Session(engine) as session:
        existed = session.exec(select(User).where(
            User.username == username)).all()
        if existed:
            raise HTTPException(status_code=400, detail="用户名已被注册,请换一个!")
        user = User(username=username, password=password,
                    phone_number=phone_number)
        session.add(user)
        session.commit()
        session.refresh(user)
        response = JSONResponse(content={"message": "Register Successfully"})
        response.set_cookie(key="username", value=username)
        return response
