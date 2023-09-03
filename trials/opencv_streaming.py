import cv2
import os

# RTSP 스트림 URL
rtsp_url = "rtsp://127.0.0.1:8556/boda"

# os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;0"

cap = cv2.VideoCapture(rtsp_url)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

if not cap.isOpened():
    print("Error: Cannot open stream")
    exit()

cv2.namedWindow("RTSP Stream", cv2.WINDOW_NORMAL)
cv2.resizeWindow("RTSP Stream", frame_width, frame_height)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Cannot read frame")
        break

    cv2.imshow("RTSP Stream", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# exit
cap.release()
cv2.destroyAllWindows()
