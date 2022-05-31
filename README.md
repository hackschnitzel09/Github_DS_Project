DBE - Distributed Systems 

Project Proposal 

Group 07: Kevin Ross, Simon Haupt, Zacharias Sitter 

Introduction 

We propose the design and implementation of a chat application using central and advanced principles of distributed systems development. The application should allow users to communicate via text messages. It should also be possible to communicate in group chats. The idea is that the users register themselves. The main server transmits the registered users as active. Afterwards the communication runs over the main server, which receives the messages and transmits them to the addressee. For the protection of the data further backup servers are installed, which get their information over the main server. 

 

 

Project requirements analysis: 
Dynamic discovery 
- Client registers itself by sending username to server 
- Server receives various incoming client’s requests  
- It stores the information of the clients Ip address and name in a list 
- This List is broadcasted to all the users 
- Whenever a client logs out, it deletes that particular client entry from its list and updates it accordingly 
- It also keeps track of various chat rooms, providing a group Ip to each multicast group 

Crash-Fault-Tolerance:
- The failure of a participant must not cause a crash of the entire system. 
- In the failure case a new leader election should be triggered 
- Heartbeat messages sent by the leader as a failure detector when a participant crash 
- Backup server which replicates the data 
- Vector clock to ensure synchronized time 
- Concurrency and transparency 

Voting:
- Based on the LCR (LeLann-Chang-Roberts) Algorithms 
- Every server must have a unique ID 
- If the leader server goes down a new leader will be elected 
- Clients can trigger election if the server does not respond  
- After trigger neighbor will be searched and pinged 
- Voting message will go around until a server get its UID back 
- After election leader announces itself as a leader 

Architecture design:
Fig. 1. Architecture design draft. 

Implementation overview: 
We plan to write the whole project in Python 3 programming language. For the remotely collaborative work we will create a public repository in GitHub. Through this opportunity, each group member can contribute on their own project topic as they prefer, and we will have a version documentation. Therefore, any programming environment can be used. Until now, PyCharm and Visual Studio are used and connected to GitHub. 
