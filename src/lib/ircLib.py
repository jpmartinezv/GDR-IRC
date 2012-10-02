'''
Created on 2012/10/02

@author: shirou
'''
import threading
import re
import socket

from lib.cmds import Cmds

class Client():
    def __init__(self):
        """Return an initialized Client object"""
        self.socket = socket.socket()
        self.connected = False
        
    def connect(self, address):
        """Connects to the address specified, where address is a tuple (host, port)."""
        if not self.connected:
            self.socket.connect(address)
            self.connected = True
            self.dispatcher = self.Dispatcher(self)
            self.dispatcher.start()
        else:
            print("Already Connected")
        
    def send(self, line):
        """Sends the 'line' to the server."""
        if self.connected:
            self.socket.send(line)
        else:
            print("Not Connected")
    
    class Dispatcher(threading.Thread):
        def __init__(self, parent):
            threading.Thread.__init__(self) #temp
            self.parent = parent
            
        def run(self):
            readbuffer = ""
            while True:
                readbuffer = readbuffer + self.parent.socket.recv(1024).decode('UTF-8')
                temp = str.split(readbuffer, "\n")
                readbuffer = temp.pop()
                for line in temp:
                    line=str.rstrip(line)
                    line=str.split(line)
                    print(line)
            
                    if(line[0]=="PING"):
                        self.parent.socket.send(bytes("PONG %s\r\n" % line[1], 'UTF-8'))
