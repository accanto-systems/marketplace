# Neutron Router VNF

This VNF manages the lifecycle of an Openstack Neutron Router. Install will fail if a router with the same name exists on the target VIM. 

## Properties & Operations

### Properties

The network VNF has the following properties:

| Property             |  Description                        | Type      |
|----------------------|-------------------------------------|-----------|
| **routername**       | Name of the new router to create    | Input     |
| **network**          | network to attach router to         | Input     |
| **interfaces**       | comma separated list of subnet ids to attach to router | Input |
| **router_id**        | Openstack ID of the router created  | Read_only |

### Operations

There are no operations. 

## Deploying this VNF

Use [lmctl](http://servicelifecyclemanager.com/reference/lmctl/) to deploy this project. [Configure your lmctl environment](http://servicelifecyclemanager.com/reference/lmctl/#configure-lmctl-environments) and run the following command:

```
lmctl project push
```
