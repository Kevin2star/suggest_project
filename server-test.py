import socket

# 서버 코드
HOST = '0.0.0.0'
PORT = 22

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"서버가 시작되었습니다.")
   
    conn, addr = s.accept()
    with conn:
        print(f"클라이언트 접속: {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"받은 메시지: {data.decode()}")
            conn.sendall("메시지 받았습니다!".encode())
