# Linux NFT/Traffic Control k8s Operator

This k8s works in conjuction with Metallb configured in BGP Mode and a Linux Router
to create a LoadBalancer structure for k8s applications.

For more information on [MetalLB](https://metallb.universe.tf)


# How it works

<img src="doc/images/nft.png"></img>

The operator reads the metallb configmap and uses variables in its custom resource defination to
create a nftables configuration and transfers the configuration to the linux router.

When a Network Service is created with a LoadBalancer configured, Metallb allocates an IP address
from its configured pool and advertizes to the router.

The operator watches for the creation of services and updates firewall rules to ensure that only
the specific address and port transit the router.  

If configured, the operator will also apply ingress rate limiting by configured linux
traffic control on the public interface.  By adding an annotation to the Service Metadata
the rate limit will be applied.  


# Installation
TBD



# Configuration examples
TBD