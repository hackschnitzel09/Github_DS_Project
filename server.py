import threading
import utility

#send ip to leader check for id  wait for server reply if no reöy trigger voting
#check leader hartbeat else trigger voting
#update lists according to leader info
#(recive client msgs and forward them based on the name) check if the name was already in use and if the client to the name is available

port = 45961
leader = False

print(utility.get_ip())
utility.udp_listener(leader)

#threading.Thread(target=utility.udp_listener(leader)).start()
#threading.Thread(target=utility.send_msg("skrv", "192.168.1.63")).start()