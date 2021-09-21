
FROM python:3.9


WORKDIR Desktop/app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip
COPY ./requirements.txt .


RUN apk add --update --na-cache postgres-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
	gcc libc-dev linux-headers postgreswl-dev musl-dev zlib zlib-dev 




RUN pip install -r requirements.txt

RUN apk del .tmp-build-deps

RUN mkdir/app
COPY ./app/ChatApp

WORKDIR /app

