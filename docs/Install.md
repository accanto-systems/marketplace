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

### Run the AIO installation

```
vagrant up
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

### Create openstack keypairs

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

