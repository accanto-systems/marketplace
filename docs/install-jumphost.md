# Basic Service Setup

## Setup virtual data centre and VIMs

Create the virtual infrastructure and VIMs by cloning the NFVI underlay project as follows:

```
git clone https://github.com/accanto-systems/nfvi-environment.git
```

Follow instructions in nfvi-environment project Readme.md to configure and setup your virtual NFVI environment. 

## Setup LM

If you are using LM AIO project to install LM, then follow the following [guide](/docs/install-AIO.md).

## Configure locations in LM

Once AIO is up and running, log onto LM at https://192.168.10.5:8082 and create the following locations. 

### Add openstack Core location

Add a location called "core" with resource manager "defaultRM" and infrastructure type "Openstack" and provide the following properties

```
os_auth_url: "http://192.168.10.10:5000/v3"
os_projectname: admin
os_username: admin
os_password: password
almip: 10.0.30.5
```

## Load VNFs and Network Services

As required, build VNF images as per each VNF readme and load into target VIM.

[Install LMCTL](/docs/install-lmctl.md) and load the VNFs and Network services into LM by running the following commands. 

```
cd marketplace
./load.sh push dev
```

You are now ready to run through the [basic demo scenario](/docs/basic-demo.md). 