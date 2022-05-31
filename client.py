import socket

#create UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#get my ip and set port
hostname = socket.gethostname()
server_ip = socket.gethostbyname(hostname + ".local")
server_port =10001

#set buffer
buffer_size = 1024

msg="hi! I am client it works!"

#send my data
udp_socket.sendto(msg.encode(),(server_ip, server_port))
print("Send: ", msg)

#Receive response
print("wait for server...")
data, server = udp_socket.recvfrom(buffer_size)
print("received: ", data.decode())