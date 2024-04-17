#!/usr/bin/env python
import sys, time, netifaces
from socket import *

MYPORT = 666
INTERFACE_NAME = 'ens192'  # The name of the interface

# Get the IP address of the interface
ip = netifaces.ifaddresses(INTERFACE_NAME)[netifaces.AF_INET][0]['addr']

s = socket(AF_INET, SOCK_DGRAM)
s.bind((ip, 0))  # Bind to the interface IP
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while 1:
    data = repr(time.time()) + '\n'
    s.sendto(data.encode(), ('<broadcast>', MYPORT))  # Encode data to bytes
    time.sleep(2)