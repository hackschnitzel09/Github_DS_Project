import socket

#get my ip
hostname = socket.gethostname()
myip = socket.gethostbyname(hostname + ".local")

broadcast_msg = myip + " online"
broadcast_ip = "192.168.1.255"
broadcast_port = 5961


#create socket
broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
broadcast_socket.sendto(str.encode(broadcast_msg), (broadcast_ip, broadcast_port))
print("broadcast msg send")

