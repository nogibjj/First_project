install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

#checks python files
lint:
	pylint --ignore-patterns=test_script.*?py *.py
	ruff check

test:
	python -m pytest -cov=main test_script.py 
	py.test --nbval

all: 
	install format lint test