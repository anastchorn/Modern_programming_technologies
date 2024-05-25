FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install pytest

CMD ["pytest", "--junitxml=/app/test-results/results.xml", "-v", "test_sorting.py"]
