from sqlalchemy.orm import Session
from answer_service.models.answer import Answer

def create_answer(db: Session, question_id: int, user_id: int, audio_url: str, text: str):
    new_answer = Answer(
        question_id=question_id, user_id=user_id, audio_url=audio_url, text=text
    )
    db.add(new_answer)
    db.commit()
    db.refresh(new_answer)
    return new_answer

def get_latest_answer(db: Session, question_id: int):
    return (
        db.query(Answer)
        .filter(Answer.question_id == question_id, Answer.is_hidden == False)
        .order_by(Answer.created_at.desc())
        .first()
    )

def get_all_answers_by_question(db: Session, question_id: int):
    return db.query(Answer).filter(Answer.question_id == question_id).all()


def hide_previous_answers(db: Session, question_id: int, current_answer_id: int):
    db.query(Answer).filter(
        Answer.question_id == question_id, Answer.id != current_answer_id
    ).update({"is_hidden": True})
    db.commit()