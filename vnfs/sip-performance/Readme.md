# SIP Performance Test VNF# IP PBX VNF

SIP Performance VNF generates simulated SIP and RTP traffic This SIP Performance VNF has a single VNFC with [SIP Performance tester](http://sipp.sourceforge.net/) deployed on a single virtual machine. 

![Overview](/vnfs/sip-performance/images/Overview.PNG)

The picture above shows the various external lifecycle manager capabilities of the VNF that can be used by other VNFs or require input from other VNFs for it to work. These are described in more detail below. 

## Operations

There are no operations. 

## Metrics

This VNF produces the following metrics:

| Metric                      |  Description                        |
|-----------------------------|-------------------------------------|
| **call rate**               | |
| **outgoing calls**          | |
| **total calls created**     | |
| **total successful calls**  | |
| **successful calls**        | |
| **failed calls**            | |
| **total failed calls**      | |
| **current calls**           | |

## Policies

There are no policies 

## Properties

The SIPP VNF has the following properties:

| Property              |  Description                                  | Type      |
|-----------------------|-----------------------------------------------|-----------|
| **target_sip_address**  | ip address of target to send SIP callls to  | Input     |
| **mgmt_network**      | id of the management network                  | Input     |
| **data_network**      | id of the network voice traffic will be carried on | Input    |
| **mgmt_address**      | management ip address assigned to VoIP Server instance | Read Only |
| **data_address**      | data ip address assigned to VoIP Server instance  | Read Only |
| **jumphost_ip**       | ip assigned to jumphost                       | Input     |
| **jumphost_username** | jumphost username                             | Input     |
| **jumphost_password** | jumphost password                             | Input     |
| **keyname**           | name of the openstack key                     | Input     |
| **mgmt_securitygroup_id | id of mgmt securitygroup                    | Input     |
|  **voice_securitygroup_id | id of voice securitygroup                 | Input     |
| **jumphost_ip**      | ip assigned to jumphost             | Input     |
| **jumphost_username** | jumphost username                  | Input     |
| **jumphost_password** | jumphost password                  | Input     |

## Build SIPP Images

The following software must be installed to your local machine to create an IP PBX VIM image. 
* [Packer](https://packer.io/)

#### Build the image

To deploy to an OpenStack VIM [run the Openstack packer installer](/vnfs/sip-performance/VNFCs/sipp-vnfc/VDUs/packer/openstack/Readme.md).

To deploy to a container based VIM [run the docker packer installer](/vnfs/sip-performance/VNFCs/sipp-vnfc/VDUs/packer/docker/Readme.md).

## Deploying this VNF

Install [lmctl](/docs/install-lmctl.md) and deploy this VNF project by running the following command in this directory:

```
lmctl project push
```
