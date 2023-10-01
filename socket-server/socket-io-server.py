import socketio
import eventlet

# 소켓IO 서버 생성
sio = socketio.Server()

# 이벤트 핸들러 함수 정의
@sio.event
def connect(sid, environ):
    print(f"클라이언트 {sid}가 연결되었습니다.")

@sio.event
def disconnect(sid):
    print(f"클라이언트 {sid}가 연결이 해제되었습니다.")

@sio.event
def message(sid, data):
    print(f"클라이언트 {sid}로부터 메시지 받음: {data}")
    # 클라이언트에게 메시지 전송
    sio.send(sid, "서버가 메시지를 받았습니다.")



if __name__ == '__main__':
    # 서버 실행
    # Flask 애플리케이션 생성
    app = socketio.WSGIApp(sio)
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 13245)), app)
