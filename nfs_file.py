import socket
import sys
import os
import time
import thread
 
def scan(ip_str):
    port = '2049'
    cs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    address=(str(ip_str),int(port))
    status = cs.connect_ex((address))
    if(status == 0):
        cmd = ["showmount", "-e",ip_str]
        output = os.popen(" ".join(cmd)).readlines()
        print output
    cs.close()
    
def readText(txtpath):
    libs = []
    fp = open(txtpath,'r')
    while 1:
        line = fp.readline()
        if line:
            libs.append(line.strip())
        else:
            break
    fp.close()
    return libs
     
if __name__ == "__main__":
    ip = readText(sys.argv[1:])
    for i in ip:
        scan(i)
