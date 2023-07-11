from sqlmodel import Field, SQLModel


class Stage(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    sname: str = Field(default=id, nullable=False, unique=True)
    is_locked: bool = Field(default=False, nullable=False)
    unlock_precondition_stars: int = Field(nullable=False)
