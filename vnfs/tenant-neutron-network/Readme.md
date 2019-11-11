# Tenant Neutron Network VNF

This VNF manages the lifecycle of a neutron tenant network. This VNF will not install if a network with the same name exists on the target VIM. 

## Metrics

There are no metrics

## Policies

There are no policies 

## Operations

There are no

## Properties

Below are description of the properties

| Property                      |  Description                        | Type      |
|-------------------------------|-------------------------------------|-----------|
| **networkname**               | Name of the new network to create   | Input     |
| **subnet**                    | IP subnet configuration             | Input     |
| **networkid**                 | id of the network in target VIM     | Read_only |
| **subnetid**                  | id of the subnet in target VIM      | Read_only |
| **gateway**                   | Gateway IP address                  | Input     |

## Deploying this VNF

Install [lmctl](/docs/install-lmctl.md) and deploy this VNF project by running the following command in this directory:

```
lmctl project push
```
