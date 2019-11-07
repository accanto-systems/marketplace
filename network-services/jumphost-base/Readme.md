# Basic shared infrastructure service

This network service assembly creates Site specific Openstack infrastructure that will be shared amongst other network service and VNF Assemblies. 

The following Openstack artefacts will be created and their IDs stored as properties against the Assembly instance:
* Management Neutron Network: All VNF VMs will connect to a management network for provisioning and metric collection
* Management Security Group: A shared security group with SSH open for all VNF VMs
* Voice Neutron Network: External Voice traffic network
* Voice Secutiry Group: Voice security group for all Voice VM NICs
* Jumphost VM: ALM will communicate to VNF VMs through a jumphost. The Jumphost will have a floating IP address and is connected to the management network. 