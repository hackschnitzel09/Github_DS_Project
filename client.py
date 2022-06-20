import utility

leader_ip = "192.168.1.63"

to = input("an wen? ")
msg = input("nachricht? ")

msg = utility.usr_ip(to) + "@" + msg
print(msg)
# if to == "1":
#     ip = "192.168.0.172"

# elif to == "2":
#     ip = "192.168.0.216"

# elif to == "3":
#     ip = "192.168.0.249"

# elif to == "4":
#     ip = "192.168.1.63"

# elif to == "5":
#     ip = "192.168.1.160"

# elif to == "6":
#     ip = "192.168.1.167"

# else:
#     ip = "192.168.1.255"

utility.send_msg(msg, leader_ip)
#utility.send_broadcast(msg)