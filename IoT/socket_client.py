from socket import *

IP_ADDRESS = "18.169.67.45"
PORT = 8902

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((IP_ADDRESS, PORT))

print('접속 완료')

while True:
    recvData = clientSock.recv(1024)
    if recvData.decode('utf-8') == "quit":
        print('상대방 :', recvData.decode('utf-8'))
        break
    else:
        print('상대방 :', recvData.decode('utf-8'))



