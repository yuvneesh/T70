import socket
import parser_1 as parse

IP_ADDRESS = "192.168.0.230"
PORT = 6000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP_ADDRESS, PORT))

message = "Hello from the Mac OS computer"
client_socket.sendall(message.encode())


raw = ''

while True:
    data = client_socket.recv(1024)
    if not data:
        break

    #print("Received message from server: {}".format(data))
    print(data)
    raw += data.decode()

    if "</MT>" in raw:
        break

info = parse.read_data(raw)
print(info)

client_socket.close()


