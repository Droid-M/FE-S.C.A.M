FROM python:3.9.1

RUN apt update
RUN apt-get upgrade -y -s
RUN apt-get install -y -s git
RUN mkdir -p /app
WORKDIR /app

COPY . .

RUN pip install -r /app/requirements.txt