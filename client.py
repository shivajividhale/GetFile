from Tools.Scripts.treesync import raw_input

__author__ = 'Shivaji'

import socket

s=socket.socket()
port=12345
s.connect((socket.gethostname(),port))
data=s.recv(1024)
input=raw_input(data.decode("utf-8"))
s.send(bytes(input,"utf-8"))
s.close()