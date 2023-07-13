from sqlmodel import Session, select

from fastapi_snake_app.db import engine
from fastapi_snake_app.db.review import Review
from fastapi_snake_app.main import app


@app.get('/reviews')
async def read_reviews() -> list[Review]:
    with Session(engine) as session:
        reviews = session.exec(select(Review)).all()
        return reviews


@app.post('/review')
async def create_review(review: Review):
    with Session(engine) as session:
        session.add(review)
        session.commit()
        session.refresh(review)
        return review
