FROM python:3.6.9-slim-stretch as development

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

EXPOSE 8080

# CMD python3 manage.py runserver 0.0.0.0:8080