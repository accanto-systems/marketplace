# Single VIM deployment with Tenant Networking

This flavour of the VoIP network service deploys to a single Openstack region. The network service VNF and Openstack infrastrcuture components are depicted in the diagram below. 

![VoIP Service](/docs/images/basic-voip.PNG)

All networks are tenant based networks "inside" the Openstack region. Floating IP addresses are attached to a jumphost to allow management traffic to get to the internal management network, and also to the gateway external IP address to allow traffic from outside the Openstack region. 

The Openstack virtual machine and network infrastructure artefacts to deliver what's required by the network service above are described in the diagram below in more detail.

![OpenStack Infrastructure](/docs/images/basic-openstack.PNG)

* **Shared Region Infrastructure**: All VNFs deployed into this Openstack region attach to the same neutron management network and security groups. This infrastructure is modelled in the [**jumphost-base**](/network-services/jumphost-base/Readme.md) network service. 
* **Shared Voice Infrastructure**: All VNFs in a particular VoIP network instances attach to the same voice and internal networks and security groups. This infrastructure is modelled in the [**jumphost-voice-service**](/network-services/jumphost-voice-service/Readme.md) network service. 
* **VoIP Server Infrastructure**: Virtual machine and network ports that attach to shared networks for the VoIP server. This infrastructure is modelled in the [**ip-pbx**](/vnfs/ip-pbx/Readme.md) VNF.
* **GW Infrastructure**: Virtual machine and network ports that attach to shared networks for the gateway. This infrastructure is modelled in the [**voip-gateway**](/vnfs/voip-gateway/Readme.md) VNF. 

## Setup target virtual data centre and VIMs

You can use an existing Openstack region or create your own virtual Openstack instance on a bare metal machine by deploying an [NFVI underlay project](https://github.com/accanto-systems/nfvi-environment) or by installing a standard [DevStack environment](https://docs.openstack.org/devstack/latest/) instance. A helper project to install Devstack can be found [here](https://github.com/accanto-systems/devstack-environment). 

The single VIM tenant scenario relies on Openstack being configured with a public external network. If you have a different setup, e.g. a provider based public network, you may have to reconfigure the **jumphost-base** packages to reflect your networking setup. 

### Setup LM

For this demonstration scenario LM must be reachable to/from Openstacks public network.

If you are using the LM AIO project to install LM, then follow the following [guide](/docs/install-AIO.md). 

### Configure locations in LM

Once AIO is up and running, log in and create the following locations. 

#### Add openstack Core location

Add a location called "core" with resource manager "defaultrm" and infrastructure type "Openstack" and provide the following properties

```
os_auth_url: "http://192.168.10.10:5000/v3"
os_projectname: admin
os_username: admin
os_password: password
almip: 172.24.4.2
```

Change the above with your Openstack credentials and your LM IP address. The LM IP address is the routable address from Openstack public network. 

### Prepare Openstack

Create a key called "default".

The Jumphost and other images below depend on Openstack having a Xenial ubuntu image pre-loaded. Xenial cloud image can be downloaded from [here](https://cloud-images.ubuntu.com/xenial/current/xenial-server-cloudimg-amd64-disk1.img).

### Build Images and load VNFs/Network Services

The following Openstack images need to be built to support this scenario. 
* [VoIP PBX Openstack](/vnfs/ip-pbx/VNFCs/asterisk-vnfc/VDUs/packer/openstack/Readme.md)
* [Voip Gateway Openstack](/vnfs/voip-gateway/VNFCs/kamailio-vnfc/VDUs/packer/openstack/Readme.md)
* [SIPP Openstack](/vnfs/sip-performance/VNFCs/sipp-vnfc/VDUs/packer/openstack/Readme.md)

[Install LMCTL](/docs/install-lmctl.md) and load the VNFs and Network services into LM by running the following commands. 

```
cd marketplace
./load.sh push dev
```

You are now ready to run through the [basic demo scenario](/docs/basic-demo.md). 