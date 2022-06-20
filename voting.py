import threading
import utility
import json
from datetime import datetime

myip = utility.get_ip()

with open("servers.json","r") as servers:
    server_list = json.load(servers)


print(server_list["s1"])

#my_id = server_list.index(myip)

#print(my_id)
# print(len(server_list))

# msg = "my id is: " + str(my_id) + " " + str(datetime.now()) 
# port = 45961

# if len(server_list) == my_id + 1:
#     neighbour = server_list[1]
# else:
#     neighbour = server_list[my_id + 1]
# print("my neighbour is: ", neighbour)

# utility.send_msg(msg, neighbour, port)