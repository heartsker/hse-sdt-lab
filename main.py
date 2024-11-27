import uvicorn
from fastapi import FastAPI
from api.router import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
