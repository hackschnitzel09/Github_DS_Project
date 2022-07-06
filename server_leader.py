import threading
import utility
import time

#reply to new clients and servers and maintain lists
#hartbeat
#sync lists to other servers


port = 45961
leader = True

threading.Thread(target=utility.udp_listener, args=(leader,)).start()


while True:
    utility.hartbeat()
    time.sleep(5)