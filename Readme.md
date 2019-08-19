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
| (base)[/network-services/base/Readme.md]  | Create management network and jumphost                   | Network, Router, Jumphost    |
| (voice-service)[/network-services/voice-service/Readme.md]  |                              |  |
| (voice-overlay-networks)[/network-services/voice-overlay-networks/Readme.md] |             |  |
| (voice-load-generator)[/network-services/voice-load-generator/Readme.md]     |             |  | 

## VNFs

| Project                                | Description                           | RM Types  | VIM types         | 
|----------------------------------------|---------------------------------------|-----------|-------------------|
| [network](/vnfs/network/Readme.md)     | Manage a single network instance      | ARM       | Openstack, Docker |
| [router](/vnfs/router/Readme.md)       | Neutron router                        | ARM       | Openstack         |
| [jumphost](/vnfs/jumphost/Readme.md)   | Basic openstack jumphost              | ARM       | Openstack         |
| [ip-pbx](/vnfs/ip-pbx/Readme.md)       | Asterisk VoIP PBX                     | ARM       | Openstack, Docker |
| [voip-gateway](vnfs/voip-gateway/Readme.md)  | Kamailio VoIP Gateway           | ARM       | Openstack, Docker |
| [sip-performance](/vnfs/sip-performance/Readme.md) | SIP Performance tester    | ARM       | Openstack, Docker |
| iperf                                  | network performance VNF               | ARM       | Openstack         |
| nprobe                                 | VoIP Probe VNF                        | ARM       | Openstack         |
| vyos                                   | vrouter VNF                           | ARM       | Openstack         |

## VIM

Coming soon

* NFVI
* Packstack

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