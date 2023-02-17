import socket
import subprocess
import os

#networking
#host is to be filled by server's IP address
host=""
port = 3072

s = socket.socket(socket.AF_NET, socket.SOCK_STREAM)
s.connect(host,port)


