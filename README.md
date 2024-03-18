## Goal - create a config generator for 5-stage EVPN Fabric with an IPv6 Underlay

Base the template for a typical campus fabric with the intention of eventually supporting multi-pod architecture, inter-vlan multicast with OISM, IPv4 and IPv6 L3VRF, Type5 routing, dhcp-relay, dhcp-snooping, and anything else I can think of. 

insert diagram

define what to modify in the yaml files to feed into the jinja template
define how to add devices to the list and to generate the configs

also need to create set format versions for some people who prefer it.

need access leaf, spines, super spines(core) and border leaves

I take no responsibility if any of this rendered config even works hah! heck it may not even be good syntax and commit error all over the place