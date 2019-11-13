# Edge Provider base network service

This network service assembly creates Site specific Openstack infrastructure that will be shared amongst other network service and VNF Assemblies. 

The following Openstack artefacts will be created and their IDs stored as properties against the Assembly instance:
* Management Provider Network: All VNF VMs will connect to a management network for provisioning and metric collection, attached to external VLAN
* Management Security Group: A shared security group with SSH open for all VNF VMs
* Voice Provider Network: External Voice traffic network attached to external VLAN
* Voice Secutiry Group: Voice security group for all Voice VM NICs
