# SIP Performance Test VNF# IP PBX VNF

This VNF packages a [SIP Performance tester](http://sipp.sourceforge.net/) with the LM standard lifecycle API.

## Properties & Operations

### Properties

The network VNF has the following properties:

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

### Operations

There are no operations. 

### Metrics

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

### Policies

There are no policies 


## Build SIPP Images

#### Software dependencies

The following software must be installed to your local machine to create an IP PBX VIM image. 
* [Packer](https://packer.io/)

#### Build the image

To deploy to an OpenStack VIM [run the Openstack packer installer](/vnfs/sip-performance/VNFCs/sipp-vnfc/VDUs/packer/openstack/Readme.md).

To deploy to a container based VIM [run the docker packer installer](/vnfs/sip-performance/VNFCs/sipp-vnfc/VDUs/packer/docker/Readme.md).

### Load the VIM image to CICD Hub

Load the VIM image you created above to the CICD Hub image repository and to your target VIM. You can follow the instructions [here](http://servicelifecyclemanager.com/user-guides/cicd/upload-images/).

The [CICD user guide](http://servicelifecyclemanager.com/user-guides/cicd/getting-started/) has more information on managing VNF packages across LM environments. 

## Deploying this VNF

Use [lmctl](http://servicelifecyclemanager.com/reference/lmctl/) to deploy this project. [Configure your lmctl environment](http://servicelifecyclemanager.com/reference/lmctl/#configure-lmctl-environments) and run the following command:

```
lmctl project push
```
