import socket
# import threading
import json
import time

def handle_client(client_socket):
    # 클라이언트에 응답 전송
    test = {
        "coordinates": [
            [(1.1, 2.2), (3.3, 4.4)],
            [(5.5, 6.6), (7.7, 8.8)]
        ],
        "direction": "normal"
    }

    # json 생성
    json_response = json.dumps(test)

    # while True:
    # json 전송
    client_socket.send(json_response.encode())
    print("Sending...", json_response)
    time.sleep(1)

    # # 연결 종료
    # client_socket.close()

def start_server():
    # 서버 설정
    host = '0.0.0.0'  # 모든 네트워크 인터페이스에서 수신 대기
    port = 13245

    # 소켓 생성 및 바인딩
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr[0]}:{addr[1]}")

    while True:
        # 클라이언트 연결 대기

        # client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        # client_handler.start()
        handle_client(client_socket)
        print("Here")
    client_socket.close()

if __name__ == "__main__":
    start_server()
