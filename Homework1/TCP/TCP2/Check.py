#!/usr/bin/env python
import sys
import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5008
TEMP = 'UploadPicture/'
FileName = 'JOJO.jpg'

print "Picture:",TEMP+FileName
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

UploadFile = open(TEMP+FileName,"rb")
Read = UploadFile.read(1024)

while Read:
    sock.send(Read)
    Read = UploadFile.read(1024)

print "Done"

