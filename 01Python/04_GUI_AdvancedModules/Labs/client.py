#!/usr/bin/python3

import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
client.connect((ip,5000))
print("="*30)
while True:
    msg = str(input("[Client] Please enter the message you want to send: "))
    msg_encoded = msg.encode('UTF-8')
    client.send(msg_encoded)
    print("="*30)
    
    rodata = client.recv(1024)
    print(f"{ip}: is sending you this message {rodata.decode('UTF-8')}")
    client.close()

