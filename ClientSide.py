import socket, threading

def receive():
    while True:
            userName = clientSocket.recv(1024).decode('utf-8')
            data = clientSocket.recv(1024).decode('utf-8')
            print(f"\n[{str(userName)}] {str(data)}")
        
def send():
    while True:
        clientSocket.send(input('\n ').encode('utf-8'))


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('localhost', 32014))

print('[Connected to the Chat Room!]')
clientSocket.send(input('Enter your nickname: ').encode('utf-8'))

threadReceive = threading.Thread(target = receive)
threadReceive.start()

threadSend = threading.Thread(target = send)
threadSend.start()
