#!/usr/bin/python
import json
import sys
j = json.loads(sys.argv[1])
print j[0]['NetworkSettings']['Networks'][sys.argv[2]]['IPAddress']