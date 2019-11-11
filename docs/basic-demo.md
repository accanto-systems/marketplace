# Single VIM Demonstration Scenario

The single voice service scenario is as follows:
1. Turn on base shared infrastructure by creating an Assembly of type **"assembly::jumphost-base::1.0"** with the name **"base"**
2. Turn on voice service in "core" Openstack location. This will initially stand up a single IPPBX in the scaling group Create an assembly of type **"assembly::jumphost-voice-service::1.0"** with the name **"voice"**
3. Run SIPP traffic simulator by creating an Assembly of type **"assembly::jumphost-voice-load-generator::1.0"** with the name **"sipp1"**
4. Run another SIPP traffic simulator creating an Assembly of type **"assembly::jumphost-voice-load-generator::1.0"** with the name **"sipp2"**, this should trigger a scaling event
5. Kill an IPPBX virtual machine in Openstack which will trigger a healing event
