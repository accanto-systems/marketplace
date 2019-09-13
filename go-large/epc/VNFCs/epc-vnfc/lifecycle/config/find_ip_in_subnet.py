#!/usr/bin/env python

import ipaddress
import sys

subnet = sys.argv[1]
# are gets a string "['1.1.1.1', '2.2.2.2']", could not find a way to read that directly into a list 
# looks like command line args are always strings, so have to strip & split to get list.
# must be a cleaner way, but couldn't find anything better.
address_list= sys.argv[2].strip('[]').split(',')
match = ""


if subnet != '':
  for elem in address_list:
    addr = elem.strip().strip('\'')
    if ipaddress.ip_address(addr) in ipaddress.ip_network(subnet):
      match = addr
      break

print(match)	
