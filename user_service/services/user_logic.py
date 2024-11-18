from sqlalchemy.orm import Session
from user_service.models.user import User
from werkzeug.security import generate_password_hash

def create_user(db: Session, username: str, password: str, email: str = None):
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password_hash=hashed_password, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()