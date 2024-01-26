FROM python:latest

RUN mkdir -p /srv/app
COPY . /srv/app

WORKDIR /srv/app
RUN pip install -r requirements.txt
# RUN flask db init
# RUN flask db migrate
# RUN flask db upgrade
