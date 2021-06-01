from socket import *

IP_ADDRESS_PC = '172.31.1.75'
PORT = 8902

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind((IP_ADDRESS_PC, PORT))
serverSock.listen(1)

print('%d번 포트로 접속 대기중...'%PORT)

connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속되었습니다.')

while True:
    sendData = input('>>>')
    if sendData == "quit":
        connectionSock.send(sendData.encode('utf-8'))
        break
    else:
        connectionSock.send(sendData.encode('utf-8'))