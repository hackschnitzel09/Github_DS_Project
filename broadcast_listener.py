import socket

#get my ip and set port
hostname = socket.gethostname()
myip = socket.gethostbyname(hostname + ".local")
print("my ip is: ", myip)

#brodcast listerner
broadcast_port = 5961

# Create a UDP socket
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Set the socket to broadcast and enable reusing addresses
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind socket to address and port
listen_socket.bind((myip, broadcast_port))
print("Listening to broadcast messages")
while True:
    data, addr = listen_socket.recvfrom(1024)
    if data:
        print("Received broadcast message:", data.decode())
