from fastapi import HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi_snake_app.db import engine
from fastapi.encoders import jsonable_encoder
from sqlmodel import Session, select
from fastapi_snake_app.db.user import User

from fastapi_snake_app.main import app


class Credential(BaseModel):
    username: str
    password: str


def login_check(username: str, password: str) -> bool:
    with Session(engine) as session:
        pwd = session.exec(select(User).where(User.username == username)).one()
        return pwd.password == password


@app.post('/login')
async def login(credentials: Credential):
    credentials_dict=jsonable_encoder(credentials)
    username = credentials_dict.get('username', None)
    password = credentials_dict.get('password', None)
    if not username or not password:
        raise HTTPException(status_code=400, detail="Not Input username or password")
    elif not login_check(username, password):
        raise HTTPException(status_code=401, detail="Wrong username or password")
    response=JSONResponse(content={"message": "Login Successfully"})
    response.set_cookie(key="username", value=username)
    return response
