#!/usr/bin/python
import sys
import re
address = sys.argv[1]
if len(sys.argv) >= 2:
  index = sys.argv[2]
  if index == "${instance.index}":
    index = 1
  results = re.search('(.*\.)(.+?)$', address)
  stub = results.group(1)
  range = results.group(2)
  next = int(range) + int(index)
  out_address = stub + str(next)
  print out_address
else:
  print address