from pydantic import BaseModel
from pydantic import ConfigDict


class AskReq(BaseModel):
    question: str
    context: str


class AskRes(BaseModel):
    answer: str
