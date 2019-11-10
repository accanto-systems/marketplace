#!/bin/sh -eux
echo "wait for 30 seconds"
sleep 30

sudo apt-get update 
sudo apt-get install -y python python-yaml gcc flex bison libmysqlclient-dev git-core build-essential collectd

cd /opt
sudo tar zxf kamailio-5.0.2_src.tar.gz	
chmod -R 766 kamailio-5.0.2
cd kamailio-5.0.2
make include_modules="dispatcher acc ctl sanity xlog siputils textops maxfwd pv rr sl tmx tm kex jsonrpcs db_mysql rtpengine" cfg
make all
sudo make install

############# rtp proxy install ##############
sudo apt-get -y install debhelper iptables-dev libavcodec-dev libavfilter-dev libavformat-dev libavresample-dev libavutil-dev libcurl4-openssl-dev libevent-dev libglib2.0-dev libhiredis-dev libjson-glib-dev libpcap-dev libpcre3-dev libssl-dev libxmlrpc-core-c3-dev markdown
sudo apt-get -y install dkms keyutils kmod libb-hooks-op-check-perl libbencode-perl libcrypt-rijndael-perl libdigest-hmac-perl libexporter-tidy-perl libio-socket-inet6-perl liblocale-gettext-perl libnfsidmap2 libsocket6-perl libtext-charwidth-perl libtext-wrapi18n-perl libtirpc1 menu module-assistant nfs-common rpcbind libmysqlclient-dev unzip

cd /opt
unzip rtpengine-mr5.5.10.1.zip
cd rtpengine-mr5.5.10.1
sudo ./debian/flavors/no_ngcp
cd daemon
sudo make