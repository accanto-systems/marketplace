# Provider Network Demo

## Instantiate site shared infrastructure

Turn on base shared infrastructure by creating an Assembly of type **"assembly::core-provider-base::1.0"** with the name **"corebase"**. The the deployment location is defaulted to **core-provider**. 

Turn on base shared infrastructure by creating an Assembly of type **"assembly::edge-provider-base::1.0"** with the name **"edgebase"**. The the deployment location is defaulted to **edge**. 

## Instatiate voice network service

Turn on voice service in "core" Openstack location. This will initially stand up a single IPPBX in the scaling group Create an assembly of type **"assembly::provider-voice-service-core::1.0"** with the name **"voice"**

## Validate Service

Create a traffic generator service by instantiating an assembly of type **"assembly::provider-voice-load-generator::1.0"** at deployment location **edge** and give it a name, e.g. SIP1. This will create a SIPP container in the kubernetes environment and send traffic over the provider network to the VoIP gateway in the openstack environment. 

## Trigger a scale 

Create another traffic generator instance by again instantiating an assembly of type **"assembly::provider-voice-load-generator::1.0"** at deployment location **edge** with a different name, .e.g. SIP2. 

This will trigger a scaling event create a new VoIP PBX server in the Openstack core-provider location. 

Delete SIP1 and SIP2 traffic generator instances, which will trigger a scale in request.

## Move Gateway from Openstack to K8s

Upgrade the voice service from **"assembly::provider-voice-service-core::1.0"** to **"assembly::provider-voice-service-edge::1.0"** which will move the gateway from openstack to kubernetes and re-establish all application relationships

Create traffic generator instance as above to validate the service is working. 