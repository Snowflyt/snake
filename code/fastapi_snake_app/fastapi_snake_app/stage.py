from sqlmodel import Session, select

from fastapi_snake_app.db import engine
from fastapi_snake_app.db.stage import Stage
from fastapi_snake_app.main import app


@app.get('/stages')
async def read_notes() -> list[Stage]:
    with Session(engine) as session:
        stages = session.exec(select(Stage)).all()
        return stages


@app.post('/stage')
async def create_note(stage: Stage):
    with Session(engine) as session:
        session.add(stage)
        session.commit()
        session.refresh(stage)
        return stage
