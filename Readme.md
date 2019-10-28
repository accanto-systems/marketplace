# Lifecycle Manager Project Marketplace

This project provides a set of working lifecycle manager Network Service and VNF examples. 

* **Network Services**: End to end network services composed from a number of VNFs
* **VNFs**: Discrete logical network functions that can be composed to deliver a network service

## Network Services

| Project                    | Description                                              | Dependent VNF/NS projects    | 
|----------------------------|----------------------------------------------------------|------------------------------|
| [mgmt_infra](/network-services/mgmt_infra/Readme.md) | Create shared infrastructure               |  jumphost                    |
| [voice-service](/network-services/voice-service/Readme.md) | Create a scaling voice service | voip-gateway, ip-pbx, network |
| [voice-load-generator](/network-services/voice-load-generator/Readme.md) |  Run SIP traffic against voice service | sip-performance | 

## VNFs

| Project                                | Description                           | RM Types  | VIM types         | 
|----------------------------------------|---------------------------------------|-----------|-------------------|
| [jumphost](/vnfs/jumphost/Readme.md)   | Basic openstack jumphost              | Brent       | Openstack, Kubernetes |
| [ip-pbx](/vnfs/ip-pbx/Readme.md)       | Asterisk VoIP PBX                     | Brent       | Openstack, Kubernetes |
| [voip-gateway](vnfs/voip-gateway/Readme.md)  | Kamailio VoIP Gateway           | Brent       | Openstack, Kubernetes |
| [sip-performance](/vnfs/sip-performance/Readme.md) | SIP Performance tester    | Brent       | Openstack, Kubernetes |

