import socket
from time import sleep
from SPyFT.settings import *


class Sender(object):
    def __init__(self, ip=socket.gethostname(), port=DEFAULT_PORT):
        self.ip = ip
        self.port = port

    def send(self, path):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        # Sending file name
        file_name = path.split('/')[-1]
        s.send(bytes(f"{len(file_name):<{HEADERSIZE}}", 'utf-8')+bytes(file_name, 'utf-8'))
        # Small wait time for server to react for filename
        sleep(0.1)

        # Opening and sending file
        try:
            fp = open(path, "rb")
        except FileNotFoundError as eee:  # Noice name
            print(f"{eee}, Cannot send a file which does not exist")
            return -1

        msg = fp.read()
        msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg

        s.send(msg)
        s.close()
        fp.close()
