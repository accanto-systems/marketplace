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

The [CICD user guide](http://servicelifecyclemanager.com/cicd/introduction/) has more information on managing VNF packages across LM environments. 