from fastapi import Body
from sqlmodel import Session, select

from fastapi_snake_app.db import engine
from fastapi_snake_app.db.play import Play
from fastapi_snake_app.main import app


@app.get('/plays', description="从游玩记录表中读取游玩记录", tags=['关卡基本操作'])
async def read_plays() -> list[Play]:
    with Session(engine) as session:
        plays = session.exec(select(Play)).all()
        return plays


@app.post('/play', description="向游玩记录表中添加游玩记录", tags=['关卡基本操作'])
async def create_play(play: Play = Body(..., example={"user_id": "用户id,必填，格式要求是整型",
                                                      "stage_id": "关卡id,必填，格式要求是整型",
                                                      "is_locked": "关卡是否解锁，选填，格式要求是布尔值",
                                                      "stars_already_get":"游玩该关卡已经得到的星星数,选填,格式要求是整型，默认值为0"
                                                      })):
    with Session(engine) as session:
        session.add(play)
        session.commit()
        session.refresh(play)
        return play
