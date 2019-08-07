# Building a Kamailio docker image

## Pre-requisites

* Docker running on your local machine

## Create the Kamailio Image

Download [Kamailio](https://www.kamailio.org/pub/kamailio/5.0.2/src/kamailio-5.0.2_src.tar.gz) to voip-gateway/VNFCs/kamailio-vnfc/VDUs/packer/software/ directory.

To build an image in your local registry run the following command
```
packer build build-local.json
```

To build an image and export to your local machine as a saved tar file, configure the export path in **build-and-export.json** file with where you want the image to be exported.  

```
"export_path": "../../../targets/docker/kamailio-vnfc.tar",
```

and run the following packer build command

```
packer build build-export.json
```

To build an image and automatically push it to a registry, update the **build-and-push.json** file with the correct registry information and run the following packer build command.

```
packer build build-local.json
```
