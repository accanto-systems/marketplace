#!/usr/bin/python

import sys

template = str(sys.argv[1])
remote_list = str(sys.argv[2])
host_ip = str(sys.argv[3])
host_port = str(sys.argv[4])

remote_list=remote_list.splitlines()

list = ""

for line in remote_list:
  if host_ip not in line:	
    list += line + "\n"
  
print(list)