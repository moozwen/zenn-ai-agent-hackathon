from fastapi import UploadFile, File
from pydantic import BaseModel
from typing import Literal


class JudgeRequest(BaseModel):
    file: UploadFile = File(...)
    bucket_name: str = None


class JudgeResponse(BaseModel):
    judge_result: Literal["danger", "gray", "safe"]
    message: str
