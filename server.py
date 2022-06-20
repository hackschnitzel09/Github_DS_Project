import socket
import threading
import utility

port = 45961


threading.Thread(target=utility.udp_listener).start()
threading.Thread(target=utility.send_msg("skrv", "192.168.1.63")).start()