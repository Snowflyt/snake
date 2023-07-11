from sqlmodel import Field, SQLModel


class Stage(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    sname: str = Field(default=id, nullable=False, unique=True)
    isLocked: bool=Field(default=False,nullable=False)
    unlockPreconditionStars: int=Field(nullable=False)
