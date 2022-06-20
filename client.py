import utility

leader_ip = "192.168.1.63"

print(utility.usr_name(leader_ip))

to = input("an wen? ")
msg = input("nachricht? ")

msg = utility.usr_ip(to) + "@" + msg + "@" + utility.get_ip()


utility.send_msg(msg, leader_ip)