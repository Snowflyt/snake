from sqlmodel import Field, SQLModel  # type: ignore


class Note(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    text: str
    completed: bool
