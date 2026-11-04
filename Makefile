.PHONY: all test docs clean

all: test docs

test:
	uv run pytest --html=report.html --self-contained-html --cov-report=html --cov-report=term --cov-report=xml --cov-context=test --cov=src

docs:
	uv run zensical build

clean:
	find . -name "__pycache__" -type d | xargs rm -rf
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete