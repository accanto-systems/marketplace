# Provide Service Setup

## Setup virtual data centre and VIMs

If you do not have an Openstack instance with appropriate provider networking, an virtual sandbox can be setup on a bare metal machine by deploying an [NFVI underlay project](https://github.com/accanto-systems/nfvi-environment). 

## Setup LM

If you are using LM AIO project to install LM, then follow the following [guide](/docs/install-AIO.md). Otherwise skip this step and follow your LM instructions. 

## Configure locations in LM

Once AIO is up and running, log onto LM and create the following locations. 

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

## Load VNFs and Network Services

As required, build VNF images as per each VNF readme and load into target VIM.

Build the following Openstack images
* [IPPBX Openstack](/vnfs/ip-pbx/VNFCs/asterisk-vnfc/VDUs/packer/openstack/Readme.md)
* [Voip Gateway Openstack](/vnfs/voip-gateway/VNFCs/kamailio-vnfc/VDUs/packer/openstack/Readme.md)
* [SIPP Openstack](/vnfs/sip-performance/VNFCs/sipp-vnfc/VDUs/packer/openstack/Readme.md)

[Install LMCTL](/docs/install-lmctl.md) and load the VNFs and Network services into LM by running the following commands. 

```
cd marketplace
./load.sh push dev
```

You are now ready to run through the [provider demo scenario](/docs/provider-demo.md).

## Accessing the k8s dashboard

To access the kubernetes dashboard, you need to first get and admin-user token by running the following command. 

```
kubectl -n kubernetes-dashboard describe secret $(kubectl -n kubernetes-dashboard get secret | grep admin-user | a
```

Enter this token into the login screen of the kubernetes dashboard. 