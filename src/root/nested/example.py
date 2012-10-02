'''
Created on 2012/10/02

@author: shirou
'''

import socket

def main():
    HOST="irc.rizon.net"
    PORT=6667
    NICK="gdrb"
    IDENT="gdrirc"
    REALNAME="GDR_IRC"
    readbuffer=""
    s=socket.socket( )
    s.connect((HOST, PORT))
    s.send(("NICK %s\r\n" % NICK).encode('UTF-8'))
    s.send(bytes("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME), 'UTF-8'))
    s.send("JOIN #hihouki".encode('utf_8'))
    
    while 1:
        readbuffer=readbuffer+s.recv(1024).decode('UTF-8')
        temp=str.split(readbuffer, "\n")
        readbuffer=temp.pop( )
        print(temp)
    
        for line in temp:
            line=str.rstrip(line)
            line=str.split(line)
    
            if(line[0]=="PING"):
                s.send(bytes("PONG %s\r\n" % line[1], 'UTF-8'))
            
if __name__ == '__main__':
    main()