from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, Table

from fastapi_snake_app.db import metadata

notes = Table('notes',
              metadata,
              Column('id', Integer, primary_key=True),
              Column('text', String),
              Column('completed', Boolean))


class NoteIn(BaseModel):
    text: str
    completed: bool


class Note(BaseModel):
    id: int
    text: str
    completed: bool
