# Network VNF

This VNF manages the lifecycle of an Openstack or Docker network (depending on the VIM type). Install will fail if a network with the same name exists on the target VIM. 

## Properties & Operations

### Properties

The network VNF has the following properties:

| Property                      |  Description                        | Type      |
|-------------------------------|-------------------------------------|-----------|
| **networkname**               | Name of the new network to create   | Input     |
| **subnet**                    | IP subnet configuration             | Input     |
| **networkid**                 | id of the network in target VIM     | Read_only |
| **gateway**                   | Gateway IP address                  | Input     |
| **iprange**                   | IP Range for docker VIM             | Input     |
| **bridgeid**                  | bridge id of docker network         | Read_only |
| **provider_network**          | Boolean to specify provider network parameters | Input |
| **provider_network_type**     | Openstack provider network type     | Input     |
| **provider_physical_network** | Openstack provider network name     | Input     |
| **provider_segmentation_id**  | Openstack provider network id       | Input     |

### Operations

There are no operations. 

## Ansible RM Configuration

If deploying to Ansible RM, you need to ensure the (Lifecycle Manager deployment location)[http://servicelifecyclemanager.com/reference/resource-manager/add-vim/] is configured with the following variables:

### Openstack configuration

Openstack lifecycle manager location variables are as follows: 

```
vimtype: openstack
os_auth_url: "http://192.168.56.130/identity/v3"
os_projectname: admin
os_username: admin
os_password: secret
```

Replace the above with your Openstack credentials.

### Docker configuration

Docker variables are as follows:

```
vim: docker
location_server: 192.168.56.100
location_user: admin
location_pwd: secret
```

Replace the above with your docker location credentials.

If a jumphost is required to communicate with the docker VIM location, the following variables can be added to your lifecycle manager location to tunnel all ansible playbooks through the jumphost.

```
jumphost_address: << JUMPHOST ADDRESS >>
jumphost_username: << JUMPHOST USERNAME >>
jumphost_password: << JUMPHOST PASSWORD >>
jumphost_key: << KEY LOCATION >>
```

## Deploying this VNF

Use [lmctl](http://servicelifecyclemanager.com/reference/lmctl/) to deploy this project. (Configure your lmctl environment)[http://servicelifecyclemanager.com/reference/lmctl/#configure-lmctl-environments] and run the following command:

```
lmctl project push
```

The [CICD user guide](http://servicelifecyclemanager.com/cicd/introduction/) has more information on managing VNF packages across LM environments. 