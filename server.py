from http.client import OK
from socket import socket
import threading
import utility
import socket
import time


#send ip to leader check for id  wait for server reply if no reöy trigger voting
#check leader heartbeat else trigger voting
#update lists according to leader info
#(recive client msgs and forward them based on the name) check if the name was already in use and if the client to the name is available
#litener on other port for heartbeat
port = 45961
leader = False
global heart
heart = False



#heartbeat receiver
def heartbeat_rec():
    s = utility.create_socket()
    # Set the socket to broadcast and enable reusing addresses
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind socket to address and port
    s.bind((utility.get_ip(), int("45962")))
    print("Listening to heartbeat messages") 
    while True:
        data, addr = s.recvfrom(1024)
        if data:
            print("Message:", data.decode())
            if data.decode() == "heartbeat@to@msg@sender":
                print("passt")
                global heart
                heart = True

def heartbeat_reset():
    global heart
    while True:
        time.sleep (5)
        if heart == False:
            print("no heartbeat")
            utility.voting()
        if heart == True:
            heart = False
            
            

threading.Thread(target=heartbeat_rec).start()
threading.Thread(target=heartbeat_reset).start()
threading.Thread(target=utility.udp_listener, args=(leader,)).start()

print(utility.get_ip())


#threading.Thread(target=utility.udp_listene