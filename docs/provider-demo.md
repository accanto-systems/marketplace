# Provider Network Demo

1. Turn on base shared infrastructure by creating an Assembly of type **"assembly::provider-base::1.0"** with the name **"base"**
2. Turn on voice service in "core" Openstack location. This will initially stand up a single IPPBX in the scaling group Create an assembly of type **"assembly::provider-voice-service::1.0"** with the name **"voice"**
3. Turn on SIPP on in "edge" kubernetes location
4. Turn on another SIPP on "edge" kubernetes location
5. Watch a scaling event create a new IPPBX and connect to the gateway
6. Upgrade the service to change location of gateway from "core" to "edge" which will move the gateway from openstack to kubernetes and re-establish all application relationships