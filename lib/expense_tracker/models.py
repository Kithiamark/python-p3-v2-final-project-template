from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base, SessionLocal

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)

    expenses = relationship("Expense", back_populates="owner")

    def create(self, db):
        db.add(self)
        db.commit()
        db.refresh(self)

    def delete(self, db):
        db.delete(self)
        db.commit()

    @staticmethod
    def get_all(db):
        return db.query(User).all()

    @staticmethod
    def find_by_username(db, username):
        return db.query(User).filter(User.username == username).first()

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

class Expense(Base):
    __tablename__ = "expenses"

    expense_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    amount = Column(Float)
    category = Column(String)
    description = Column(String, nullable=True)
    expense_date = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", back_populates="expenses")

    def create(self, db):
        db.add(self)
        db.commit()
        db.refresh(self)

    def delete(self, db):
        db.delete(self)
        db.commit()

    @staticmethod
    def get_all(db):
        return db.query(Expense).all()

    @staticmethod
    def find_by_id(db, expense_id):
        return db.query(Expense).filter(Expense.expense_id == expense_id).first()

    def __repr__(self):
        return f"<Expense(amount={self.amount}, category='{self.category}', description='{self.description}')>"
