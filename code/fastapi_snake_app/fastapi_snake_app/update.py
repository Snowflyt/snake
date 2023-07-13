from fastapi import HTTPException, Body
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi_snake_app.db import engine
from sqlmodel import Session, select
from fastapi_snake_app.db.user import User

from fastapi_snake_app.main import app
from fastapi_snake_app.register import validate_phone_number


# 定义更新用户数据的请求模型
class UpdateUserRequest(BaseModel):
    username: str | None
    password: str | None
    phone_number: str | None
    language_excellent: str | None


@app.post('/update', description="用于更新用户个人信息", tags=['用户基本操作'])
async def update(user_id: int, update_user_request: UpdateUserRequest
= Body(..., example={"user_id": "用户id，必填格式要求是整型，如114514",
                     "update_user_request": {"username": "用户名,选填,格式要求是字符串，默认值是None",
                                             "password": "密码,选填，格式要求是字符串，默认值是None",
                                             "phone_number": "电话号码,选填，格式要求是字符串，默认值是None",
                                             "language_excellent": "用户当前擅长的语言，选填，格式要求是字符串，默认值为None"}})):
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        results = session.exec(statement)
        user = results.one()
        if len(update_user_request.password) < 8 or len(update_user_request.password) > 20:
            raise HTTPException(status_code=400, detail="密码长度必须介于8和20之间")
        elif len(update_user_request.phone_number) != 11 or validate_phone_number(update_user_request.phone_number):
            raise HTTPException(status_code=400, detail="电话号码格式不对,请检查")
        existed = session.exec(select(User).where(User.username == update_user_request.username)).all()
        if existed:
            raise HTTPException(status_code=400, detail="用户名已被注册,请换一个!")
        user.username = update_user_request.username if update_user_request.username else user.username
        user.password = update_user_request.password if update_user_request.password else user.password
        user.phone_number = update_user_request.phone_number if update_user_request.phone_number else user.phone_number
        user.language_excellent = update_user_request.language_excellent if update_user_request.language_excellent else user.language_excellent
        session.add(user)
        session.commit()
        session.refresh(user)
        response = JSONResponse(content={"message": "用户数据更新成功", "user": user.username})
        return response
