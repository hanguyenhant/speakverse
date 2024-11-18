from sqlalchemy import Column, Integer, String, DateTime, func
from utils.database import Base
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash # Thư viện để hash password


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False) # Lưu trữ password đã được hash
    email = Column(String, unique=True, index=True) # có thể không bắt buộc
    created_at = Column(DateTime, default=func.now())

    #relationship
    answers = relationship("Answer", back_populates="user")


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    # chuyển object -> dict
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}