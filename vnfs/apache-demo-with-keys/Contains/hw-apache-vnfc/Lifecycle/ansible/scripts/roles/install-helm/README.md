# Ansible Role - Install Helm on ALD

Role to install and configure the Helm client on the Ansible Lifecycle Driver (ALD). This role uses `delegate_to: localhost` to install and configure the Helm client on the Ansible Lifecycle Driver, so that resource package Ansible scripts can execute Helm commands against VNFcs.

Note: this role will not be very robust when used by multiple scripts trying to install Helm (there are likely to be race conditions when installing Helm on ALD in this case); as such, it shouldn't be used in production.