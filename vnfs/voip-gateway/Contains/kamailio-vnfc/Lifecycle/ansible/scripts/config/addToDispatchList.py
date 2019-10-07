#!/usr/bin/python

import sys

template = str(sys.argv[1])
remote_list = str(sys.argv[2])
host_ip = str(sys.argv[3])
host_port = str(sys.argv[4])

remote_list=remote_list.splitlines()

list = ""
found = False
for line in remote_list:
  if host_ip in line:
    found = True  
  list += line + "\n"
  
if not found:  
  list += "1 sip:" + host_ip + ":" + host_port + "\n"
  
print(list)

