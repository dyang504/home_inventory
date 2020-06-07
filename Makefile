serve:
	uvicorn backend.main:app --reload

test:
	pytest -v

freeze:
	pip freeze > requirements.txt