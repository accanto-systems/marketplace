#!/bin/sh

set -e
set -x
export DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true

echo "tzdata tzdata/Areas select Europe" > /tmp/preseed.txt;
echo "tzdata tzdata/Zones/Europe select London" >> /tmp/preseed.txt; 
debconf-set-selections /tmp/preseed.txt 

apt-get update
apt-get install -y tzdata

apt-get install -y openssh-server sudo python supervisor vim less net-tools inetutils-ping curl
mkdir -p /var/run/sshd

/usr/bin/ssh-keygen -A

sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

useradd -m -d /home/ubuntu ubuntu -s /bin/bash
echo "ubuntu ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
echo 'ubuntu:ubuntu' | chpasswd

echo 'root:ubuntu' | chpasswd

mkdir /home/ubuntu/.ssh
chown ubuntu:ubuntu /home/ubuntu/.ssh
chmod 700 /home/ubuntu/.ssh

mv /opt/id_rsa.pub /home/ubuntu/.ssh/authorized_keys
chown ubuntu:ubuntu /home/ubuntu/.ssh/authorized_keys
chmod 0600 /home/ubuntu/.ssh/authorized_keys