FROM python:3.6.4-alpine3.7

RUN apk update && apk add bash

WORKDIR /app

COPY ./requirements.txt /etc

RUN pip install -r /etc/requirements.txt

ENV FLASK_ENV="development"
ENV FLASK_APP="app.py"

EXPOSE 8080

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]