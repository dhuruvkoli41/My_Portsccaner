#!/bin/python3

import sys
import socket#for nade to node connection
from datetime import datetime # for time prints 
#define our target

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
	print("Invalid amount of argument,")
	print("Syntex: python3 scanner.py <ip>")
	sys.exit()
# add a pretty banner 
print("-" * 50)
print("scanning target "+ target)
print("Time started:"+str(datetime.now()))
print("-" * 50)

try:
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #if the connection not established so it stops in 1 sec 
		result = s.connect_ex((target,port)) #returns an error indicator 
	#	print("Checking port {}",format(port))
		if result == 0:
			print("port (" + format(port) + ") is open")
		s.close()	
		
except KeyboardInterrupt:
	print("\nExisting program.") 
	sys.exit()# for clean exit 	
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()# for clean exit
	
except socket.error:
	print("Couldn't connect to server.")
	sys.exit()#for clean exit 
	
		
			
		
		