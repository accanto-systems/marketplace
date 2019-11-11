# Setup LM AIO

## Clone AIO project

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

Change the network in the Vagrantfile in the base directory of the AIO project so it aligns with the NFVI project. The Vagrantfile network configuration should like as follows:

```
    nodeconfig.vm.network 'private_network', ip: '192.168.10.5'
```

The NFVI infrastructure creates a set of provider networks that are used by Openstack and Kubernetes VIMs. The AIO VM must have a vNIC attached to the provider switching network, public openstack network and the management network. To attach the AIO to the provider and openstack public networks, add the following to your **lm-allinone/Vagrantfile** as the last vNICs in the list, as follows: 

```
    nodeconfig.vm.network 'public_network', dev: 's1', type: 'bridge', mode: 'bridge', :ovs => true, ip: '10.0.30.5'
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

