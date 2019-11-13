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
lm_charts_package: ../lm-artifacts/lm-helm-charts-2.1.0-XXXX-dist.tgz
lm_docker_package: ../lm-artifacts/lm-docker-source-2.1.0-XXXX-dist.tgz
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

Change the network in the Vagrantfile in the base directory of the AIO project so it aligns with the NFVI project. The Vagrantfile network configuration should like as follows: 

```
    nodeconfig.vm.network 'private_network', ip: '192.168.10.5'
```

The NFVI infrastructure creates a set of provider networks that are used by Openstack and Kubernetes VIMs. The AIO VM must have a vNIC attached to the provider switching network and configured on the management network. To attach the AIO to the provider network, add the following to your **lm-allinone/Vagrantfile** as the last vNIC in the list, as follows: 

```
    nodeconfig.vm.network 'public_network', dev: 's1', type: 'bridge', mode: 'bridge', :ovs => true, ip: '10.0.30.5'
```

Likewise, NFVI Openstack public interface is bound to a local ovs bridge, **'br-ex'**. Add the following line in the Vagrantfile to attach AIO to this network so it can communicate with any virtual machines with public IP addresses. 

```
    nodeconfig.vm.network 'public_network', dev: 'br-ex', type: 'bridge', mode: 'bridge', :ovs => true, ip: '172.24.4.2'
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

## Setup LMCTL

Install lmctl on your host machine by running the folowing command:

```
python3 -m pip install lmctl
```

Create a file called **lmconfig.yaml** and add the following:

```
environments:
  dev:
    description: dev environment on BT
    alm:
      host: 192.168.10.5
      port: 8083
      protocol: https
      auth_host: 192.168.10.5
      auth_port: 8082
      username: jack
      password: jack
      secure: true
    arm:
      defaultrm:
        host: 192.168.10.5
        port: 31081
        protocol: https
```

In a command shell you need to set the following environment variable to point to this file. 
```
export LMCONFIG=~/lmconfig.yaml
```

## Install 2.1 Drivers

Log into the AIO box @ 192.168.10.5. Username/Password is vagrant/vagrant and run the following commands to attach required Resource Manager drivers. 

### Ansible lifecycle driver

Create an Ansible lifecycle driver by running the following commands in the AIO VM. 

Log into 192.168.10.5 (vagrant/vagrant) and add Ansible driver micro service:

```
helm install --name ansible-lifecycle-driver https://github.com/accanto-systems/ansible-lifecycle-driver/releases/download/v0.4.0/ansiblelifecycledriver-0.4.0.tgz
```

On your host machine run the following lmctl command to add the ansible lifecycle driver micro service to the ALM resource manager. 

```
lmctl lifecycledriver add --type ansible --url http://ansible-lifecycle-driver:8293 dev
```

### Openstack HEAT driver

Create a VIM HEAT driver by running the following commands on the AIO virtual machine @ 192.168.10.5 (vagrant/vagrant).

```
helm install --name openstack-vim-driver https://github.com/accanto-systems/openstack-vim-driver/releases/download/0.3.0/os-vim-driver-0.3.0.tgz
```
On your host machine run the following lmctl command to attach the VIM driver to the resource manager.

```
lmctl vimdriver add --type Openstack --url http://os-vim-driver:8292 dev
```

### k8s Driver

Create a k8s VIM driver by running the following command on the AIO virtual machine @ 192.168.10.5 (vagrant/vagrant)

```
helm install --name k8s-vim-driver  https://github.com/accanto-systems/k8s-vim-driver/releases/download/v0.1.0/k8s-vim-driver-0.1.0.tgz
```

On your host run the following lmctl command to add the k8s vim driver to the resource manager. 

```
lmctl vimdriver add --type Kubernetes --url http://k8s-vim-driver:8294 dev
```

## Add locations

Add NFVI locations to ALM

### Openstack Core location

#### Configure locations in LM

Once AIO is up and running, log onto LM at https://192.168.10.5:8082 and create the following locations. 

Add a location called "core-provider" with resource manager "brent" and infrastructure type "Openstack" and provide the following properties

```
os_auth_project_name: admin
os_auth_project_domain_name: default
os_auth_password: password
os_auth_username: admin
os_auth_user_domain_name: default
os_auth_api: v3
os_api_url: http://192.168.10.10:5000
almip: 10.0.30.5
```

Add a location called "core" with resource manager "brent" and infrastructure type "Openstack" and provide the following properties

```
os_auth_project_name: admin
os_auth_project_domain_name: default
os_auth_password: password
os_auth_username: admin
os_auth_user_domain_name: default
os_auth_api: v3
os_api_url: http://192.168.10.10:5000
almip: 172.24.4.2
```

#### Configure locations with lmctl

```
{   
    "os_auth_project_name": "admin",
    "os_auth_project_domain_name": "default",
    "os_auth_password": "password",
    "os_auth_username": "admin",
    "os_auth_user_domain_name": "default",
    "os_auth_api": "v3",
    "os_api_url": "http://192.168.10.10:5000",
    "almip": "10.0.30.5"
}

lmctl deployment add dev core-provider -r brent -i Openstack -d "something" -p "path to file with above config" 

```
```
{   
    "os_auth_project_name": "admin",
    "os_auth_project_domain_name": "default",
    "os_auth_password": "password",
    "os_auth_username": "admin",
    "os_auth_user_domain_name": "default",
    "os_auth_api": "v3",
    "os_api_url": "http://192.168.10.10:5000",
    "almip": "172.24.4.2"
}

lmctl deployment add dev core -r brent -i Openstack -d "something" -p "path to file with above config" 

```
### k8s edge location

#### Grab k8s secret and certificates

Log onto NFVI k8s master node (assume kubeadm K8s cluster), e.g. 192.168.10.50 (vagrant/vagrant), and note down from the /etc/kubernetes/admin.conf file the following:

* client-certificate-data
* client-key-data
* certificate-authority-data

These will be needed when adding the K8s deployment location to LM.

#### Configure locations with lmctl

Create a file with the following json:

```
{   
    "k8s-server": "https://192.168.10.50:6443",
    "k8s-namespace": "default",
    "k8s-certificate-authority-data": "INSERT client-certificate-data",
    "k8s-client-certificate-data": "INSERT client-certificate-data",
    "k8s-client-key-data": "INSERT client-key-data",
    "almip": "10.0.30.5"
}
```

Create location in LM with lmctl and file you created

```
lmctl deployment add dev edge-provider -r brent -i Kubernetes -d "something" -p "path to file with above config" 

```

Create a file with the following json:

```
{   
    "k8s-server": "https://192.168.10.50:6443",
    "k8s-namespace": "default",
    "k8s-certificate-authority-data": "INSERT client-certificate-data",
    "k8s-client-certificate-data": "INSERT client-certificate-data",
    "k8s-client-key-data": "INSERT client-key-data",
    "almip": "172.24.4.2"
}
```

Create location in LM with lmctl and file you created

```
lmctl deployment add dev edge -r brent -i Kubernetes -d "something" -p "path to file with above config" 

```
## Load VNFs and Network Services

Clone the marketplace project and checkout the **port-heat** branch

```
git clone https://github.com/accanto-systems/marketplace.git
git checkout port-heat
```

As required, build VNF images as per each VNF readme and load into target VIM if necessary

Finally load the VNFs and Network services into LM

```
cd marketplace
./load.sh push dev
```

## Accessing the k8s dashboard

get admin-user token to log in

```
kubectl -n kubernetes-dashboard describe secret $(kubectl -n kubernetes-dashboard get secret | grep admin-user | awk '{print $1}')
```

