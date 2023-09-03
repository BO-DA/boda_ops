from flask import Flask, Response, render_template
import cv2
import threading

app = Flask(__name__)

class VideoStream:
    def __init__(self, rtsp_url):
        self.cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)
        self.frame = None
        self.is_running = True
        self.thread = threading.Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while self.is_running:
            ret, self.frame = self.cap.read()

    def get_frame(self):
        ret, jpeg = cv2.imencode('.jpg', self.frame)
        return jpeg.tobytes()

    def stop(self):
        self.is_running = False
        self.thread.join()
        self.cap.release()

video_stream = VideoStream("rtsp://127.0.0.1:8556/boda")

@app.route('/boda')
def index():
    return render_template('index.html')

def generate():
    while True:
        frame = video_stream.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=10000, threaded=True)
