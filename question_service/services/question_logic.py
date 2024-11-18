from question_service.models.question import Question
from sqlalchemy.orm import Session
from sqlalchemy import func


def get_questions(db: Session, part: int = None, topic_id: int = None, skip: int = 0, limit: int = 100):
    query = db.query(Question)
    if part:
        query = query.filter(Question.part == part)
    if topic_id:
        query = query.filter(Question.topic_id == topic_id)

    print(query)

    return query.offset(skip).limit(limit).all()


def get_random_question(db: Session, part: int = None, topic_id: int = None):
    query = db.query(Question)
    if part:
        query = query.filter(Question.part == part)
    if topic_id:
        query = query.filter(Question.topic_id == topic_id)
    return query.order_by(func.random()).first()


def create_question(db: Session, text: str, part: int, topic_id: int, youtube_video_id: str = None):
    new_question = Question(text=text, part=part, topic_id=topic_id, youtube_video_id=youtube_video_id)
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question