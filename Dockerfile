FROM python:3.9.0-alpine

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./store /my_app

WORKDIR /my_app

RUN python manage.py migrate
