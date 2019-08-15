# Openstack Jumphost VNF

This VNF manages the lifecycle of an Openstack Jumphost machine. The jumphost attaches to a single internal openstack network and is assigned a floating ip address.

## Properties & Operations

### Properties

The network VNF has the following properties:

| Property             |  Description                        | Type      |
|----------------------|-------------------------------------|-----------|
| **jumphostname**     | Name of the virtual machine         | Input     |
| **imagename**        | Name of the image in the target VIM to use | Input     |
| **networkid**        | The internal openstack network to attach to | Input     |
| **jumphost_id**      | Openstack ID of the router created  | Read_only |
| **jumphost_ip**      | Public IP address of the jumphost   | Read_only |
| **jumphost_username**  | Username                            | Input     |
| **jumphost_password**  | Password                            | Input     |

### Operations

There are no operations. 

## Ansible RM Configuration

If deploying to Ansible RM, you need to ensure the (Lifecycle Manager deployment location)[http://servicelifecyclemanager.com/reference/resource-manager/add-vim/] is configured with the following variables:

```
vimtype: openstack
os_auth_url: "http://192.168.56.130/identity/v3"
os_projectname: admin
os_username: admin
os_password: secret
```

Replace the above with your Openstack credentials.

## Deploying this VNF

Use [lmctl](http://servicelifecyclemanager.com/reference/lmctl/) to deploy this project. (Configure your lmctl environment)[http://servicelifecyclemanager.com/reference/lmctl/#configure-lmctl-environments] and run the following command:

```
lmctl project push
```
