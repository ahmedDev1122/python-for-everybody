'''

You are to retrieve the following document using the HTTP protocol
in a way that you can examine the HTTP Response headers.

http://data.pr4e.org/intro-short.txt
'''

import socket

# server info
site = 'data.pr4e.org'
port = 80

# create socket and connect
sock = socket.socket()
sock.connect((site, port))

# send GET request
msg = 'GET /intro-short.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'
sock.send(msg.encode())

# receive and print response
while True:
    reply = sock.recv(512)
    if len(reply) < 1:
        break
    print(reply.decode())

sock.close()
