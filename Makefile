serve:
	uvicorn backend.main:app --reload

test:
	coverage run -m pytest -v
	coverage html

freeze:
	pip freeze > requirements.txt