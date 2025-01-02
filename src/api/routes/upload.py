from fastapi import APIRouter, UploadFile, File
from google.cloud import storage
import os

from src.api.services.upload_service import upload_service
from src.api.schemas.judge import JudgeRequest, JudgeResponse

router = APIRouter()


@router.post("/upload")
async def upload_file(
        file: UploadFile = File(...),
        bucket_name: str = "zenn-ai-agent-hackathon-phase-1"
) -> JudgeResponse:
    request = JudgeRequest(file=file, bucket_name=bucket_name)
    return await upload_service(request)
