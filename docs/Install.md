# NFVI Demo Setup

## Setup virtual data centre and VIMs

Create the virtual infrastructure and VIMs by cloning the NFVI underlay project as follows:

```
git clone https://github.com/accanto-systems/nfvi-environment.git
```

Follow instructions in nfvi-environment project Readme.md to configure and setup your virtual NFVI environment. 

## Setup LM

Clone [lm-allinone](https://github.com/accanto-systems/lm-allinone.git) project and add your LM software source and helm charts to **lm-allnone/lm-artifacts** directory.

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

### Theme LM if you need to

Add your theme tar file to **lm-allinone/ansible** directory and update the following properties in your **lm-allinone/ansible/ansible-variables.yml** file.

```
lm_theme: True
lm_theme_directory: .
lm_theme_name: bluerinse
```

### Add NFVI interface to AIO VM

The NFVI infrastructure creates a set of provider networks that are used by Openstack and Kubernetes VIMs. The AIO VM must have a vNIC attached to the provider switching network and configured on the management network. To attach the AIO to the provider network, add the following to your **lm-allinone/Vagrantfile** as the last vNIC in the list, as follows: 

```
    nodeconfig.vm.network 'public_network', dev: 's1', type: 'bridge', mode: 'bridge', :ovs => true, ip: '10.0.30.5'
```

### Run the AIO installation

Create your AIO by running the following command:

```
vagrant up
```

### Configure the mgmt interface on the AIO virtual machine

Once the AIO VM is up you need to configure the NIC attached to the provider switches with the correct VLAN and IPAM. The Mgmt interface is on VLAN with id 5. Add a VLAN subinterface by running the following commands in the AIO directory on your host machine as follows:

```
cd lm-allinone
vagrant ssh
sudo ifconfig eth2 0
sudo ip link add link eth2 name eth2.5 type vlan id 5
sudo ifconfig eth2.5 10.0.30.5
```

## Configure locations in LM

Once AIO is up and running, log onto LM at https://192.168.10.5:8082 and create the following locations. 

### Add openstack Core location

Add a location called "core" with resource manager "defaultRM" and infrastructure type "Openstack" and provide the following properties

```
os_auth_url: "http://192.168.10.10:5000/v3"
os_projectname: admin
os_username: admin
os_password: password
almip: 10.0.30.5
```

### Add k8s edge location

Add a location called "edge" with resource manager "defaultRM" with infrastructure type "Kubernetes" and provide the following properties

```
k8s_address: 192.168.10.50
k8s_ssh_user: vagrant
k8s_ssh_password: vagrant 
almip: 10.0.30.5
```

## Setup LMCTL

Install lmctl on your host machine by running the folowing command:

```
python3 -m pip install lmctl==2.0.7.1
```

Create a file called **lmconfig.yaml** and add the following:

```
dev:
  description: demo environment
  alm:
    ip_address: 192.168.10.5
    port: 8083
    protocol: https
    secure_port: true
    auth_address: 192.168.10.5
    auth_port: 8082
    username: jack
    password: jack
  arm:
    defaultrm:
      ip_address: 192.168.10.5
      port: 31081
      secure_port: True
      onboarding_addr: https://osslm-ansible-rm:8443
```

In a command shell you need to set the following environment variable to point to this file. 
```
export LMCONFIG=~/lmconfig.yaml
```

## Load VNFs and Network Services

Clone the marketplace project and checkout the **provider** branch

```
git clone https://github.com/accanto-systems/marketplace.git
git checkout provider
```

As required, build VNF images as per each VNF readme and load into target VIM if necessary

Finally load the VNFs and Network services into LM

```
cd marketplace
./load.sh push dev
```
