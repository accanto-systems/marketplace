# Openstack Jumphost VNF

This VNF manages the lifecycle of an Openstack Jumphost machine. The jumphost attaches to a single internal openstack network and is assigned a floating ip address.

## Metrics

There are no metrics

## Operations

There are no operations. 

## Properties

The network VNF has the following properties:

| Property             |  Description                        | Type      |
|----------------------|-------------------------------------|-----------|
| **jumphostname**     | Name of the virtual machine         | Input     |
| **keyname**          | Name of the openstack keypair       | Input     |
| **networkid**        | The internal openstack network to attach to | Input     |
| **jumphost_id**      | Openstack ID of the router created  | Read_only |
| **jumphost_ip**      | Public IP address of the jumphost   | Read_only |
| **jumphost_username**  | Username                            | Input     |
| **jumphost_password**  | Password                            | Input     |

## Jumphost Image

The jumphost uses the latest Ubuntu Xenial image, this can be downloaded from [here](https://cloud-images.ubuntu.com/xenial/current/xenial-server-cloudimg-amd64-disk1.img)

## Deploying this VNF

Install [lmctl](/docs/install-lmctl.md) and deploy this VNF project by running the following command in this directory:

```
lmctl project push
```
