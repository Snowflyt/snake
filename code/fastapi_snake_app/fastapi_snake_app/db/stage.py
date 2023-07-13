from sqlmodel import Field, SQLModel  # type: ignore


class Stage(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    sname: str = Field(default=str(id) if id else None,
                       nullable=False, unique=True)
    unlock_precondition_stars: int = Field(nullable=False)
