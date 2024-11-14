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
    db_question = models.User(q_content=question.q_content)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question
 

def create_choice(db: Session, choice: schemas.ChoiceCreate, question_id: int):
    db_choice= models.Choice(choice, owner_id=question_id)
    db.add(db_choice)
    db.commit()
    db.refresh(db_choice)
    return db_choice
