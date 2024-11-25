import socket

# 클라이언트 코드
HOST = '서버_IP'  # 여기에 서버 VM의 IP 주소를 입력하세요
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = "안녕하세요!"
    s.sendall(message.encode())
    print(f"메시지 전송: {message}")
    
    data = s.recv(1024)
    print(f"서버 응답: {data.decode()}")