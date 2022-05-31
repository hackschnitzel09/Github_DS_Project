import socket

#create udp socket
udp_socket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#get my ip and set port
hostname = socket.gethostname()
myip = socket.gethostbyname(hostname + ".local")
myport =10001

#set buffer
buffer_size = 1024

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