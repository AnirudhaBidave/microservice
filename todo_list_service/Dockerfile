FROM python:3.9-slim-buster

WORKDIR /app

RUN pip install flask watchdog prometheus_client psutil

COPY . /app

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host", "0.0.0.0"]
