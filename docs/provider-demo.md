# Provider Network Demo

1. Turn on base shared infrastructure
2. Turn on voice service in Openstack region with a single IPPBX in the scaling group 
3. Turn on SIPP on kubernetes edge
4. Turn on another SIPP on kubernetes edge
5. Watch a scaling event create a new IPPBX and connect to the gateway
6. Upgrade the service to move the gateway from openstack to kubernetes