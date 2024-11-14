from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import SessionLocal, engine
import uvicorn

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET 操作

@app.get("/questions/{question_id}")
def get_question(question_id: int, db: Session = Depends(get_db)):
    """特定の質問をIDで取得"""
    question = crud.get_question(db=db,question_id=question_id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@app.get("/choices/{choice_id}")
def get_choice(choice_id: int, db: Session = Depends(get_db)):
    """特定の選択肢をIDで取得"""
    choice = crud.get_choice(db=db,choice_id=choice_id)
    if choice is None:
        raise HTTPException(status_code=404, detail="Choice not found")
    return choice

# POST 操作

@app.post("/questions/")
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    return crud.create_question(db=db,question=question)

@app.post("/choices/")
def create_choice(choice: schemas.ChoiceCreate, question_id: int, db: Session = Depends(get_db)):
    return crud.create_choice(db=db,choice=choice,question_id=question_id)

if __name__ == '__main__':
    uvicorn.run(app=app)
