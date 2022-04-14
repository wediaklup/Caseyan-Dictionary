import socket
from api import essentials

s = socket.socket()
HOST = "LAPTOP-WDK"
PORT = 8080


def conn_test():
    try:
        s.connect((HOST, PORT))
        return True
    except Exception as e:
        essentials.error_msg(e, "ESTABLISHING CONNECTION")
        return False


def receive():
    try:
        f = open("liste.kaz", "wb")
        file_data = s.recv(65536)
        f.write(file_data)
        f.close()
        print("Received")
    except Exception as e:
        essentials.error_msg(e, msg_box=True)


if __name__ == '__main__':
    receive()