FROM python:3.11-alpine

WORKDIR /app
COPY .. .


RUN pip install --upgrade pip --no-cache-dir


COPY ../requirements.txt .
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput