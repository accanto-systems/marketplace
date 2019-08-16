# IP PBX VNF

This VNF packages an [Asterisk VoIP server](https://www.asterisk.org/) with the LM standard lifecycle API.

## Properties & Operations

### Properties

The network VNF has the following properties:

| Property             |  Description                        | Type      |
|----------------------|-------------------------------------|-----------|
| **mgmt_network**     | id of the management network        | Input     |
| **data_network**     | id of the network voice traffic will be carried on | Input    |
| **gw_address**       | ip address of a SIP gateway that proxies traffic to this VoIP Server if it exists | Input    |
| **mgmt_address**     | management ip address assigned to VoIP Server instance | Read Only |
| **data_address**     | data ip address assigned to VoIP Server instance  | Read Only |
| **jumphost_ip**      | ip assigned to jumphost             | Input     |
| **jumphost_username** | jumphost username                  | Input     |
| **jumphost_password** | jumphost password                  | Input     |

### Operations

There are no operations. 

### Metrics

| Metric               |  Description                        |
|----------------------|-------------------------------------|
| **h_integrity**      | health integrity metric             |

### Policies

| Policy               |  Description                        |
|----------------------|-------------------------------------|
| **heal**             | healing policy on asterisk vnfc listening to health metrics from above  |

## Ansible RM Configuration

If deploying to Ansible RM, you need to ensure the (Lifecycle Manager deployment location)[http://servicelifecyclemanager.com/reference/resource-manager/add-vim/] is configured with the following variables:


### Openstack configuration

Openstack lifecycle manager location variables are as follows: 

```
vimtype: openstack
os_auth_url: "http://192.168.56.130/identity/v3"
os_projectname: admin
os_username: admin
os_password: secret
almip: 192.168.56.100
```

Replace the above with your Openstack credentials.

### Docker configuration

Docker variables are as follows:

```
vimtype: docker
location_server: 192.168.56.100
location_user: admin
location_pwd: secret
almip: 192.168.56.100
```

Replace the above with your docker location credentials.

## Deploying this VNF

Use [lmctl](http://servicelifecyclemanager.com/reference/lmctl/) to deploy this project. [Configure your lmctl environment](http://servicelifecyclemanager.com/reference/lmctl/#configure-lmctl-environments) and run the following command:

```
lmctl project push
```

## VIM Images

Follow the steps below to build VIM images and load the VNF package
* [Build a VIM run time image](#create-the-vim-image)
* [Load VIM image to CICD Hub](#load-the-vim-image-to-cicd-hub)
* [Create VNF package](#push-vnf-package)

### Create the VIM image

To run this VNF an image must be built appropriate for the target VIM. 

#### Software dependencies

The following software must be installed to your local machine to create an IP PBX VIM image. 
* [Packer](https://packer.io/)

#### Build the image

To deploy to an OpenStack VIM [run the Openstack packer installer](/vnfs/ip-pbx/VNFCs/asterisk-vnfc/VDUs/packer/openstack/Readme.md).

To deploy to a container based VIM [run the docker packer installer](/vnfs/ip-pbx/VNFCs/asterisk-vnfc/VDUs/packer/docker/Readme.md).

### Load the VIM image to CICD Hub

Load the VIM image you created above to the CICD Hub image repository and to your target VIM. You can follow the instructions [here](http://servicelifecyclemanager.com/user-guides/cicd/upload-images/).


The [CICD user guide](http://servicelifecyclemanager.com/user-guides/cicd/getting-started/) has more information on managing VNF packages across LM environments. 