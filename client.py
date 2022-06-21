import utility

leader_ip = "192.168.1.63"

#ask name send together with ip to leader check if name is already taken if no add to list else new entry wait for servy reply if no reöy trigger voting
# ability to send and receive 

to = input("an wen? ")
msg = input("nachricht? ")
msg = "msg@" + utility.usr_ip(to) + "@" + msg + "@" + utility.get_ip()


utility.send_msg(msg, leader_ip)



