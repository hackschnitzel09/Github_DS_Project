import threading
import utility
from datetime import datetime

myip = utility.get_ip()

server_list = ["192.168.0.216" ,"192.168.0.172", "192.168.0.149"]
my_id = server_list.index(myip)

print(my_id)
print(len(server_list))

msg = "my id is: " + str(my_id) + " " + str(datetime.now()) 
port = 45961

if len(server_list) == my_id + 1:
    neighbour = server_list[1]
else:
    neighbour = server_list[my_id + 1]
print("my neighbour is: ", neighbour)

utility.send_msg(msg, neighbour, port)