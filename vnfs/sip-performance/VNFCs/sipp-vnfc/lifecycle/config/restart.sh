#!/bin/bash
pkill collectd
pkill sipp
rm /opt/*.csv
nohup /opt/sipp-3.5.1/sipp -bg -sf /opt/myuac.xml -trace_stat -fd 3 -d 5000 -i $1 -s 1001 $2 -max_retrans 1 -recv_timeout 5000 -send_timeout 2000 -l $3 -mp 5606 </dev/null >/dev/null 2>&1 & 
sleep 1
nohup collectd -C /etc/collectd/collectd.conf < /dev/null > /dev/null 2>&1
sleep 1