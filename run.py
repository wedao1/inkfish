# -*- coding:UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import pssh
import sshconfig
from tag import Tag

class Session():
    def __init__(self,style=2,name="lo"):
        self.name="lo"
        self.style=style
        self.active=True 

    def setName(self,keyword="lo"):
        cmd=raw_input("search keyword of hostnames to start:")
        self.name=cmd
        print(sshconfig.get_host_list(self.name))
    def setStyle(self):
        cmd=int(raw_input("set style 1 or 2 #"))
        self.style=cmd
        print("set style = "+str(cmd))
    def scmd(self,cmd):
        pssh.cmd(self.name,cmd,self.style)
    def run(self):
        self.setName()
        while self.active:
            cmd=raw_input("#")
            if(cmd == ":name"):
                self.setName()
            elif(cmd == ":tag"):
                t=Tag()
                self.scmd(t.menu())
            elif(cmd == ":style"):
                self.setStyle()
            elif(cmd == ":q"):
                self.active=False
            elif(cmd != ""):
                self.scmd(cmd)
    
if __name__ == "__main__":
    s=Session()
    s.run();
