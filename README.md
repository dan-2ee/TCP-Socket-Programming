# TCP-Socket-Programming

## 구현 내용 <br/>
- 소켓 통신을 활용하여 Server, Client 프로그램 작성
- TCP 기반 소켓프로그래밍 작성 후 Client에서는 HTTP 프로토콜의 GET/HEAD/POST/PUT Request를 요청하고, Server에서는 Client의 Request에따라 응답 메시지를 구성하여 Response 하도록 구현
- 사용한 프로그래밍 언어: python 
- 입출력에 이용한 파일 형식: html
- localhost로 진행
- HTTP 명령어 수행시에 Server에서 Client가 요청하는 파일을 실제로 생성하고, update하며 실제 환경에 맞는 Response State를 회신함

<br/>

## HTTP 명령어 수행 결과 <br/>
💭 GET 수행 
: GET 명령어 뒤에 파일 이름을 입력하면, 서버에서 해당 파일을 읽어 들인 뒤 파일 내용을 body에 담아 클라이언트에게 전송합니다. 클라이언트에서 GET test.html 을 요청하면 서버에서 test.html이라는 이름의 파일이 존재하는지 확인후 파일의 내용을 response의 body에 담아 전송하게 됩니다. 

- Server 출력 내용
<img width="452" alt="image" src="https://user-images.githubusercontent.com/65989401/168011693-093ac80b-9fc4-4b84-bfbc-950207223a9b.png">

- Client 출력 내용
<img width="452" alt="image" src="https://user-images.githubusercontent.com/65989401/168011712-65d76bbb-7bb2-4fb0-95b3-62e57689ee1b.png">

- Test.html 파일 내용 
<img width="452" alt="image" src="https://user-images.githubusercontent.com/65989401/168011738-80f6abe2-ecf1-46de-a9c4-6b5d612091ec.png">

<br>
💭 HEAD 수행
: HEAD 요청 방식은 GET과 유사한 방식이지만 서버에서 헤더 정보 이외에는 어떤 데이터도 보내지 않습니다. 클라이언트에서 HEAD test.html 을 요청하면 서버에서 test.html이라는 이름의 파일이 존재하는지 확인 후, 파일 내용 본문을 포함하지 않고, 헤더 정보만을 response에 담아 클라이언트로 전송합니다.

- Server 출력 내용
<img width="452" alt="image" src="https://user-images.githubusercontent.com/65989401/168012350-8b694fca-5b61-4871-8b23-179c9aff9678.png">

- Client 출력 내용
<img width="452" alt="image" src="https://user-images.githubusercontent.com/65989401/168012372-16ddd26b-5df3-46b2-a424-e9f12117758e.png">

- Test.html 파일 내용 
<img width="452" alt="image" src="https://user-images.githubusercontent.com/65989401/168012402-60fa8924-7d5c-483c-885d-8b1313de2329.png">

<br>
💭 PUT 수행 
: 클라이언트에서 <PUT 파일명 추가할 태그 내용>을 입력하면, 서버에서 해당 파일이 존재하는지 확인 후 FileNotFoundError가 발생하지 않으면, 해당 파일의 body 태그 안에 클라이언트가 입력한 태그 내용을 추가합니다. 

- Server 출력 내용
<img width="452" alt="image" src="https://user-images.githubusercontent.com/65989401/168021815-96d3ac40-4e96-4447-9970-0d170dccc2ca.png">

- Client 출력 내용
<img width="452" alt="image" src="https://user-images.githubusercontent.com/65989401/168021369-73ddabb7-a510-4753-ae7d-ef7c81992852.png">

- PUT 요청 전 test.html 파일 내용
<img width="452" alt="image" src="https://user-images.githubusercontent.com/65989401/168021415-efc152f9-ab34-4509-8a77-07c5366f18f7.png">

- PUT 요청 후 test.html 파일 내용 
<img width="452" alt="image" src="https://user-images.githubusercontent.com/65989401/168021441-f2fba4a7-030f-4425-bfd6-f8b62790a0c6.png">

<br>
💭 POST 수행 
: 클라이언트에서 <POST 생성할 파일명 파일 내용> 을 요청하면, 서버에서 해당 파일 내용으로 새로운 파일을 생성하고, 파일 내용을 response의 body에 담아 클라이언트에게 전송합니다. 

- Server 출력 내용
<img width="452" alt="image" src="https://user-images.githubusercontent.com/65989401/168022869-d4d8dccb-1ba7-4904-9d7d-8e0f574efd25.png">

- Client 출력 내용
<img width="452" alt="image" src="https://user-images.githubusercontent.com/65989401/168022905-6f86cbdc-8c53-4776-8404-fadf1cb9126b.png">

- POST 요청 후 생긴 파일 내용
<img width="452" alt="image" src="https://user-images.githubusercontent.com/65989401/168022940-c8067a6d-dd6a-450b-b81a-73bd420bee37.png">

<br/>

## 응답 코드 <br/>
✔️ GET
- 200 (Success): 클라이언트의 요청이 성공적으로 처리된 경우 -> 클라이언트가 요청한 파일 내용 반환
- 400 (Bad Request): 클라이언트의 요청 자체가 잘못된 경우
- 404 (Not Found): 클라이언트에서 요청한 파일이 존재하지 않는 경우 (찾는 리소스가 없는 경우)

✔️ HEAD
- 200 (Success): 클라이언트의 요청이 성공적으로 처리된 경우 -> server의 현재 상태 반환
- 400 (Bad Request): 클라이언트의 요청 자체가 잘못된 경우

✔️ PUT
- 200 (Success): 클라이언트의 요청이 성공적으로 처리된 경우 -> 파일의 body 태그 안에 내용 추가 후 파일 내용 반환
- 400 (Bad Request): 클라이언트의 요청 자체가 잘못된 경우
- 404 (Not Found): 클라이언트에서 요청한 파일이 존재하지 않는 경우 (찾는 리소스가 없는 경우)

✔️ POST
- 201 (Created): 클라이언트의 요청이 성공적으로 처리되어 리소스가 만들어진 경우 -> 클라이언트가 원하는 이름, 내용으로 리소스 생성 후 파일 내용 반환 
- 400 (Bad Request): 클라이언트의 요청 자체가 잘못된 경우

<br/>

## 동작 환경 <br/>
- localhost로 구현
- server,client 모두 동일한 Mac OS 이용
- root and request path: 127.0.0.1
