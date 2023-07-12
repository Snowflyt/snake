from datetime import datetime

from sqlmodel import Field, SQLModel  # type: ignore


class Review(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(default=str(id) if id else None)
    content: str=Field(nullable=False)
    submit_time: datetime=Field(default=datetime.today())

