from sqlmodel import Session, select

from fastapi_snake_app.db import engine
from fastapi_snake_app.db.note import Note
from fastapi_snake_app.main import app


@app.get('/notes')
async def read_notes() -> list[Note]:
    with Session(engine) as session:
        notes = session.exec(select(Note)).all()
        return notes


@app.post('/note')
async def create_note(note: Note):
    with Session(engine) as session:
        session.add(note)
        session.commit()
        session.refresh(note)
        return note