FROM python:3.6.4-alpine3.7

RUN apk update && apk add bash


WORKDIR /app

COPY ./requirements.txt /etc

RUN apk --update add python py-pip openssl ca-certificates py-openssl wget
RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
  && pip install --upgrade pip \
  && pip install -r /etc/requirements.txt \
  && apk del build-dependencies

ENV FLASK_ENV="development"
ENV FLASK_APP="app.py"

EXPOSE 8080

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]