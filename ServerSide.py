import socket, threading

HOST = 'localhost'
PORT = 32014
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST,PORT))
serverSocket.listen()

Connections = []
print(f'Chat Room started on {str(PORT)}')

def newClient():
    while True:
            clientSocket, clientAddress = serverSocket.accept()
            userName = clientSocket.recv(1024)  
            Connections.append((userName, clientSocket))
            
            print(f'{userName} JOINED the Chat Room')
            sendMessage(clientSocket, userName, f'Joined'.encode())
            
            threadClient = threading.Thread(target = transmitionSYS, args=[userName, clientSocket])
            threadClient.start()  

def transmitionSYS(userName, clientSocket):
    while True:
        try:
            data = clientSocket.recv(1024)
            if data:
                print(f'New Message: {userName}')
                sendMessage(clientSocket, userName, data)
        except:
            sendMessage(clientSocket,userName, f'left the Chat Room'.encode())
            print(f'{userName} LEFT the Chat Room')
            Connections.remove((userName, clientSocket))
            clientSocket.close()
            break

def sendMessage(clientSocket, userName, data):
    for client in Connections:
        if client[1] != clientSocket:
            client[1].send(userName)
            client[1].send(data)
   
newClient()
