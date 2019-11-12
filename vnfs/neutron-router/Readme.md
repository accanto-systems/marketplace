# Neutron Router VNF

This VNF manages the lifecycle of an Openstack Neutron Router. Install will fail if a router with the same name exists on the target VIM. 

## Metrics

There are no metrics

## Operations

There are no operations. 

## Properties

The network VNF has the following properties:

| Property             |  Description                        | Type      |
|----------------------|-------------------------------------|-----------|
| **routername**       | Name of the new router to create    | Input     |
| **network**          | external network name or id to attach router to         | Input     |
| **interface**        | subnet id of network interface to attach to router | Input |
| **router_id**        | Openstack ID of the router created  | Read_only |

## Deploying this VNF

Install [lmctl](/docs/install-lmctl.md) and deploy this VNF project by running the following command in this directory:

```
lmctl project push
```
