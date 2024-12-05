from pydantic import BaseModel, ConfigDict


class AskReq(BaseModel):
    question: str
    context: str


class AskRes(BaseModel):
    answer: str
