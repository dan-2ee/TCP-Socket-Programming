from socket import *

HOST = 'localhost'  
PORT = 1234

def create_socket_and_send_message(request_message):
    # 클라이언트 소켓 만들기
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((HOST, PORT))
    clientSocket.send(request_message.encode())

    # 응답 확인
    data = clientSocket.recv(1024)
    print('Received', data.decode())

    clientSocket.close()


while (True):
    value = input("Enter the HTTP command ")
    create_socket_and_send_message(value)