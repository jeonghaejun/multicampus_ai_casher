from socket import *

# # 도현
# IP_ADDRESS = "18.169.67.45"
# PORT = 8898

# # 로컬
# IP_ADDRESS = '172.30.1.101'
# PORT = 8898

# 건우
IP_ADDRESS = "3.35.190.203"
PORT = 8898

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((IP_ADDRESS, PORT))

print('접속 완료')

while True:
    recvData = clientSock.recv(1024)
    if recvData.decode('utf-8') == "":
        break
    else:
        print('상대방 :', recvData.decode('utf-8'))
