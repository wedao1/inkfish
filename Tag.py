# -*- coding:UTF-8 -*-
import os
import sys

class Tag():
    def __init__(self,path="./tags/"):
        self.path = path
        self.tags=[]
        self.load()
    def load(self):
        self.tags=os.listdir(self.path)
    #def add(name,text):
    #def del(name):    
    def list(self):
        self.load()
        return self.tags
    def get(self,tag):
        file=self.path+tag
        content=""
        with open(file, 'r') as f:
	    content = f.read()
        return content
        
    def menu(self):
        for i in range(0, len(self.tags)):
            print(""+str(i)+"."+self.tags[i]+"\n")
        i=int(input("input tag number:"))
        return self.get(self.tags[i])
        
if __name__ == '__main__':
    t=Tag()
    l=t.list()
    print(l)
    print(t.get(l[0]))
    print(t.menu())
