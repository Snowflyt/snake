from datetime import datetime

from pydantic import BaseModel
from sqlmodel import Session

from fastapi_snake_app.db import engine
from fastapi_snake_app.db.review import Review
from fastapi_snake_app.main import app


class ReviewMade(BaseModel):
    id: int
    username: str | None
    content: str
    submit_time: datetime = datetime.today()


@app.post("/makeReviews")
async def create_review(review_made: ReviewMade):
    with Session(engine) as session:
        id = review_made.id
        username = review_made.username
        content = review_made.content
        submit_time = review_made.submit_time
        review = Review(id=id, username=username, content=content,submit_time=submit_time)
        session.add(review)
        session.commit()
        session.refresh(review)
        return {"message": "Review created successfully"}
