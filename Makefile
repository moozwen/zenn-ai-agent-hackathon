.PHONY: api ui

api:
	uv run uvicorn src.api.main:app --reload

ui:
	uv run streamlit run src/web/main.py
