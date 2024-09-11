from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session
from datetime import datetime
import uuid
from .engine.db import Base

class User(Base):
    __tablename__ = 'users'

    userID = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(32), unique=True, index=True)
    userName = Column(String(50), unique=True)
    email = Column(String(50))
    password = Column(String(64))
    password_reset = Column(String(64))
    mobile_access = Column(String(10))
    register_since = Column(DateTime, default=datetime.now)
    last_login = Column(Integer)
    user_ip = Column(String(45))

    @staticmethod
    def create_user(db: Session) -> str:
        unique_id = uuid.uuid4().hex
        current_time = datetime.now()

        user = User(
            user_id=unique_id,
            register_since=current_time
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user.user_id
        
    def fetch_user_by_id(db: Session, user_id: str):
        return db.query(User).filter(User.user_id == user_id).first()
