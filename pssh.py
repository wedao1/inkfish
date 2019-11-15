# -*- coding:UTF-8 -*-
import threading
import paramiko
import sshconfig

class paramikoThreading(threading.Thread):
    def __init__(self,command,name,host,username,password,port=22,style=1):
        super(paramikoThreading,self).__init__()
        self.command = command
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.name = name
        self.style=style 
    def run(self):
        ssh = paramiko.SSHClient()
        # 创建一个ssh的白名单
        know_host = paramiko.AutoAddPolicy()
        # 加载创建的白名单
        ssh.set_missing_host_key_policy(know_host)
 
        # 连接服务器
        if(self.password==""):
        #    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.load_system_host_keys()
            ssh.connect(hostname=self.host, port=self.port, username=self.username, pkey=sshconfig.get_private_key())
        else:
            ssh.connect(hostname=self.host,port=self.port,username=self.username,password=self.password)
        stdin, stdout, stderr = ssh.exec_command(self.command)
        if(self.style==1): 
            print("[%s@%s]# %s\n%s"%(self.name,self.host,self.command,stdout.read().decode()))
        elif(self.style==2):
            print("[%s@%s]:\n%s"%(self.name,self.host,stdout.read().decode()))
    
        ssh.close()

def cmd(find,str,style=1):
    pool={}
    t_pool = []
    pool = sshconfig.get_config(find); 
    if(style==2):
        print(">>>\n%s"%(str))    
    for onehost in pool:
        t = paramikoThreading(
            name=onehost,
            host=pool[onehost].get("hostname","localhost"),
            username=pool[onehost].get("username","root"),
            port=pool[onehost].get("port","22"),
            password=pool[onehost].get("password",""),
            command=str,
            style=style
            )
        t_pool.append(t)
    for t in t_pool:
        t.start()
    for t in t_pool:
        t.join()

if __name__ == '__main__':
    cmd('lo','uptime') 
