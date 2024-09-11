from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime
import hashlib
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

    # User creation function
    @staticmethod
    def create_user(db: Session, password: str, salt: str) -> str:
        unique_id = uuid.uuid4().hex
        hashed_password = hashlib.sha1((password + salt).encode()).hexdigest()
        user = User(
            user_id=unique_id,
            password=hashed_password,
            register_since=datetime.now(),
            password_reset=hashlib.sha1('panadol71oking56wangkal93'.encode()).hexdigest()
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user.user_id

    # Update user information
    @staticmethod
    def update_user(db: Session, user_id_db: int, unique_id: str):
        db.query(User).filter(User.userID == user_id_db).update({
            User.user_id: unique_id,
            User.userName: unique_id,
            User.email: unique_id,
            User.last_login: int(datetime.timestamp(datetime.now())),
            User.user_ip: func.current_user_ip()  # Assuming a custom function to get the IP
        })
        db.commit()

    # Fetch user by user_id
    @staticmethod
    def fetch_user_by_id(db: Session, user_id: str):
        return db.query(User).filter(User.user_id == user_id).first()
