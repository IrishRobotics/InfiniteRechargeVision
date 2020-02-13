import numpy as np
import cv2
import math
import socket
import pickle
import sys
import struct
from matplotlib import pyplot as plt 

def recvall(sock, n):
    data = b''
    while len(data) < n:
        packet = sock.recv(n- len(data))
        if not packet:
            return None
        data += packet
    return data

print('RoboRiosimulator')

Host = '10.9.30.176' # CHANGE THIS to roboRio Network Ip address
Port = 60378

recvSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket setup')

recvSocket.bind((Host, Port))
print('socket bound')

recvSocket.listen(1)
print("socket listeb")

conn, addr = recvSocket.accept()
print(f'Connectipon address: {addr}')

while True:
    data = conn.recv(4) # buffer size is 1024 bytes
    #print (f'received message:, {data}')
    if data: 
        message = struct.unpack('!i', data)
        messageId = message[0]
        #print(f'{messageId}')
        
        if messageId == 1:           
            data = conn.recv(26)
            messageType1 = struct.unpack('!dhhhi', data) 
            
            targetAngle = messageType1[0]
            #targetDistance = messageType1[1]
            timeHour = messageType1[1]
            timeMinute = messageType1[2]
            timeSecond = messageType1[3]
            timeMicroSecond = messageType1[4]




            print(f'got vision target found {targetAngle} {timeHour}:{timeMinute}:{timeSecond}.{timeMicroSecond}')

        elif messageId == 2:
            print('got no vision target found')