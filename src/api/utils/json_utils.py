import json
from pydantic import ValidationError, BaseModel


def validate_llm_response(llm_response: str, model_class):
    """
    LLMからのレスポンス文字列(llm_response)をJSONとして読み取り、
    指定されたPydanticモデル(model_class)に適合するか検証する。

    :param llm_response: LLMが返した文字列 (JSON想定)
    :param model_class: PydanticのBaseModelクラス
    :return: バリデーション済みのPythonオブジェクト, またはエラーメッセージ
    """
    try:
        # JSON文字列をパース
        parsed = json.loads(llm_response)

        # Pydanticモデルを用いたバリデーション
        validated = model_class.parse_obj(parsed)

        # バリデーションに成功した場合はオブジェクトを返す
        return validated

    except json.JSONDecodeError as e:
        # JSON自体が壊れている場合
        return f"JSONDecodeError: {str(e)}"

    except ValidationError as e:
        # Pydanticのバリデーションに失敗した場合
        return f"ValidationError: {str(e)}"