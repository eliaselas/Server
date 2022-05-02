import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 444
serversocket.bind(("###.##.###.###", 6677))

serversocket.listen(3)
while True:
    clientsocket,address = serversocket.accept()

    print("receive connection from %s " % str(address))

    message = 'hello! Trank you for connecting to the server' + "\r\n"
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()
