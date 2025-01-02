import os
import json
from google.cloud import storage

from src.agents.judge.judge_agent import judge_text
from src.api.schemas.judge import JudgeRequest, JudgeResponse


async def upload_service(request: JudgeRequest):
    try:
        # ファイルの内容を読み取る
        content = await request.file.read()
        text_content = content.decode("utf-8")

        # テキストを判定
        judge_result: JudgeResponse = judge_text(text_content, json.dumps(JudgeResponse.model_json_schema(), ensure_ascii=False, indent=2))

        # 一時ファイルとして保存
        temp_file_path = f"temp_{request.file.filename}"
        with open(temp_file_path, "wb") as buffer:
            buffer.write(content)

        # Google Cloud Storageにアップロード
        if request.bucket_name:
            storage_client = storage.Client()
            bucket = storage_client.bucket(request.bucket_name)
            blob = bucket.blob(request.file.filename)
            blob.upload_from_filename(temp_file_path)

        # 一時ファイルを削除
        os.remove(temp_file_path)

        return judge_result
    except Exception as e:
        return {"error": str(e)}
