from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi_snake_app.db import engine
from sqlmodel import Session, select
from fastapi_snake_app.db.user import User

from fastapi_snake_app.main import app


def login_check(username: str, password: str) -> bool:
    with Session(engine) as session:
        pwd = session.exec(select(User).where(User.username==username)).one()
        return pwd[2] == password


@app.post('/login')
async def login(credentials: dict, response: JSONResponse):
    username = credentials.get('username',None)
    password = credentials.get('password',None)
    if not username or not password:
        raise HTTPException(status_code=400, detail="Not Input username or password")
    elif not login_check(username, password):
        raise HTTPException(status_code=401, detail="Wrong username or password")
    response.set_cookie(key="username", value=username)
    return {"msg": "Login Successfully"}
