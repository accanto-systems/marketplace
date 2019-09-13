# NFVI Demo Setup

## Setup LM

Clone lm-allinone project and add LM distribution to **lm-allnone/lm-artifacts** directory.

Update the following properties in **lm-allinone/ansible/ansible-variables.yml** file to point to LM software

```
lm_charts_package: ../lm-artifacts/lm-helm-charts-2.0.3-208-dist.tgz
lm_docker_package: ../lm-artifacts/lm-docker-source-2.0.3-208-dist.tgz
```

### Set the RM polling timer to 5 secs

Add the fillowing daytona block to the **lmConfigImport** section of the anible/lm-helm-values.yml file

```
configurator:
  lmConfigImport:
    ...
    daytona:
      alm.daytona.resource-manager.polling-interval: 5000
```

### Theme LM if you need

Add your theme tar file to **lm-allinone/ansible** directory and update the following properties in your **lm-allinone/ansible/ansible-variables.yml** file.

```
lm_theme: True
lm_theme_directory: .
lm_theme_name: bluerinse
```

### Add underlay interface to AIO VM

Add the following to your **lm-allinone/Vagrantfile** as the last vNIC in the list. 

```
    nodeconfig.vm.network 'public_network', dev: 's1', type: 'bridge', mode: 'bridge', :ovs => true, ip: '10.0.30.5'
```

### Run the AIO installation

```
vagrant up
```

### Set the mgmt interface on the LM VIM

LM mgmt interface is on VLAN with id 5. Add VM vNIC VLAN subinterface by doing the following

```
cd lm-allinone
vagrant ssh
ifconfig eth3
ip link add link eth3 name eth3.5 type vlan id 5
ifconfig eth3.5 10.0.30.5
```
## Setup virtual data centre and VIMs

Create the virtual infrastructure and VIMs by cloning the NFVI underlay projects

```
git clone underlay
```

Run the following commands to install everything

```
cd underlay
ansible-playbook -i inventory underlay.yaml
vagrant up
ansible-playbook -i inventory overlay.yaml
```

### Openstack images

Load the following Openstack images
* sipp
* ippbx
* kamailio

### Create openstack keypair

Create an openstack keypair called **default** 

## Configure locations in LM

### Add openstack Core location

In ALM add a location called "core" with the type "Openstack" and provide the following properties

```
os_auth_url: "http://192.168.10.10:5000/v3"
os_projectname: admin
os_username: admin
os_password: password
almip: 10.0.30.5
```

### Add k8s edge location

In ALM add a location called "edge" with the type "Kubernetes" and provide the following properties

```
k8s_address: 192.168.10.20
k8s_ssh_user: vagrant
k8s_ssh_password: vagrant 
almip: 10.0.30.5
```

### Setup k8s networking with correct VLAN ids



## Setup LMCTL

Install 2.0 version of lmctl

```
python3 -m pip install lmctl==2.0.7.1
```

Create a file called **lmconfig.yaml** and add the following:

```
dev:
  description: dev environment on BT
  alm:
    ip_address: 172.16.14.11
    port: 8083
    protocol: https
    secure_port: true
    auth_address: 172.16.14.11
    auth_port: 8082
    username: jack
    password: jack
  arm:
    defaultrm:
      ip_address: 172.16.14.11
      port: 31081
      secure_port: True
      onboarding_addr: https://osslm-ansible-rm:8443
```

In a command shell you need to set the following environment variable to point to this file. 
```
export LMCONFIG=~/lmconfig.yaml
```

## Load VNFs and Network Services

clone this marketplace project and checkout the **provider** branch

```
git clone https://github.com/accanto-systems/marketplace.git
git checkout provider
```

And finally load the VNFs and Network services into LM

```
cd marketplace
./load.sh push dev
```
