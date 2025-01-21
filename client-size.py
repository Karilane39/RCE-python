import socket

#####################################################################

evil_socket_port = 6666
evil_socket_IP = '192.168.1.87'
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

####################################################################

client_socket.connect((evil_socket_IP,evil_socket_port))
print("connexion réussi")

while True:
    message = ""
    try :
        message = input(">>> ")
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(data)
    except KeyboardInterrupt:
        break

client_socket.close()