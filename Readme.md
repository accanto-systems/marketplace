# Lifecycle Manager Project Marketplace

This project provides a set of working lifecycle manager examples. 

* **Network Services**: End to end network services composed from a number of VNFs
* **VNFs**: Discrete logical network functions that can be composed to deliver a network service
* **VIMs**: Installers for VIM software
* **Servers**: Compute infrastructure device configurations
* **Fabric**: Installers for network controllers and logical network services

## Network Services

| Project                    | Description                                              | Dependent projects    | 
|----------------------------|----------------------------------------------------------|-----------------------|
| **voice-service**          | Manage a single network instance                         |                       |
| **voice-overlay-networks** | Neutron router                                           | Openstack             |
| **voice-load-generator**   | Asterisk VoIP PBX                                        | Openstack, Docker     | 

## VNFs

| Project                                | Description                           | RM Types  | VIM types         | 
|----------------------------------------|---------------------------------------|-----------|-------------------|
| [network](/vnfs/network/Readme.md)     | Manage a single network instance      | ARM       | Openstack, Docker |
| [router](/vnfs/router/Readme.md)       | Neutron router                        | ARM       | Openstack         |
| [jumphost](/vnfs/jumphost/Readme.md)   | Basic openstack jumphost              | ARM       | Openstack         |
| **ip-pbx**                             | Asterisk VoIP PBX                     | ARM       | Openstack, Docker |
| **voip-gateway**                       | Kamailio VoIP Gateway                 | ARM       | Openstack, Docker |
| **sip-performance**                    | SIP Performance tester                | ARM       | Openstack, Docker |

## VIM


## Servers


## Fabric

