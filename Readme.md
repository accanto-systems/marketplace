# Lifecycle Manager Project Marketplace

This project provides a set of working lifecycle manager Network Service and VNF examples along with a demonstration scenario script. 

## Network Services

| Project                    | Description                                              | Dependent VNF/NS projects    | 
|----------------------------|----------------------------------------------------------|------------------------------|
| [base](/network-services/base/Readme.md) | Create shared infrastructure and jumphost   | baseinfrastructure, network, router, jumphost |
| [voice-service](/network-services/voice-service/Readme.md) | Create a scaling voice service | voip-gateway, ip-pbx, network |
| [voice-service2](/network-services/voice-service2/Readme.md) | Clone of voice service1 with different deployment location setup | voip-gateway, ip-pbx, network |
| [voice-load-generator](/network-services/voice-load-generator/Readme.md) |  Run SIP traffic against voice service | sip-performance | 

## VNFs

| Project                                | Description                           | RM Types  | VIM types         | 
|----------------------------------------|---------------------------------------|-----------|-------------------|
| [baseinfrastructure](/vnfs/baseinfrastructure/Readme.md) | Create shared VNF infrastructure  | ARM       | Openstack |
| [network](/vnfs/network/Readme.md)     | Manage a single network instance      | ARM       | Openstack |
| [ip-pbx](/vnfs/ip-pbx/Readme.md)       | Asterisk VoIP PBX                     | ARM       | Openstack, Kubernetes |
| [voip-gateway](vnfs/voip-gateway/Readme.md)  | Kamailio VoIP Gateway           | ARM       | Openstack, Kubernetes |
| [sip-performance](/vnfs/sip-performance/Readme.md) | SIP Performance tester    | ARM       | Openstack, Kubernetes |

