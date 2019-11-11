# Kamailio VoIP Gateway VNF

A Voice Gateway VNF proxies VoIP SIP signalling and RTP traffic and load balances across a pool of registered VoIP servers. 

This gateway VNF has a single VNFC with [Kamailio SIP Gateway](https://www.kamailio.org/w/) and [RTP engine](https://github.com/sipwise/rtpengine) applications deployed on a single virtual machine. 

![Overview](/vnfs/voip-gateway/images/overview.PNG)

The picture above shows the various external lifecycle manager capabilities of the VNF that can be used by other VNFs or require input from other VNFs for it to work.

## Infrastructure

Networks and security groups are required to be provided externally to this gateway VNF, as follows:
* **Mgmt**: The management network and security group for all operational provisioning and metrics are carried on
* **External**: External voice traffic appears on this network/security group
* **Internal**: Internal voice traffic to voip servers is routed on this network/security group.

## Operations

The following operations are provided.

### DispatchList

Add/Delete VoIP servers to the Gateway dispatch list or pool.

| Operation                     |  Description                               |
|-------------------------------|--------------------------------------------|
| **addToDispatchList**         | Add a voip server to the gateway pool      |
| **deleteFromDispatchList**    | Remove a voip server from the gateway pool |
  
## Metrics

This VNF produces the following metrics:

| Metric                   |  Description                        |
|--------------------------|-------------------------------------|
| **h_load**               | current number of sessions          |

## Policies

There are no policies 

## Properties

The gateway VNF has the following properties:

| Property                      |  Description                        | Type      |
|-------------------------------|-------------------------------------|-----------|
| **mgmt_network**              | id of the management network        | Input     |
| **mgmt_address**              | mgmt ip address                     | Read Only |
| **external_network**          | id of the external network          | Input     |
| **external_address**          | external facing ip address          | Read Only |
| **internal_network**          | id of the internal network          | Input     |
| **internal_address**          | internal ip address                 | Read Only |
| **keyname**                   | openstack key name                  | Input     |
| **mgmt_securitygroup_id**     | id of the mgmt security group       | Input     |
| **voice_securitygroup_id**    | id of the voice security group      | Input     |
| **jumphost_ip**      | ip assigned to jumphost             | Input     |
| **jumphost_username** | jumphost username                  | Input     |
| **jumphost_password** | jumphost password                  | Input     |


## VIM Images

The following software must be installed to your local machine to create an IP PBX VIM image. 
* [Packer](https://packer.io/)

### Build the gateway image(s)

To deploy to an OpenStack VIM [run the Openstack packer installer](/vnfs/voip-gateway/VNFCs/kamailio-vnfc/VDUs/packer/openstack/Readme.md).

To deploy to a container based VIM [run the docker packer installer](/vnfs/voip-gateway/VNFCs/kamailio-vnfc/VDUs/packer/docker/Readme.md).

## Deploying this VNF

Install [lmctl](/docs/install-lmctl.md) and deploy this VNF project by running the following command in this directory:

```
lmctl project push
```
