# -*- coding:UTF-8 -*-
import paramiko
 
#创建一个ssh的客户端
ssh = paramiko.SSHClient()
#创建一个ssh的白名单
know_host = paramiko.AutoAddPolicy()
#加载创建的白名单
ssh.set_missing_host_key_policy(know_host)
#连接服务器
ssh.connect(
    hostname = "10.10.21.177",
    port = 22,
    username = "root",
    password = "12345"
)
 
shell = ssh.invoke_shell()
shell.settimeout(1)
 
command = input(">>>"+"\n")
shell.send(command)
while True:
    try:
        recv = shell.recv(512).decode()
        if recv:
            print(recv)
        else:
            continue
    except:
        command = input(">>>") + "\n"
        shell.send(command)
ssh.close() #关闭连接

