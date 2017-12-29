#!/usr/bin/env python
#coding:utf-8
from multiprocessing.dummy import Pool as ThreadPool
from sys import argv
import socket
import redis

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

def redisCheck(ip):
	try:
		r = redis.Redis(host=ip,port=6379,db=0,socket_timeout=120)
		return {ip:r.ping()}
	except:
		return {ip:False}

if __name__ == '__main__':
	socket.setdefaulttimeout(10)
	filepath,threed_num = argv[1:]
	ips = readText(filepath)
	pool = ThreadPool(int(threed_num))
	results = pool.map(redisCheck,ips)
	pool.close()
	pool.join()
	result = {}
	for x in results:
		result = dict(result,**x)
	fp = open('redisOut.txt','w')
	for i in result:
		fp.write(i + '	' + str(result[i]) + '\n')
	fp.close
