from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes import upload

app = FastAPI()
app.include_router(upload.router)

# CORSの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
