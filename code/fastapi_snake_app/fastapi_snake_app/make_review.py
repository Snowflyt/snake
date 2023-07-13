from datetime import datetime

from fastapi import Body
from pydantic import BaseModel
from sqlmodel import Session

from fastapi_snake_app.db import engine
from fastapi_snake_app.db.review import Review
from fastapi_snake_app.main import app


class ReviewMade(BaseModel):
    id: int
    user_id: int
    username: str | None
    content: str
    submit_time: datetime = datetime.today()


@app.post("/makeReviews", description="用于用户发表评论", tags=['用户基本操作'])
async def make_review(review_made: ReviewMade = Body(..., example={"id": "评论id,必填，格式要求是整型",
                                                                   "user_id": "用户id,必填，格式要求是整型",
                                                                   "username": "用户名,选填，如果不填代表匿名发布，格式要求是字符串",
                                                                   "content": "评论文本的内容，必填，格式要求是字符串"
                                                                   })):
    with Session(engine) as session:
        id = review_made.id
        user_id = review_made.user_id
        username = review_made.username
        content = review_made.content
        submit_time = datetime.today()
        review = Review(id=id, user_id=user_id, username=username, content=content, submit_time=submit_time)
        session.add(review)
        session.commit()
        session.refresh(review)
        return {"message": "Review created successfully"}
