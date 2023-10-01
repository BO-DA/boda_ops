import socketio

# 소켓IO 클라이언트 생성
sio = socketio.Client()

# connect 이벤트 핸들러 함수 정의
@sio.event
def connect():
    print("서버에 연결되었습니다.")

# disconnect 이벤트 핸들러 함수 정의
@sio.event
def disconnect():
    print("서버와의 연결이 해제되었습니다.")

# message 이벤트 핸들러 함수 정의
@sio.event
def message(data):
    print(f"서버로부터 메시지 받음: {data}")

if __name__ == '__main__':
    # 서버에 연결
    sio.connect('http://192.168.0.5:13245')

    while True:
        # 메시지 입력 받기
        user_input = input("메시지를 입력하세요 (exit로 종료): ")

        # exit 입력 시 연결 종료
        if user_input.lower() == 'exit':
            break

        # 서버로 메시지 전송
        sio.send(user_input)

    # 연결 종료
    sio.disconnect()
