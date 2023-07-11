from databases.interfaces import Record

from fastapi_snake_app.db import database
from fastapi_snake_app.db.note import notes, Note, NoteIn
from fastapi_snake_app.main import app


@app.get('/notes', response_model=list[Note])
async def read_notes() -> list[Record]:
    query = notes.select()  # type: ignore
    return await database.fetch_all(query)  # type: ignore


@app.post('/note', response_model=Note)
async def create_note(note: NoteIn):
    query = notes.insert().values( # type: ignore
        text=note.text, completed=note.completed) 
    last_record_id = await database.execute(query)  # type: ignore
    return {**note.dict(), 'id': last_record_id}
