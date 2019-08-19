# Lifecycle Manager Project Marketplace

This project provides a set of working lifecycle manager Network Service and VNF examples. 

* **Network Services**: End to end network services composed from a number of VNFs
* **VNFs**: Discrete logical network functions that can be composed to deliver a network service
* **VIMs**: Installers for VIM software
* **Servers**: Compute infrastructure device configurations
* **Fabric**: Installers for network controllers and logical network services

## Network Services

| Project                    | Description                                              | Dependent VNF/NS projects    | 
|----------------------------|----------------------------------------------------------|------------------------------|
| [base](/network-services/base/Readme.md) | Create shared infrastructure and jumphost   | baseinfrastructure, network, router, jumphost |
| [voice-service](/network-services/voice-service/Readme.md) | Create a scaling voice service | voip-gateway, ip-pbx, network |
| [voice-load-generator](/network-services/voice-load-generator/Readme.md) |  Run SIP traffic against voice service | sip-performance | 

## VNFs

| Project                                | Description                           | RM Types  | VIM types         | 
|----------------------------------------|---------------------------------------|-----------|-------------------|
| [baseinfrastructure](/vnfs/baseinfrastructure/Readme.md) | Create shared VNF infrastructure  | ARM       | Openstack |
| [network](/vnfs/network/Readme.md)     | Manage a single network instance      | ARM       | Openstack |
| [router](/vnfs/router/Readme.md)       | Neutron router                        | ARM       | Openstack |
| [jumphost](/vnfs/jumphost/Readme.md)   | Basic openstack jumphost              | ARM       | Openstack |
| [ip-pbx](/vnfs/ip-pbx/Readme.md)       | Asterisk VoIP PBX                     | ARM       | Openstack |
| [voip-gateway](vnfs/voip-gateway/Readme.md)  | Kamailio VoIP Gateway           | ARM       | Openstack |
| [sip-performance](/vnfs/sip-performance/Readme.md) | SIP Performance tester    | ARM       | Openstack |

## VIM

Coming soon

* Openstack

## Servers

Coming soon

* Compute Node
* Control Node
* Network Node
* Network Bond

## Fabric

Coming soon

* OVS Switch
* Onos Controller