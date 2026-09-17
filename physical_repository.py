from sqlalchemy.orm import Session
from models import  User
from logger_setup import logger
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select

class Repository:
    def __init__(self, db : Session):
        self.db = db

    def add_user(self, user_name, user_age):
        user = User(
            User_name=user_name,
            User_age=user_age
        )
        self.db.add(user)
        try:
            self.db.commit()
            self.db.refresh(user)
            logger.info(f"User added for user_id={user_name}")
            return user
        except IntegrityError:
            self.db.rollback()
            logger.error(f"Duplicate User attempt for user_id={user_name} on same date")
            return None
    
    def get_user_by_name(self, user_name):
        stmt = select(User).where(User.User_name==user_name)
        return self.db.execute(stmt).scalar_one_or_none()

    def get_user_by_id(self, user_id):
        stmt = select(User).where(User.User_id==user_id)
        return self.db.execute(stmt).scalar_one_or_none()

    def get_all_users(self):
        stmt = select(User)
        return self.db.execute(stmt).scalars().all()
