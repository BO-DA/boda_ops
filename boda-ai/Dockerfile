FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime

LABEL maintainer="KIM JINJAE <jinjae.dev@gmail.com>"

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
