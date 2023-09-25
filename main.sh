# run docker container 
docker run --rm -it --network=host bluenviron/mediamtx:latest

# run docker container ffmpeg-rtsp
docker build -t ffmpeg-rtsp:latest ffmpeg-rtsp/
docker run ffmpeg-rtsp:latest
