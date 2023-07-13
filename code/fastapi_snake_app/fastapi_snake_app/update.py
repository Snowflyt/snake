from fastapi import HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi_snake_app.db import engine
from fastapi.encoders import jsonable_encoder
from sqlmodel import Session, select
from fastapi_snake_app.db.user import User

from fastapi_snake_app.main import app


# 定义更新用户数据的请求模型
class UpdateUserRequest(BaseModel):
    username: str|None
    password: str|None
    phone_number: str|None
    language_excellent: str|None


@app.post('/update')
async def update(user_id:int,update_user_request: UpdateUserRequest):
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        results = session.exec(statement)
        user = results.one()
        user.username = update_user_request.username if update_user_request.username else user.username
        user.password = update_user_request.password if update_user_request.password else user.password
        user.phone_number = update_user_request.phone_number if update_user_request.phone_number else user.phone_number
        user.language_excellent = update_user_request.language_excellent if update_user_request.language_excellent else user.language_excellent
        session.add(user)
        session.commit()
        session.refresh(user)
        return {"message": "用户数据更新成功", "user": user.username}
