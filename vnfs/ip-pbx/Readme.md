# VoIP Server VNF

The VoIP Server VNF is a PBX provisioned with a set of Dial Plan entries that answer voice calls and respond with a recorded message. This VoIP VNF has a single VNFC with [Asterisk VoIP server](https://www.asterisk.org/) deployed on a single virtual machine. 

![Overview](/vnfs/ip-pbx/images/overview.PNG)

The picture above shows the various external lifecycle manager capabilities of the VNF that can be used by other VNFs or require input from other VNFs for it to work. These are described in more detail below. 

## Infrastructure

Networks and security groups are required to be provided externally to this gateway VNF, as follows:
* **Mgmt**: The management network and security group for all operational provisioning and metrics are carried on
* **Internal**: Internal voice traffic to voip servers is routed on this network/security group.

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

## Properties

The network VNF has the following properties:

| Property             |  Description                        | Type      |
|----------------------|-------------------------------------|-----------|
| **mgmt_network**     | id of the management network        | Input     |
| **data_network**     | id of the network voice traffic will be carried on | Input    |
| **data_cidr**        | subnet cidr for data network        | Input    |
| **gw_address**       | ip address of a SIP gateway that proxies traffic to this VoIP Server if it exists | Input    |
| **mgmt_address**     | management ip address assigned to VoIP Server instance | Read Only |
| **data_address**     | data ip address assigned to VoIP Server instance  | Read Only |
| **jumphost_ip**      | ip assigned to jumphost             | Input     |
| **jumphost_username** | jumphost username                  | Input     |
| **jumphost_password** | jumphost password                  | Input     |

## Building IP PBX VNF Images

The following software must be installed to your local machine to create an IP PBX VIM image. 
* [Packer](https://packer.io/)

#### Build the image(s)

To deploy to an OpenStack VIM [run the Openstack packer installer](/vnfs/ip-pbx/VNFCs/asterisk-vnfc/VDUs/packer/openstack/Readme.md).

To deploy to a container based VIM [run the docker packer installer](/vnfs/ip-pbx/VNFCs/asterisk-vnfc/VDUs/packer/docker/Readme.md).

## Deploying this VNF

Install [lmctl](/docs/install-lmctl.md) and deploy this VNF project by running the following command in this directory:

```
lmctl project push
```
