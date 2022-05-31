import socket

#get my ip and set port
hostname = socket.gethostname()
myip = socket.gethostbyname(hostname)

print(hostname)
print(myip)