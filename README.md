# BODA_OPS
AI 영상 처리를 위해 Android Application과 AI 서버를 이어주는 작업 수행 기록을 남겨둔 레포지토리입니다.

## 경로 소개
 - trials: 직접 찾아보면서 작성하거나 테스트해 보았던 파일들을 정리하였습니다.

## 탐색한 레포지토리
RTSP 서버 관련해서 탐색해보고 사용해본 레포지토리입니다.
 - [Live-Streaming-using-OpenCV-Flask](https://github.com/NakulLakhotia/Live-Streaming-using-OpenCV-Flask)
 - [RTSP-Client-Server](https://github.com/mutaphore/RTSP-Client-Server)
 - [nginx-rtmp-module](https://github.com/arut/nginx-rtmp-module)
 - [v4l2rtspserver](https://github.com/mpromonet/v4l2rtspserver)

## 정리 + 알게 된 사실
 - ffplay 명령어로 영상을 바로 받아서 재생해볼 수 있습니다.
 - 결국 RTSP 영상 데이터를 들어오는 대로 output으로 보내는 절차 없이 바로 처리하고 확인할 수 있는 방법은 찾지 못했습니다.
    (ffmpeg에서는 output 을 지정해야 하는데, output을 mp4와 같은 파일로 지정하는 경우 파일에 저장된 앞부분부터 처리하는 문제가 있었습니다.)
 - 실시간 처리를 위해서 처음에는 ffmpeg에서 이미지로 캡쳐해서 저장하고, 그걸 모델에서 계속 받아서 처리하는 식으로 구현해보았습니다.
 - 그러나 이렇게 처리하면, 같은 이미지에 덮어씌우면서 업데이트하다 보니, 이미지가 가끔 제대로 처리되지 않는 문제가 생겼습니다.
 - 이 문제 해결을 위해 클라이언트(APP)에서 RTSP를 보내면 그걸 listen하는 ffmpeg 서버를 설정하고, ffmpeg 서버에서 처리를 위한 서버(localhost)에 영상을 보내는 식으로 구현하였습니다.
