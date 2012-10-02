'''
Created on 2012/10/02

@author: shirou
'''

from lib.ircConnection import Client

def main():
    HOST="irc.rizon.net"
    PORT=6667
    NICK="gdrb"
    IDENT="gdrirc"
    REALNAME="GDR_IRC"
    readbuffer=""
    print("aaaa")
    client = Client()
    client.connect((HOST, PORT))
    client.send(("NICK %s\r\n" % NICK).encode('utf-8'))
    client.send(("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME)).encode('utf-8'))
    client.send(("JOIN #hihouki\r\n").encode('utf-8'))
    
    while True:
        line = input()
        client.send((line+"\r\n").encode('utf-8'))
            
if __name__ == '__main__':
    main()