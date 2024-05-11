FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install flake8 pytest

RUN flake8 --ignore=E501 sorting.py test_sorting.py

CMD mkdir -p /app/test-results && pytest --junitxml=/app/test-results/results.xml -v
