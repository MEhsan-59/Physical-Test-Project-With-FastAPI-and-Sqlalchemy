# models.py
from datetime import datetime, date
from sqlalchemy import Column, Date, Integer, String, Float, Boolean, Sequence, UniqueConstraint, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()
emp_seq = Sequence('emp_seq', start=4000)

class User(Base):
    __tablename__ = "User"
    User_name = Column(String, nullable=False, index=True)
    User_id   = Column(Integer, emp_seq, server_default=emp_seq.next_value(), primary_key=True, index=True, unique=True)
    User_age  = Column(Integer, nullable=False)
    created_at= Column(Date, nullable=False, default=datetime.now) 
