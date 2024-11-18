from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from utils.database import Base

class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    questions = relationship("Question", back_populates="topic")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}