# Single VIM Demonstration Scenario

The following steps demonstrate the behaviour use cases from the earlier introduction.

## Instantiate site shared infrastructure

In the LM UI, create an Assembly of type **"assembly::jumphost-base::1.0"** with the name **"base"**. This will create site shared management networks and security groups. 

## Instatiate voice network service

Create an assembly of type **"assembly::jumphost-voice-service::1.0"** with the name **"voice"**, accepting all default properties describing locations and the name of the site infrastructure assembly instance. 

This will initially stand up a gateway, and a single VoIP PBX in the scaling group. All VNFs will be attached to the shared management infrastucture created in the **base** assembly instance.

## Validate Service

Run a SIPP traffic simulator by creating an Assembly of type **"assembly::jumphost-voice-load-generator::1.0"** with the name **"sipp1"**. 

## Trigger a scale 

Run another SIPP traffic simulator by again creating an Assembly of type **"assembly::jumphost-voice-load-generator::1.0"** with the name **"sipp2"**. This will generate a load metric from the gateway that will cross a scaling threshold and trigger the instantiation of a new VoIP PBX server. 

## Kill a VoIP PBX virtual machine

In the Openstack UI, kill a VoIP Server VM. After 3 periods of missing integrity metrics, a healing event will be triggered in the lifecycle manager. This will bring the VoIP PBX instance through a set of opinionated patterns until the VoIP network service is brought back into an overall state of Active.  


## Using Behaviour Runner to Automate scale testing

Clean up environment by doing XYZ

...

## Using behaviour running in CICD

...