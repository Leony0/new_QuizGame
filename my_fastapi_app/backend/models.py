#モデルの作成

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, index=True)
    q_content = Column(String,index=True)
    #email = Column(String, unique=True, index=True)
    #hashed_password = Column(String)
    #is_active = Column(Boolean, default=True)

    choice = relationship("Choice", back_populates="owner")
    #items = relationship("Item", back_populates="owner")


class Choice(Base):
    __tablename__ = "choice"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
    is_answer = Column(Boolean, default=True)
    question_id = Column(Integer, ForeignKey("question.id"))

    owner = relationship("Question", back_populates="choice")
    #owner = relationship("User", back_populates="items")

#class Item(Base):
#    __tablename__ = "items"
#
#    id = Column(Integer, primary_key=True, index=True)
#    title = Column(String, index=True)
#    description = Column(String, index=True)
#   owner_id = Column(Integer, ForeignKey("users.id"))

#    owner = relationship("User", back_populates="items")