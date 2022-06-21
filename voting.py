import threading
import utility
import json
from datetime import datetime


#utility.neighbour()


msg = "voting@" + str(utility.neighbour()) + "@"  +"msg@" + utility.server_name(utility.get_ip())
utility.send_msg(msg, (utility.server_ip(str(utility.neighbour()))))

#utility.send_msg(msg, utility.server_ip(utility.neighbour()))


#check if neigbour responts to my id send if not delete him of the list and send to next

# msg = "my id is: " + str(my_id) + " " + str(datetime.now()) 
# port = 45961

# utility.send_msg(msg, neighbour, port)