from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class Budget(Base):
    __tablename__ = 'budgets'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True, index=True)
    monthly_budget = Column(Float, default=0.0)

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    amount = Column(Float)
    category = Column(String)
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

class MessageHistory(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    message = Column(String)
    reply = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)