FROM ubuntu:20.04

LABEL maintainer="KIM JINJAE <jinjae.dev@gmail.com>"

# install requirements
RUN apt-get update && apt-get -y upgrade && \
    apt-get -y install ffmpeg

# ffmpeg command
CMD ["ffmpeg", "-re", "-rtsp_flags", "listen", "-i", "rtsp://127.0.0.1:8556", "-an", "-r", "4", "-f", "rtsp", "rtsp://127.0.0.1:8554/boda", "-vsync", "2"]
