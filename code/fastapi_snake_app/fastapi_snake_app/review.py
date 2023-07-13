from fastapi import Body
from sqlmodel import Session, select

from fastapi_snake_app.db import engine
from fastapi_snake_app.db.review import Review
from fastapi_snake_app.main import app


@app.get('/reviews', description="从评论表中读取评论", tags=['用户基本操作'])
async def read_reviews() -> list[Review]:
    with Session(engine) as session:
        reviews = session.exec(select(Review)).all()
        return reviews


@app.post('/review', description="向评论表中添加评论", tags=['用户基本操作'])
async def create_review(review: Review = Body(..., example={"user_id": "用户id，必填，格式要求是整型",
                                                            "username": "用户名,选填，如果不填代表匿名发布，格式要求是字符串",
                                                            "content": "评论文本的内容，必填，格式要求是字符串"
                                                            })):
    with Session(engine) as session:
        session.add(review)
        session.commit()
        session.refresh(review)
        return review
