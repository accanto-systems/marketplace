# Voice Overlay Networks

This network service creates two networks for use within the voice service.  These are mgmt_network shared by all VNFs and data_network that is used as the front-end network that traffic will flow into the voice service.

A typical way of using this within another network service using a reference:

---
      overlay_networks:
        type: assembly::voice-overlay-networks::1.0
        properties:
          name:
            value: ${overlay_networks_name}
          deploymentLocation:
            value: ${deploymentLocation}
          resourceManager:
            value: ${resourceManager}
---

For a vnf instance to use a network referenced by the above reference object the following property reference would be used:

---
      mgmt_network:
        value: ${overlay_networks.mgmt_network}
      data_network:
        value: ${overlay_networks.data_network}
---