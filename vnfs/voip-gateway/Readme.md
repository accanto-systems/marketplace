# Kamailio VoIP Gateway VNF

This VNF packages a [Kamailio SIP Gateway](https://www.kamailio.org/w/) with the LM standard lifecycle API.

Follow the steps below to build VIM images and load the VNF package
* [Build a VIM run time image](#create-the-vim-image)
* [Load VIM image to CICD Hub](#load-the-vim-image-to-cicd-hub)
* [Create VNF package](#push-vnf-package)

## Create the VIM image

To run this VNF an image must be built appropriate for the target VIM. 

### Software dependencies

The following software must be installed to your local machine to create an IP PBX VIM image. 
* [Packer](https://packer.io/)

### Build the image

To deploy to an OpenStack VIM [run the Openstack packer installer](./VNFCs/kamailio-vnfc/VDUs/packer/openstack/Readme.md).

To deploy to a container based VIM [run the docker packer installer](./VNFCs/kamailio-vnfc/VDUs/packer/docker/Readme.md).

## Load the VIM image to CICD Hub

Load the VIM image you created above to the CICD Hub image repository and to your target VIM. You can follow the instructions [here](http://servicelifecyclemanager.com/cicd/upload_images/).

## Push VNF Package

To push the VNF to your target ALM and RM, you must first [download and install LM command line tools](http://servicelifecyclemanager.com/reference/lmctl/). and configure your LM environment. 

Finally you can push your VNF package to your target LM environment, by running the following in the root directory of this project.
```
lmctl project push <YOUR_ENV>
```

The [CICD user guide](http://servicelifecyclemanager.com/cicd/introduction/) has more information on managing VNF packages across LM environments. 