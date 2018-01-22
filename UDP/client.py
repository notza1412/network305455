import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005


print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
number_1 = raw_input("number:")
print "number: ",number_1

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(number_1,(UDP_IP,UDP_PORT))
data,server = sock.recvfrom(1024)
print "show anwser",data
 
