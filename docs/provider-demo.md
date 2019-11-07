# Provider Network Demo

1. Turn on base shared infrastructure
2. Turn on voice service in "core" Openstack region. This will initially stand up a single IPPBX in the scaling group 
3. Turn on SIPP on in "edge" kubernetes location
4. Turn on another SIPP on "edge" kubernetes location
5. Watch a scaling event create a new IPPBX and connect to the gateway
6. Upgrade the service to change location of gateway from "core" to "edge" which will move the gateway from openstack to kubernetes and re-establish all application relationships