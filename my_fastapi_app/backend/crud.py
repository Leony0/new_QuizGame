#操作について

from sqlalchemy.orm import Session
import models
import schemas


def get_question(db: Session, question_id: int):
    return db.query(models.Question).filter(models.Question.id == question_id).first()

def get_choice(db: Session, choice_id: int):
    return db.query(models.Choice).filter(models.Choice.id == choice_id).first()


#def get_user_by_email(db: Session, email: str):
#    return db.query(models.User).filter(models.User.email == email).first()


#def get_users(db: Session, skip: int = 0, limit: int = 100):
#    return db.query(models.User).offset(skip).limit(limit).all()


def create_question(db: Session, question: schemas.QuestionCreate):
    #fake_hashed_password = question.password + "notreallyhashed"
    db_user = models.User(q_content=question.q_content)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
