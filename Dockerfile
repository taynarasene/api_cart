FROM python:3.6.4-alpine3.7

RUN apk update && apk add bash

WORKDIR /app

COPY ./requirements.txt /etc

RUN pip install -r /etc/requirements.txt

ENV FLASK_ENV="development"
EXPOSE 8080

ENV NAME api_app

CMD ["python", "app.py"]
