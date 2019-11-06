# Setup LMCTL

Install lmctl on your host machine by running the folowing command:

```
python3 -m pip install lmctl==2.0.7.1
```

Create a file called **lmconfig.yaml** and add the following:

```
dev:
  description: demo environment
  alm:
    ip_address: 192.168.10.5
    port: 8083
    protocol: https
    secure_port: true
    auth_address: 192.168.10.5
    auth_port: 8082
    username: jack
    password: jack
  arm:
    defaultrm:
      ip_address: 192.168.10.5
      port: 31081
      secure_port: True
      onboarding_addr: https://osslm-ansible-rm:8443
```

In a command shell you need to set the following environment variable to point to this file. 
```
export LMCONFIG=~/lmconfig.yaml
```
