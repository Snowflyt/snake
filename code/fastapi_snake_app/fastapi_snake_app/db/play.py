from sqlmodel import Field, SQLModel


class Play(SQLModel, table=True):
    user_id: str = Field(default=id, nullable=False,primary_key=True)
    stage_id: str = Field(default=False, nullable=False,primary_key=True)
    isLocked: bool = Field(nullable=False)
    starsAlreadyGet: int = Field(max_items=3, min_items=0, nullable=False)