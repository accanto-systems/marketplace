# Lifecycle Manager Project Marketplace

This project provides a set of working lifecycle manager Network Service and VNF examples. An example VoIP Service is implemented around a set of opensource VNFs, as follows: 

![VoIP Service](/docs/images/voip-service-intro.PNG)

The VoIP service includes a Voice (SIP & RTP) Gateway that load balances voice traffic across a dynamic pool of IPPBX servers. To test the service a SIP performance test VNF is also included that can simulate voice traffic and demonstrate IPPBX cluster behaviour. 

The following Opensource VNFs are included:
* [**Voice Gateway**](/vnfs/voip-gateway/Readme.md)
* [**IPPBX Server**](/vnfs/ip-pbx/Readme.md)
* [**SIPP traffic simulator**](/vnfs/sip-performance/Readme.md)

Two flavours of the VoIP Service are included as described below.

## Basic VoIP Service 

The basic VoIP service runs in a single OpenStack region using tenant networking. 

![VoIP Service](/docs/images/basic-voip.PNG)

Instructions to run this demo can be found [here](/docs/install-jumphost.md)

## VoIP Service with Provider Networking

An advanced version of the VoIP service is deployed across Openstack and Kubernetes data centres.

![VoIP Service](/docs/images/provider-voip.PNG)

Instructions to run this demo can be found [here](/docs/install-provider.md)




