from sqlmodel import Session, select

from fastapi_snake_app.db import engine
from fastapi_snake_app.db.play import Play
from fastapi_snake_app.main import app


@app.get('/plays')
async def read_notes() -> list[Play]:
    with Session(engine) as session:
        plays = session.exec(select(Play)).all()
        return plays


@app.post('/play')
async def create_note(play: Play):
    with Session(engine) as session:
        session.add(Play)
        session.commit()
        session.refresh(Play)
        return play