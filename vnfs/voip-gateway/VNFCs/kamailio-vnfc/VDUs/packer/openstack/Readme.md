# Building a VoIP Gateway OpenStack image

## Pre-requisites

* [Packer](https://packer.io/) running on your host machine.
* A running OpenStack environment
* [Ubuntu Xenial image](http://cloud-images.ubuntu.com/xenial/current/xenial-server-cloudimg-amd64-disk1.img) pre-loaded to your OpenStack.
* Ensure you have a private neutron network connected to a router which is bound to a public network. Packer will deploy a build VM to this private network.
* The security group specified must have the ssh port open for packer to communicate with the VM it creates. 
* Create a new keypair and store the private key file on your local machine. 

## Configure your packer script

In the **voip-gateway/VNFCs/asterisk-vnfc/VDUs/packer/openstack/kamailio.json** packer script, set the following ids from your openstack deployment.

```
  "identity_endpoint": "http://<YOUR OPENSTACK>/identity/v3",
  "tenant_name": "<YOUR OPENSTACK TENANT NAME>",
  "username": "<YOUR OPENSTACK USERNAME>",
  "password": "<YOUR OPENSTACK PASSWORD>",
  "networks": ["<PRIVATE NETWORK>"],
  "floating_ip_network":"<PUBLIC NETWORK>",
  "ssh_keypair_name": "<KEYPAIR NAME>",
  "ssh_private_key_file":"<KEYPAIR PEM>", 
  "source_image": "<XENIAL IMAGE ID>",
  "security_groups":["<YOUR SECURITY GROUP>"],
```

## Create the Kamailio Image

Download [Kamailio](https://www.kamailio.org/pub/kamailio/5.0.2/src/kamailio-5.0.2_src.tar.gz) and [RTP engine](https://github.com/sipwise/rtpengine/archive/mr5.5.10.1.zip) to voip-gateway/VNFCs/kamailio-vnfc/VDUs/packer/software/ directory.

Ensure your Openstack Environment has the following artefacts configured:
* If it does not exist, create an "internal" neutron network
* Ensure the "internal" network is connected to a router router to public network
* Create a keypair for Packer to communicate with the VM
* Ensure a security group with ssh ports open are available for packer to talk to the image

Update the packer configuration file with the IDs of the Openstack assets above and run the following command to build the kamailio image.

```
packer build kamailio.json
```

## Retrieve the image to your local machine

Once the packer process is finished you can retrieve the image from you openstack environment by running the following command. 

```
glance image-download kamailio
```

You can push this to your CICD Hub image repository to be used in other OpenStack instances.
