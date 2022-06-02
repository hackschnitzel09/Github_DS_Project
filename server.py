import utility

socket = utility.create_socket()
myip = utility.get_ip()

myport =10001

#set buffer
buffer_size = 1024

msg="hi! I am server, it works!"

#bind socket to port
socket.bind((myip, myport))
print("Server up and running {}:{}".format(myip, myport))

while True:
    print("\n waiting for msgs...\n")

    data, client_ip = socket.recvfrom(buffer_size)
    print("client ip: ", client_ip)
    print("msg: ", data.decode())

    if data:
        socket.sendto(str.encode(msg), client_ip)
        print("repied: ", msg)