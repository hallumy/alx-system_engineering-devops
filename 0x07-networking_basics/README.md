#Networking Basics

## OSI model
OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.

It is organized from the lowest level to the highest level:

The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal
The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc

## Types of Network
LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.

##MAC and IP Addresses
MAC(media access control) is a unique physical identifier of a computer
IP(Internet Protocol) is a logical address of the computer and is used to uniquely locate a computer connected via a network

##UDP and TCP
TCP is a Connection-oriented protocol while UDP is a connectionless protocol.
TCP is comparatively slower than UDP. Overall, UDP is a much faster, simpler, and efficient protocol, however, retransmission of lost data packets is only possible with TCP.

##TCP and UDP ports
Bash script that displays listening ports:

That only shows listening sockets
That shows the PID and name of the program to which each socket belongs

## HOST of the NETWORK
Bash script that pings an IP address passed as an argument.

Requirements:

Accepts a string as an argument
Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed
Ping the IP 5 times
