# Provider Multus Network VNF

This VNF manages the lifecycle of an Openstack neutron provider network. Install will fail if a network with the same name exists on the target VIM. 

## Metrics

There are no metrics

## Policies

There are no policies 

## Operations

There are no operations. 

## Properties

The network VNF has the following properties:

| Property                      |  Description                        | Type      |
|-------------------------------|-------------------------------------|-----------|
| **networkname**               | Name of the new network to create   | Input     |
| **subnet**                    | IP subnet CIDR configuration             | Input     |
| **networkid**                 | id of the network in target VIM     | Read_only |
| **subnetid**                  | id of the subnet in target VIM      | Read_only |
| **gateway**                   | Gateway IP address                  | Input     |
| **provider_network**          | Boolean to specify provider network parameters | Input |
| **provider_network_type**     | Openstack provider network type     | Input     |
| **provider_physical_network** | Openstack provider network name     | Input     |
| **provider_segmentation_id**  | Openstack provider network id       | Input     |

## Deploying this VNF

Install [lmctl](/docs/install-lmctl.md) and deploy this VNF project by running the following command in this directory:

```
lmctl project push
```
