
FROM python:3.8


WORKDIR /app

RUN pip install flake8

COPY . .

RUN flake8 --ignore=E501 .
