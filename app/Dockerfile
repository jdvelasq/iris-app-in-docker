FROM python:3.9-slim-buster

ENV LANG C.UTF-8 

WORKDIR /app
COPY . /app

RUN pip3 install  \    
    flask \
    scikit-learn

EXPOSE  5000
ENV DEBIAN_FRONTEND=dialog
WORKDIR /app
ENTRYPOINT python3 app.py