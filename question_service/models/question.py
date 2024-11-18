from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from utils.database import Base
from topic_service.models.topic import Topic

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    part = Column(Integer, nullable=False)
    topic_id = Column(Integer, ForeignKey("topics.id"))
    youtube_video_id = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    topic = relationship("Topic", back_populates="questions")


    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}