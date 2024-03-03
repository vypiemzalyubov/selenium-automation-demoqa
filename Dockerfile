FROM python:3.11-slim-bullseye
WORKDIR /src
USER root
COPY requirements.txt /src/
RUN pip install -r requirements.txt
COPY . /src/