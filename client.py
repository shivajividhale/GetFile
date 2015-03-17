from Tools.Scripts.treesync import raw_input

__author__ = 'Shivaji'

import socket

s=socket.socket()
port=12345
s.connect((socket.gethostname(),port))
data=s.recv(1024)
input=raw_input(data.decode("utf-8"))
print("file name:",input)
i=0
input=input.replace("\n","")
"""
while input[i] != "\n":
    input1[i] = input[i]
    i=i+1
"""
s.send(bytes(input, "utf-8"))
fileContent=s.recv(1024)
#print("File contents: ",fileContent.decode("UTF-8"))
newFile=open("_"+input,"wb")
newFile.write(fileContent)
s.close()