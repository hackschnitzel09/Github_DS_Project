import threading
import utility

port = 45961
leader = False

print(utility.get_ip())
utility.udp_listener(leader)

#threading.Thread(target=utility.udp_listener(leader)).start()
#threading.Thread(target=utility.send_msg("skrv", "192.168.1.63")).start()