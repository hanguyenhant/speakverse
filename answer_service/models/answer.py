from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, func, Boolean
from sqlalchemy.orm import relationship
from utils.database import Base


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Liên kết với User Service
    audio_url = Column(String)
    text = Column(Text)
    created_at = Column(DateTime, default=func.now())
    is_hidden = Column(Boolean, default=False)  # Ẩn câu trả lời cũ

    question = relationship("Question", back_populates="answers")
    user = relationship("User", back_populates="answers") # relationship với User