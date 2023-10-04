#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())

print(f"your IP: {ip}")
print("="*30)
s.bind((ip,5000))
s.listen(5)
while True:
    client, address = s.accept()#waiting
    rodata = client.recv(1024)
    print(f"{address} is sending to you this message {rodata.decode('UTF-8')}")
    print("="*30)
    msg = str(input("[Server]Please enter the message you want to send: "))
    msg_encoded = msg.encode('UTF-8')
    client.send(msg_encoded)
    client.close()
   