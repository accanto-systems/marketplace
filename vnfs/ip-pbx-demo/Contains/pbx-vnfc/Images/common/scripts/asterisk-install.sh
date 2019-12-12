#!/bin/sh -eux
sleep 30

sudo apt-get update 
sudo apt-get upgrade -y
sudo apt-get -y install python wget ntp build-essential subversion libncurses5-dev libssl-dev libxml2-dev vim-nox autoconf ncurses-dev doxygen texinfo libcurl4-openssl-dev libsnmp-dev uuid-dev sqlite libsqlite3-dev git libspeex-dev libgsm1-dev libspeex-dev libxml2-dev libjansson-dev libsrtp-dev libsnmp-dev snmp snmpd snmp-mibs-downloader collectd

cd /opt
sudo tar zxf asterisk-14.7.8.tar.gz
	
sudo chmod -R 777 asterisk-14.7.8
cd asterisk-14.7.8
./configure 
make
sudo make install
sudo make samples

#sudo echo "agentAddress udp:161,udp6:[::1]:161\ncreateUser asteriskUser MD5 password DES\nrwuser asteriskUser priv" >> /etc/snmp/snmpd.conf
#sudo echo 'master agentx\nagentXSocket /var/agentx/master\nagentXPerms 0660 0550 nobody asterisk' >> /etc/snmp/snmpd.conf

#sudo echo "enabled = yes" >> /etc/asterisk/res_snmp.conf

