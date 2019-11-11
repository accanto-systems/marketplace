# Single VIM deployment with Tenant Networking

This flavour of the VoIP network service deploys to a single Openstack region and is depicted in the diagram below. 

![VoIP Service](/docs/images/basic-voip.PNG)

All networks are tenant based networks "inside" the Openstack region. Floating IP addresses are attached to a jumphost to allow management traffic to get to the internal management network, and also to the gateway external IP address to allow traffic from outside the Openstack region. 

The Openstack virtual machine and network infrastructure artefacts to deliver what's required by the network service above are described in the diagram below in more detail.

![OpenStack Infrastructure](/docs/images/basic-openstack.PNG)





## Setup target virtual data centre and VIMs

If you do not have an Openstack instance, a virtual sandbox can be setup on a bare metal machine by deploying an [NFVI underlay project](https://github.com/accanto-systems/nfvi-environment) or by installing a standard [DevStack environment](https://docs.openstack.org/devstack/latest/). 

### Setup LM

For this scenario LM must be reachable to/from Openstack public network.

If you are using LM AIO project to install LM, then follow the following [guide](/docs/install-AIO.md). 

### Configure locations in LM

Once AIO is up and running, log in and create the following locations. 

#### Add openstack Core location

Add a location called "core" with resource manager "defaultrm" and infrastructure type "Openstack" and provide the following properties

```
os_auth_url: "http://192.168.10.10:5000/v3"
os_projectname: admin
os_username: admin
os_password: password
almip: 192.168.10.5
```

Change the above with your Openstack credentials and your LM IP address. The ALM IP address is the routable address from Openstack public network. 

### Prepare Openstack

Create a key called "default".

The Jumphost and other images below depend on Openstack having a Xenial ubuntu image pre-loaded. Xenial cloud image can be downloaded from [here](https://cloud-images.ubuntu.com/xenial/current/xenial-server-cloudimg-amd64-disk1.img).

### Build Images and load VNFs/Network Services

The following Openstack images need to be built to support this scenario. 
* [IPPBX Openstack](/vnfs/ip-pbx/VNFCs/asterisk-vnfc/VDUs/packer/openstack/Readme.md)
* [Voip Gateway Openstack](/vnfs/voip-gateway/VNFCs/kamailio-vnfc/VDUs/packer/openstack/Readme.md)
* [SIPP Openstack](/vnfs/sip-performance/VNFCs/sipp-vnfc/VDUs/packer/openstack/Readme.md)

[Install LMCTL](/docs/install-lmctl.md) and load the VNFs and Network services into LM by running the following commands. 

```
cd marketplace
./load.sh push dev
```

You are now ready to run through the [basic demo scenario](/docs/basic-demo.md). 