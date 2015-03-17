__author__ = 'Shivaji'
import socket
s=socket.socket()
port=12345
host=socket.gethostname()
s.bind((host,12345))
s.listen(5)

while True:
    con,addr=s.accept()
    print ('Connected to:',addr)
    con.send(bytes("Enter a string: \n",'UTF-8'))
    data=con.recv(1024)
    print(data.decode("UTF-8"))
    fileName=data.decode("UTF-8")
    print("File Name:",fileName)
    obj=open(fileName,"rb")
    abc=obj.read()
    #con.send(bytes(abc,'utf-8'))
    con.send(abc)
    con.close()

