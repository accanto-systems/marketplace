# Building an IP PBX docker image

## Pre-requisites

* Docker running on your local machine

## Create the IP PBX Image

Download [Asterisk](https://downloads.asterisk.org/pub/telephony/asterisk/old-releases/asterisk-14.7.8.tar.gz) to **ip-pbx/VNFCs/asterisk-vnfc/VDUs/packer/software/** directory.

To build an image in your local registry run the following command
```
packer build build-local.json
```

To build an image and export to your local machine as a saved tar file, configure the export path in **build-and-export.json** file with where you want the image to be exported.  

```
"export_path": "../../../targets/docker/ip-pbx.tar",
```

and run the following packer build command

```
packer build build-export.json
```

To build an image and automatically push it to a registry, update the **build-and-push.json** file with the correct registry information and run the following packer build command.

```
packer build build-local.json
```
