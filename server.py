from socket import *
import datetime

HOST = 'localhost'  
PORT = 1234

# TCP server socket 생성
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((HOST, PORT))

# 서버가 클라이언트의 접속을 허용하도록 합니다
serverSocket.listen()
print('The server is running')

GetResponse = "HTTP/1.1 {header[0]} {header[1]}\nDate: {date}\nHost: {url}\nContent-Type: text/html\nContent-Length: {l}\n\n{body}"
HeadResponse = "HTTP/1.1 {header[0]} {header[1]}\nDate: {date}\nHost: {url}\nContent-Type: text/html\nContent-Length: {l}\n"
PutResponse = "HTTP/1.1 {header[0]} {header[1]}\nDate: {date}\nHost: {url}\nContent-Type: text/html\nContent-Length: {l}\n\n{body}"
PostResponse = "HTTP/1.1 {header[0]} {header[1]}\nDate: {date}\nHost: {url}\nContent-Type: text/html\nContent-Length: {l}\n\n{body}"

def GET(socket, requestMessage):
    global GetResponse, HOST
    try:
        print("Perform a GET request")
        file = requestMessage[1]
        f = open(file, 'r')
        r = f.read()
        Response = GetResponse.format(
            header = [200, "OK"],
            date = datetime.datetime.now(),
            url = HOST, 
            l = len(r),
            body = r
        )
    except FileNotFoundError as e:
        print(e)
        Response = GetResponse.format(
            header = [404, "Not Found"],
            date = datetime.datetime.now(),
            url = HOST, 
            l = None,
            body = None,
        )
    except:
        Response = GetResponse.format(
            header = [400, "Bad Request"],
            date = datetime.datetime.now(),
            url = HOST, 
            l = None,
            body = None,
        )
    finally:
        socket.send(Response.encode())

def HEAD(socket, requestMessage):
    global HeadResponse, HOST
    try:
        print("Perform a HEAD request")
        file = requestMessage[1]
        f = open(file, 'r')
        r = f.read()
        Response = HeadResponse.format(
            header = [200, "OK"],
            date = datetime.datetime.now(),
            url = HOST, 
            l = len(r),
        )
    except:
        Response = HeadResponse.format(
            header = [400, "Bad Request"],
            date = datetime.datetime.now(),
            url = HOST, 
            l = None,
        )
    finally:
        socket.send(Response.encode())

def PUT(socket, requestMessage):
    global PutResponse, HOST
    try:
        print("Perform a PUT request")
        file = requestMessage[1]
        word = " ".join(requestMessage[2:])
        
        with open(file, 'r+') as f:             
            lines = ""
            for line in f:
                if(line.startswith('<body>')):      # body 태그로 시작하는 line을 찾음
                    lines += "<body>\n"
                    lines += "    <h2> {} </h2>\n".format(word)
                else:
                    lines += line
            # body 태그 안에 내용 추가 
            f = open(file, "w")
            f.write(lines)
            f.close()

        f = open(file, 'r')
        r = f.read()

        Response = PutResponse.format(
            header = [200, "OK"],
            date = datetime.datetime.now(),
            url = HOST, 
            l = len(r),
            body = r
        )  

    except FileNotFoundError as e:
        print(e)
        Response = PutResponse.format(
            header = [404, "Not Found"],
            date = datetime.datetime.now(),
            url = HOST, 
            l = None,
            body = None,
        )

    except:
        Response = PutResponse.format(
            header = [400, "Bad Request"],
            date = datetime.datetime.now(),
            url = HOST, 
            l = None,
        )

    finally:
        socket.send(Response.encode())

def POST(socket, requestMessage):
    global PostResponse, HOST
    try:
        print("Perform a POST request")
        file = requestMessage[1]
        content = " ".join(requestMessage[2:])
        f = open(file, "w")
        f.write(content)
        f.close()

        f = open(file, 'r')
        r = f.read()
        f.close()

        Response = PostResponse.format(
            header = [201, "Created"],
            date = datetime.datetime.now(),
            url = HOST, 
            l = len(r),
            body = r
        )  

    except:
        Response = PostResponse.format(
            header = [400, "Bad Request"],
            date = datetime.datetime.now(),
            url = HOST, 
            l = None,
        )

    finally:
        socket.send(Response.encode())

while True:
    # accept 함수에서 대기하다가 클라이언트가 접속하면 새로운 소켓 리턴 
    clientSocket, addr = serverSocket.accept()
    # 접속한 클라이언트의 주소
    print('Connected by', str(addr))
    message = clientSocket.recv(1024).decode()
    # 빈 문자열을 수신하면 루프를 중지합니다. 
    if not message:
        print("is an empty string")
        break
    
    requestMessage = message.split()
    request = requestMessage[0]
    
    if (request == "GET"):
        GET(clientSocket, requestMessage)
    elif (request == "HEAD"):
        HEAD(clientSocket, requestMessage)
    elif (request == "PUT"):
        PUT(clientSocket, requestMessage)
    elif (request == "POST"):
        POST(clientSocket, requestMessage)

    clientSocket.close()

serverSocket.close()