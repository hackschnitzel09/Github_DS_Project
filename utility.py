import json
from operator import truediv
import socket
#todo
#neighbor what if there is no +1 id
port = 45961

server_list = open('servers.json','r')

# with open('servers.json') as json_file:
#     servers = json.load(json_file)
#     print(json.dumps(servers, indent=4))

# with open("servers.json", "w") as write_file:
#     json.dump(data, write_file)



#create udp socket
def create_socket():
    udp_socket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return(udp_socket)

def get_broadcast_ip():
    ip = get_ip()
    broadcast_ip = ip[:-3] + "255"
    return(broadcast_ip)

#get my ip 
def get_ip():
    hostname = socket.gethostname()
    myip = socket.gethostbyname(hostname + ".local")
    return(myip)

#listen for msg on udp
def udp_listener(leader):
    s = create_socket()
    myip = get_ip()
    # Set the socket to broadcast and enable reusing addresses
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind socket to address and port
    s.bind((get_ip(), port))
    print("Listening to broadcast messages")
    while True:
        data, addr = s.recvfrom(1024)
        if data:
            print("Message:", data.decode())
            #check if Iam leader
            msg_split(data.decode(), leader)

#Split mgs into receiver and msg and forward it to receiver
def msg_split(rec_msg, leader):
    msg_obj = rec_msg.split("@")
    kind= msg_obj[0]
    to = msg_obj[1]
    msg = msg_obj[2]
    sender = msg_obj[3]
    #print("send to: " + to)
    print("msg: " + msg)
    print("from: " + sender)
    

    if kind == "voting":
        msg = "voting@" + str(neighbor()) + "@" + "@" + get_ip()   
        send_msg(msg, server_ip(str(neighbor())))
    
    if leader == True:    
        if kind == "msg":
            msg = "msg@" + to + "@" + msg + "@" + usr_name(sender)
            print(msg)
            send_msg(msg, to)

    
#find neighbor
def neighbor():
    myip = get_ip()

    with open("servers.json","r") as servers:
        server_list = json.load(servers)

    my_id = server_name(myip)
    print(my_id)
    print(len(server_list))

    if len(server_list) == int(my_id):
        neighbor = 1
    else:
        neighbor = int(my_id) + 1
    print("my neighbor is: ", neighbor) 
    return(neighbor)


#Send UDP msg
def send_msg(msg, rec_ip):
    s = create_socket()
    s.sendto(msg.encode(),(rec_ip, port))
    print("msg send to: " + rec_ip)

#Send UDP msg with Port
def send_msgp(msg, rec_ip, port):
    s = create_socket()
    s.sendto(msg.encode(),(rec_ip, port))
    print("msg send to: " + rec_ip)

#send broadcast
def send_broadcast(msg):
    s = create_socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(str.encode(msg), (get_broadcast_ip(), port))
    print("broadcast msg send")

#get ip of user by name
def usr_ip(name):
    with open("users.json","r") as users:
        user_list = json.load(users)
    usr_ip = user_list[name]
    print("User ip is: " + usr_ip)
    return(usr_ip)

#get name by ip
def usr_name(ip):
    with open("users.json","r") as users:
        user_list = json.load(users)
    names = list(user_list.keys())
    ips = list(user_list.values())
    return(names[ips.index(ip)])

#get server by ip
def server_name(ip):
    with open("servers.json","r") as servers:
        server_list = json.load(servers)
    ids = list(server_list.keys())
    ips = list(server_list.values())
    return(ids[ips.index(ip)])

#get ip of server by name
def server_ip(id):
    with open("servers.json","r") as server:
        server_list = json.load(server)
    server_ip = server_list[id]
    print("server ip is: " + server_ip)
    return(server_ip)

#hartbeat
def hartbeat():
    with open("servers.json","r") as servers:
        server_list = json.load(servers)
    i = 1
    while i <= len(server_list):
        send_msgp("hartbeat@to@msg@sender", str(server_list[str(i)]), "45962")
        i += 1
    print("Hartbeat send")