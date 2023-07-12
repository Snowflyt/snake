from sqlmodel import Field, SQLModel  # type: ignore


class Play(SQLModel, table=True):
    user_id: str = Field(nullable=False, primary_key=True)
    stage_id: str = Field(nullable=False, primary_key=True)
    is_locked: bool = Field(default=False,nullable=False)
    stars_already_get: int = Field(nullable=False)