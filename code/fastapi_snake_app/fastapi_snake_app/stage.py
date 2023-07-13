from fastapi import Body
from sqlmodel import Session, select

from fastapi_snake_app.db import engine
from fastapi_snake_app.db.stage import Stage
from fastapi_snake_app.main import app


@app.get('/stages', description="从关卡表中读取关卡", tags=['关卡基本操作'])
async def read_stages() -> list[Stage]:
    with Session(engine) as session:
        stages = session.exec(select(Stage)).all()
        return stages


@app.post('/stage', description="向关卡表中添加关卡", tags=['关卡基本操作'])
async def create_stage(stage: Stage = Body(..., example={"id": "关卡id，选填，格式要求是整型或None，默认值为None",
                                                         "sname": "关卡名,必填，格式要求是字符串",
                                                         "unlock_precondition_stars": "解锁这一关卡所需要的星星数，选填，格式要求是整型，默认值为0",
                                                         })):
    with Session(engine) as session:
        session.add(stage)
        session.commit()
        session.refresh(stage)
        return stage
