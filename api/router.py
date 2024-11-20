from fastapi import APIRouter

from core.schemas.question import AskRes, AskReq
from services.runner import Runner

router = APIRouter()

@router.post("/ask", response_model=AskRes)
async def ask(req: AskReq):
    runner = Runner()
    AskRes.answer = runner.run(req.question, req.context)
    return AskRes