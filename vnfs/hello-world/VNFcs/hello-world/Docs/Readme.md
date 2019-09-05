# Hello World Example

This basic VNFC example deploys a single Compute VM on Openstack with a Private IP address.

# Usage

Ensure you have a suitable image and key setup in Openstack. By default this VNFC expects an image called `xenial-server-cloudimg-amd64-disk1` and a key called `helloworld` but these may be changed using the inputs of the tosca template. 

# Deploy on Openstack

## Translate Tosca to Heat

Translate the Tosca template to Heat using the [heat-translator](https://github.com/openstack/heat-translator)

```
cd helloworld/Definitions/infrastructure 
python3 heat_translator.py --template-file=helloworld.yaml --output hot_helloworld.yaml
```

## Create with Heat

To create from the Heat template use the `stack create` command from the Openstack client:

```
openstack stack create -t hot_helloworld.yaml helloworld
```

Check the status of your stack using `list` and `show` commands:

```
openstack stack list
openstack stack show helloworld
```

