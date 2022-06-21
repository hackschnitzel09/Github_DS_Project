import utility

leader_ip = "192.168.1.63"

to = input("an wen? ")
msg = input("nachricht? ")
msg = "msg@" + utility.usr_ip(to) + "@" + msg + "@" + utility.get_ip()


utility.send_msg(msg, leader_ip)