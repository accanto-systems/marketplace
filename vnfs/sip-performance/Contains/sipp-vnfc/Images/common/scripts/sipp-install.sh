#!/bin/sh -eux

sleep 30

sudo apt-get update 

TZ=Etc/UTC
sudo ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#sudo apt-get update && apt-get -y install wget ntp build-essential subversion libncurses5-dev openssl libssl-dev libpcap-dev
sudo apt-get update && apt-get -y install python wget ntp build-essential  libncurses5-dev  libpcap-dev iproute2 collectd
cd /opt
tar zxvf sipp-3.5.2.tar.gz
cd sipp-3.5.2
sudo ./configure --with-pcap 
sudo make
