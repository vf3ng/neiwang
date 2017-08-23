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
        print "%s may have nfs service" %(ip_str)
        cmd = ["showmount", "-e",ip_str]
        output = os.popen(" ".join(cmd)).readlines()
        print output
    cs.close()
    
def find_ip(ip_prefix):
    for i in range(1,256):
        ip = '%s.%s'%(ip_prefix,i)
        thread.start_new_thread(scan, (ip,))
        time.sleep(0.1)
     
if __name__ == "__main__":
    commandargs = sys.argv[1:]
    args = "".join(commandargs)    
   
    ip_prefix = '.'.join(args.split('.')[:-1])
    find_ip(ip_prefix)
