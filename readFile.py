__author__ = 'Shivaji'

obj=open("file1.txt","rb")
print("Name of file:",obj.name)
abc=obj.read()
print("File contents:",abc.decode())
