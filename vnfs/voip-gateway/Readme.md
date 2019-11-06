# Kamailio VoIP Gateway VNF

This VNF packages a [Kamailio SIP Gateway](https://www.kamailio.org/w/) with the LM standard lifecycle API.

This VNF manages the lifecycle of an Openstack or Docker network (depending on the VIM type). Install will fail if a network with the same name exists on the target VIM. 

## Properties & Operations

### Properties

The network VNF has the following properties:

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

### Operations

There following operation are available. 

| Operation                     |  Description                               |
|-------------------------------|--------------------------------------------|
| **addToDispatchList**         | Add a voip server to the gateway pool      |
| **deleteFromDispatchList**    | Remove a voip server from the gateway pool |
  
### Metrics

This VNF produces the following metrics:

| Metric                   |  Description                        |
|--------------------------|-------------------------------------|
| **h_load**               | current number of sessions          |

### Policies

There are no policies 

## Ansible RM Configuration

If deploying to Ansible RM, you need to ensure the (Lifecycle Manager deployment location)[http://servicelifecyclemanager.com/reference/resource-manager/add-vim/] is configured with the following variables:

## Deploying this VNF

Use [lmctl](http://servicelifecyclemanager.com/reference/lmctl/) to deploy this project. (Configure your lmctl environment)[http://servicelifecyclemanager.com/reference/lmctl/#configure-lmctl-environments] and run the following command:

```
lmctl project push
```

The [CICD user guide](http://servicelifecyclemanager.com/cicd/introduction/) has more information on managing VNF packages across LM environments. 

## VIM Images

Follow the steps below to build VIM images and load the VNF package
* [Build a VIM run time image](#create-the-vim-image)
* [Load VIM image to CICD Hub](#load-the-vim-image-to-cicd-hub)
* [Create VNF package](#push-vnf-package)

## Create the VIM image

To run this VNF an image must be built appropriate for the target VIM. 

### Software dependencies

The following software must be installed to your local machine to create an IP PBX VIM image. 
* [Packer](https://packer.io/)

### Build the image

To deploy to an OpenStack VIM [run the Openstack packer installer](/vnfs/voip-gateway/VNFCs/kamailio-vnfc/VDUs/packer/openstack/Readme.md).

To deploy to a container based VIM [run the docker packer installer](/vnfs/voip-gateway/VNFCs/kamailio-vnfc/VDUs/packer/docker/Readme.md).

## Load the VIM image to CICD Hub

Load the VIM image you created above to the CICD Hub image repository and to your target VIM. You can follow the instructions [here](http://servicelifecyclemanager.com/user-guides/cicd/upload-images/).
