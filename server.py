import socket

#create udp socket
udp_socket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#set buffer
buffer_size = 1024

#get my ip and set port
hostname = socket.gethostname()
myip = socket.gethostbyname(hostname)
print("my ip is: ", myip)
myport =10001

#brodcast listerner
broadcast_port = 5961

def brodcast_listener(broadcast_port, myip):
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





def server(hostname, myip, myport):


    msg="hi! I am server, it works!"

    #bind socket to port
    udp_socket.bind((myip, myport))
    print("Server up and running {}:{}".format(myip, myport))

    while True:
        print("\n waiting for msgs...\n")

        data, client_ip = udp_socket.recvfrom(buffer_size)
        print("client ip: ", client_ip)
        print("msg: ", data.decode())

        if data:
            udp_socket.sendto(str.encode(msg), client_ip)
            print("repied: ", msg)


brodcast_listener(broadcast_port, myip)