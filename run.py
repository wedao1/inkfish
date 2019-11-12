#!/usr/bin/python
# -*- coding:UTF-8 -*-
import pssh
import sshconfig
class Session():
    def __init__(self,style=1,name="lo"):
        self.name="lo"
        self.style=style
        self.active=True 

    def setName(self,keyword="lo"):
        cmd=raw_input("input hostname keyword to start:")
        self.name=cmd
        print sshconfig.get_host_list(self.name);
    def run(self):
        self.setName()
        while self.active:
            cmd=raw_input()
            if(cmd == ":name"):
                self.setName()
            elif(cmd == ":q"):
                self.active=False
            elif(cmd != ""):
                pssh.cmd(self.name,cmd,self.style)
    
if __name__ == "__main__":
    s=Session()
    s.run();
