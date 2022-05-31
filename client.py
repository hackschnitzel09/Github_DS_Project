import socket

#create UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#set buffer
buffer_size = 1024


#get my ip
hostname = socket.gethostname()
myip = socket.gethostbyname(hostname)

broadcast_msg = myip + "online"
broadcast_ip = "192.168.56.255"
broadcast_port = 5961

def client(server_ip, server_port):
    #get my ip and set port
    hostname = socket.gethostname()
    server_ip = "xxx.xxx.xxx.xxx"
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

#broadcast sender
def broadcast_send(broadcast_msg, broadcast_ip, proadcast_port):
    #create socket
    broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    broadcast_socket.sendto(str.encode(broadcast_msg), (broadcast_ip, broadcast_port))
    print("broadcast msg send")

broadcast_send(broadcast_msg, broadcast_ip, broadcast_port)