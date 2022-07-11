import utility

leader_ip = "192.168.1.100"

#ask name send together with ip to leader check if name is already taken if no add to list else new entry wait for servy reply if no reöy trigger voting
# ability to send and receive

to = input("an wen? ")
kind = input("was für eine nachricht?(msg/newu/news) ")
if kind == "newu":
    name = input("name? ")
    msg = kind + "@" + utility.usr_ip(to) + "@" + name + "@" + utility.get_ip()
else:
    msg = input("nachricht? ")



utility.send_msg(msg, leader_ip)



