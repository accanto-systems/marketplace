# Lifecycle Manager Project Marketplace

This project provides a set of working lifecycle manager Network Service and VNF examples. This branch supports version 2.0 of StratOSS Lifecycle Manager only. Worked examples for other versions of SLM are available on other branches in this project.

## VoIP Network Service Worked Example

An example VoIP Network Service is provided that uses a set of open source VNFs. The VoIP service includes a Voice (SIP & RTP) Gateway that load balances voice traffic across a dynamic pool of IPPBX servers. To test the service a SIP performance test VNF is also included that can simulate voice traffic and demonstrate IPPBX cluster behaviour. 

![VoIP Service](/docs/images/voip-service-intro.PNG)

The following Opensource VNFs are included:
* [**Voice Gateway**](/vnfs/voip-gateway/Readme.md)
* [**IPPBX Server**](/vnfs/ip-pbx/Readme.md)
* [**SIPP traffic simulator**](/vnfs/sip-performance/Readme.md)

Suporting VNFs are provided that wrap openstack networking as follows:
* [**Router**](/vnfs/neutron-router/Readme.md):
* [**Tenant Network**](/vnfs/tenant-neutron-network/Readme.md):
* [**Provider Network**](/vnfs/provider-neutron-network/Readme.md):

The diagram below shows a logical VoIP Network Service deployment with some use case behaviour that must be automated by the lifecycle manager. 

![VoIP Server Deployment Rules](/docs/images/voice-service-logical-deployment.PNG)

### LM Use Cases
1. Stand up the VoIP network service VNFs and perform required initial integrations to have a working gateway with 1 initial VoIP server in its pool to service external calls. 
2. Run a SIP VNF and attach it to the VoIP Network service to simulate users. Load metrics generate by the gateway can show current user sessions being serviced by the network service.
3. Add SIP VNFs to simulate additional users. Increased load metrics trigger a scale policy in the VoIP Server pool, adding a new VoIP server and adding itself to the gateway dispatch list so it can load balance and route calls. 
4. If an infrastructure failure occurs in the VoIP Server pool a policy is triggered that will heal and recover the network service. 


### Network Service flavours

Two flavours of the VoIP Network Service are provided:

* [Single VIM with Tenant Networking](/docs/install-jumphost.md): A basic VoIP service that runs in a single OpenStack region using tenant networking. 
* [Multiple VIMs with Provider Networking](/docs/install-provider.md): An multi VIM version of the VoIP service deployed across Openstack and Kubernetes data centres.




