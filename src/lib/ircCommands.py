'''
Created on 2012/10/02

@author: shirou
'''
from lib.ircConnection import *

def User(nick, mode="0", realname="GDRIrc"):
    send("USER "+nick+" "+mode+" * "+realname+"\r\n")
