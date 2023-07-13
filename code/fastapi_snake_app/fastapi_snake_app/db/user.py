from sqlmodel import Field, SQLModel  # type: ignore


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(default=str(id) if id else None, nullable=False, unique=True)
    password: str = Field(nullable=False, max_length=20, min_length=8)
    phone_number: str = Field(nullable=False, min_length=11, max_length=11)
    level: int = Field(nullable=False,default=1)
    experience: int = Field(nullable=False,default=0)
    common_money: int = Field(nullable=False,default=0)
    special_money: int = Field(nullable=False,default=0)
    total_stars: int = Field(default=0, nullable=False)
    rank: str = '最强青铜IV'
    score: int = Field(default=0)
    language_excellent:str=Field(default="全能")


