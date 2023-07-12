from sqlmodel import Session, select

from fastapi_snake_app.db import engine
from fastapi_snake_app.db.user import User
from fastapi_snake_app.main import app


@app.get('/users')
async def read_users() -> list[User]:
    pass
    # with Session(engine) as session:
    #     users = session.exec(select(User)).all()
    #     return users


# @app.post('/user')
# async def create_user(user: User):
#     with Session(engine) as session:
#         session.add(user)
#         session.commit()
#         session.refresh(user)
#         return user
