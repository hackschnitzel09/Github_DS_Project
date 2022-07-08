import threading
import utility
import time

#reply to new clients and servers and maintain lists
#heartbeat
#sync lists to other servers


port = 45961
leader = True

threading.Thread(target=utility.udp_listener, args=(leader,)).start()


while True:
    utility.heartbeat()
    time.sleep(5)