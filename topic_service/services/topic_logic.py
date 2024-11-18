from sqlalchemy.orm import Session
from topic_service.models.topic import Topic

def get_all_topics(db: Session):
    return db.query(Topic).all()

def get_topic_by_id(db: Session, topic_id: int):
    return db.query(Topic).filter(Topic.id == topic_id).first()

def create_topic(db: Session, name: str, description: str = None):
    new_topic = Topic(name=name, description=description)
    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)
    return new_topic

def update_topic(db: Session, topic_id: int, name: str, description: str = None):
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if topic:
        topic.name = name
        topic.description = description
        db.commit()
        return topic
    return None

def delete_topic(db: Session, topic_id: int):
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if topic:
        db.delete(topic)
        db.commit()
        return True
    return False