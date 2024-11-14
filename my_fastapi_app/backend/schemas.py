#Pydanticを用いてスキーマを作成

from typing import List, Optional
from pydantic import BaseModel


class ChoiceBase(BaseModel):
    content:str
    #description: Optional[str] = None


class ChoiceCreate(ChoiceBase):
    pass


class Choice(ChoiceBase):
    id: int
    is_answer: bool
    question_id: int

    #owner_id: int

    class Config:
        orm_mode = True

#####################################

class QuestionBase(BaseModel):
    q_content: str


class QuestionCreate(QuestionBase):
    pass


class Question(QuestionBase):
    id: int
    #is_active: bool
    #items: List[Item] = []

    class Config:
        orm_mode = True
