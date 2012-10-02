'''
Created on 2012/10/02

@author: shirou
'''

def toBytes(arg):
        return arg.encode("UTF-8")

def auto_comas(channels, keys=None):
    content = ""
    n = len(channels)
    for i in range(0, n - 1):
        content += (channels[i] + ",")
    content += channels[n - 1]
    if(not keys is None):
        content += " "
        for i in range(0, n - 1):
            content += keys[i] + ","
        content += keys[n - 1]
    return content

class Cmds:
    
    def Pass(self, password):
        return toBytes("PASS " + password + "\r\n")
    
    def Nick(self, nickname):
        return toBytes("NICK " + nickname + "\r\n")
        
    def User(self, nick, mode="0", realname="GDRIrc"):
        return toBytes("USER " + nick + " " + mode + " * :" + realname + "\r\n")
        
    def Oper(self, name, password):
        return toBytes("OPER " + name + " " + password + "\r\n")
        
    def Mode(self, target, mode):
        return toBytes("MODE" + target + " " + mode + "\r\n")
        
    def Service(self, name, distribution , info, type=0):
        return toBytes("SERVICE " + name + " * " + distribution + " " + type + " 0 :" + info + "\r\n")
        
    def Quit(self, message):
        return toBytes("QUIT :" + message + "\r\n")
    
    def Squit(self, server, comment):
        return toBytes("SQUIT " + server + " :" + comment + "\r\n")
        
    def Join(self, channels, keys=None):
        content = auto_comas(channels, keys)
        return toBytes("JOIN " + content + "\r\n")
    
    def Part(self, channels, message=None):
        if(message is None):
            content = auto_comas(channels)
        else:
            content = auto_comas(channels) + " :" + message
        return toBytes("PART" + content + "\r\n")
    
    def Topic(self, channel, topic=None):
        if(topic is None):
            content = channel
        else:
            content = channel + " :" + topic
        return toBytes("PART" + content + "\r\n")
            
            
    
    
