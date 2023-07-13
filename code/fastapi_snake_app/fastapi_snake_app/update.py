from fastapi import HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlmodel import Session, select

from fastapi_snake_app.db import engine
from fastapi_snake_app.db.user import User
from fastapi_snake_app.main import app
from fastapi_snake_app.register import validate_phone_number


# 定义更新用户数据的请求模型
class UpdateUserRequest(BaseModel):
    username: str | None
    password: str | None
    phone_number: str | None
    language_excellent: str | None


@app.post('/update')
async def update(user_id: int, request: UpdateUserRequest):
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        results = session.exec(statement)
        user = results.one()
        if (request.password is not None and
                (len(request.password) < 8 or len(request.password)) > 20):
            raise HTTPException(status_code=400, detail="密码长度必须介于8和20之间")
        if (request.phone_number is not None and
                (len(request.phone_number) != 11 or validate_phone_number(request.phone_number))):
            raise HTTPException(status_code=400, detail="电话号码格式不对,请检查")
        existed = session.exec(select(User).where(
            User.username == request.username)).all()
        if existed:
            raise HTTPException(status_code=400, detail="用户名已被注册,请换一个!")
        user.username = request.username if request.username else user.username
        user.password = request.password if request.password else user.password
        user.phone_number = request.phone_number if request.phone_number else user.phone_number
        user.language_excellent = (request.language_excellent
                                   if request.language_excellent
                                   else user.language_excellent)
        session.add(user)
        session.commit()
        session.refresh(user)
        response = JSONResponse(
            content={"message": "用户数据更新成功", "user": user.username})
        return response
