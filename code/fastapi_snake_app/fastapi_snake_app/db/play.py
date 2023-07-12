from sqlmodel import Field, SQLModel  # type: ignore


class Play(SQLModel, table=True):
    user_id: str = Field(default=id, nullable=False, primary_key=True)
    stage_id: str = Field(default=False, nullable=False, primary_key=True)
    is_locked: bool = Field(nullable=False)
    stars_already_get: int = Field(nullable=False)
