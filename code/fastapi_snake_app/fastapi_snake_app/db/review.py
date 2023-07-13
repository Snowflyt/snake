from datetime import datetime

from sqlmodel import Field, SQLModel  # type: ignore


class Review(SQLModel, table=True):
    id: int = Field(primary_key=True, nullable=False)
    user_id: int = Field(default=None, nullable=False)
    username: str | None = Field(default=str(user_id) if id else None)
    content: str = Field(nullable=False)
    submit_time: datetime = Field(default=datetime.today())
