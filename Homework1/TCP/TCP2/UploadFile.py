#!/usr/bin/env python
import sys
import socket
import os

TCP_IP = '127.0.0.1'
TCP_PORT = 5008
FileName = 'JOJO.jpg'

print "Namepicture:",FileName
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(10)


while 1:
    data, addr = s.accept()
    NewFolder = r'UploadPicture/'
    if not os.path.exists(NewFolder):
        os.makedirs(NewFolder)


    UploadFile = open(NewFolder+FileName,"wb")
    Data = data.recv(1024)
    while Data:
        UploadFile.write(Data)
        Data= data.recv(1024)
    print "Upload File Completed"


s.close()
    

