import socket

# the 0.0.0.0 is a filler

SERVER_HOST = "0.0.0.0"

# port 80(HTTP) may work better to hide the traffic
SERVER_PORT = 5003

BUFFER_SIZE = 1024 * 128

# separator string for sending 2 messages in one go

SEPARATOR = "<sep>"

# create a socket object

s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))

