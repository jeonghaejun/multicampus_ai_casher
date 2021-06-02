from socket import *
import time

# IP_ADDRESS_PC = '172.31.1.75'
IP_ADDRESS = '172.30.1.101'
PORT = 8898

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind((IP_ADDRESS, PORT))
serverSock.listen(1)

print('%d번 포트로 접속 대기중...'%PORT)

connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속되었습니다.')
# sendData="hello"
# connectionSock.send(sendData.encode('utf-8'))
while True:
    x=input()
    if x == "":
        sendData="False"
        connectionSock.send(sendData.encode('utf-8'))