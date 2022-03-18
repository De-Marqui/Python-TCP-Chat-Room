import socket, threading

def send():
    while True:
        cli_sock.send(input('\n').encode())

def receive():
    while True:
        sen_name = cli_sock.recv(1024)
        data = cli_sock.recv(1024)
        print(f"\n<{str(sen_name)}> {str(data)}")

if __name__ == "__main__":   
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    HOST = '192.168.0.22'
    PORT = 5023
    cli_sock.connect((HOST, PORT))
    
    print('[Connected to the server!]')
    uname = input('Enter your nickname: ')
    cli_sock.send(uname.encode())

    thread_send = threading.Thread(target = send)
    thread_send.start()
    thread_receive = threading.Thread(target = receive)
    thread_receive.start()
