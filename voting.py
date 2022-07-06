import threading
import utility
import json
from datetime import datetime


#if voted set leader variable in server.py
#pin neigbour bevor send

#utility.neighbor()


msg = "voting@" + str(utility.neighbor()) + "@"  +"msg@" + utility.server_name(utility.get_ip())
utility.send_msg(msg, (utility.server_ip(str(utility.neighbor()))))

#utility.send_msg(msg, utility.server_ip(utility.neighbor()))


#check if neigbour responts to my id send if not delete him of the list and send to next

# msg = "my id is: " + str(my_id) + " " + str(datetime.now()) 
# port = 45961

# utility.send_msg(msg, neighbor, port)