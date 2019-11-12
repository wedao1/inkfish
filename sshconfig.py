
# _*_ coding: utf-8 _*_
import os 
import pandas as pd
import paramiko,re 

SSH_CONF="~/.ssh/config"
SSH_CONF_KEY="~/.ssh/id_rsa"

def get_config(find):
    if not os.path.isfile(os.path.expanduser(SSH_CONF)):
        return {}
    with open(os.path.expanduser(SSH_CONF)) as f:
        cfg = paramiko.SSHConfig()
        cfg.parse(f)
        ret_dict = {}
        hostnames = cfg.get_hostnames()
        for hostname in hostnames:
            if(find not in hostname):
                continue 
            if ('?' in hostname) or ('*' in hostname):
                continue
            options = cfg.lookup(hostname)
            # We want the ssh config to point to the real hostname, but we dont want to
            # set ansible_ssh_host to the real name, but the ssh_config alias
            ret_dict[hostname] = options
        return ret_dict

def get_private_key():
    private_key = paramiko.RSAKey.from_private_key_file(os.path.expanduser(SSH_CONF_KEY))
    return private_key

def get_ssh_key_for_host(host):
    ssh_config = paramiko.SSHConfig()
    user_config_file = os.path.expanduser("~/.ssh/config")
    if os.path.exists(user_config_file):
        with open(user_config_file) as f:
            ssh_config.parse(f)
    
    user_config = ssh_config.lookup(host)

    if 'identityfile' in user_config:
        path = os.path.expanduser(user_config['identityfile'][0])
        if not os.path.exists(path):
            raise Exception("Specified IdentityFile "+path+ " for " + host + " in ~/.ssh/config not existing anymore.")

        return path
 
# 获取文件的内容
def get_contends(path):
    with open(path) as file_object:
        contends = file_object.read()
    return contends
 
 
# 将一行内容变成数组
def get_contends_arr(contends):
    contends_arr_new = []
    contends_arr = str(contends).split(']')
    for i in range(len(contends_arr)):
        if (contends_arr[i].__contains__('[')):
            index = contends_arr[i].rfind('[')
            temp_str = contends_arr[i][index + 1:]
            if temp_str.__contains__('"'):
                contends_arr_new.append(temp_str.replace('"', ''))
            # print(index)
        # print(contends_arr[i])
    return contends_arr_new
 
def get_host_list(find):
    a=get_config(find)
    s=[]
    for k in a:
        s.append(k+"@"+a[k].get("hostname"))
    return ",".join(s)
 
if __name__ == '__main__':
    print get_host_list("lo")
