import socket
CHUNK = 65535
port = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


hostname = "127.0.0.1"

while True:
    s.connect((hostname, port))
    message = input("Type message: ")
    data = message.encode('ascii')
    s.send(data)
    data = s.recv(CHUNK)
    text = data.decode('ascii')
    print(f"Devesh says {text} ")