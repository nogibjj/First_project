install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

#checks python files
lint:
	pylint --ignore-patterns=test_main.*?py *.py

test:
	python -m pytest -cov=main test_main.py
	py.test --nbval

all: 
	install format lint test