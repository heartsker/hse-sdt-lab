import uvicorn
from fastapi import FastAPI

from api.router import router

app = FastAPI()
app.include_router(
    router,
    prefix="/api"
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        port=9000,
        reload=True,
    )
