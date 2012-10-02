'''
Created on 2012/10/02

@author: shirou
'''
def toBytes(arg):
    return arg.encode("UTF-8")

def Pass(password):
    return toBytes("PASS " + password + "\r\n")

def Nick(nickname):
    return toBytes("NICK " + nickname + "\r\n")
    
def User(nick, mode="0", realname="GDRIrc"):
    return toBytes("USER " + nick + " " + mode + " * :" + realname + "\r\n")
    
def Oper(name, password):
    return toBytes("OPER " + name + " " + password + "\r\n")
    
def Mode(target, mode):
    return toBytes("MODE" + target + " " + mode + "\r\n")
    
def Service(name, distribution , info, type=0):
    return toBytes("SERVICE " + name + " * " + distribution + " " + type + " 0 :" + info + "\r\n")
    
def Quit(message):
    return toBytes("QUIT :" + message + "\r\n")

def Squit(server, comment):
    return toBytes("SQUIT " + server + " :" + comment + "\r\n")
    
def Join(channels, keys=None):
    
    content = ""
    i = 0
    for channel in channels:
        content += channel
        if(not keys[i]):
            content = content + " " + keys[i]
        content += ","
        i+=1
    return toBytes("JOIN " + content + "\r\n")
    


