import socket, threading

def accept_client():
    while True: 
        cli_socket, cli_add = server_socket.accept()
        CONNECTION_LIST.append(cli_socket)
        
        thread_client = threading.Thread(target = broadcast_usr, args = [cli_socket])
        thread_client.start()

def broadcast_usr(cli_sock):
    #TODO Implementar exception + checagem para validação de Data
    while True:
      data = cli_sock.recv(1024)
      b_usr(cli_sock, data)
  

def b_usr(cs_sock, msg):
    for client in CONNECTION_LIST:
        if client != cs_sock:
            client.send(msg)

def main():  
    CONNECTION_LIST = []
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    HOST = '192.168.0.22'
    PORT = 5023
    server_socket.bind((HOST, PORT))
  
    server_socket.listen(1)
    print(f"Chat Room server started on: {str(PORT)}")

    thread_accepted = threading.Thread(target = accept_client)
    thread_accepted.start()--
    
main()
