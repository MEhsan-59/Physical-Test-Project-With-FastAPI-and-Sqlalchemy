from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from schema import AddUserResponse, AddUserSchema
from database import get_db
from logger_setup import logger
from physical_manager import User
from physical_repository import Repository

app = FastAPI()

def get_test_manager(db: Session = Depends(get_db)):
    repo = Repository(db)
    return User(repo)

@app.post("/add-user", response_model=AddUserResponse)
def add_user_endpoint(data: AddUserSchema, manager: User = Depends(get_test_manager)):
    logger.info("API : Add User")
    status, msg = manager.add_user(data.user_name, data.user_age)
    if not status:
        return AddUserResponse(status=status, message=msg)
    return AddUserResponse(status=status, message=msg)
