# Provider Neutron Network VNF

This VNF manages the lifecycle of an Openstack or Docker network (depending on the VIM type). Install will fail if a network with the same name exists on the target VIM. 

## Properties & Operations

### Properties

The network VNF has the following properties:

| Property                      |  Description                        | Type      |
|-------------------------------|-------------------------------------|-----------|
| **networkname**               | Name of the new network to create   | Input     |
| **subnet**                    | IP subnet configuration             | Input     |
| **networkid**                 | id of the network in target VIM     | Read_only |
| **subnetid**                  | id of the subnet in target VIM      | Read_only |
| **gateway**                   | Gateway IP address                  | Input     |
| **iprange**                   | IP Range for docker VIM             | Input     |
| **bridgeid**                  | bridge id of docker network         | Read_only |
| **provider_network**          | Boolean to specify provider network parameters | Input |
| **provider_network_type**     | Openstack provider network type     | Input     |
| **provider_physical_network** | Openstack provider network name     | Input     |
| **provider_segmentation_id**  | Openstack provider network id       | Input     |

### Operations

There are no operations. 

## Deploying this VNF

Use [lmctl](http://servicelifecyclemanager.com/reference/lmctl/) to deploy this project. [Configure your lmctl environment](http://servicelifecyclemanager.com/reference/lmctl/#configure-lmctl-environments) and run the following command:

```
lmctl project push
```
