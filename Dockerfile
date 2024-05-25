FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install pytest

ENTRYPOINT ["pytest"]

CMD mkdir -p /app/test-results && pytest --junitxml=/app/test-results/results.xml -v
