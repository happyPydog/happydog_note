.PHONY: test install

test:
	python -m pytest tests

install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
