Avoid having 10000s of devices all on the exact same network, we use VLANs to segment them

Imagine we have giant conference room with 300 seat & someone comes in and shouts & everyone hears (ARP).

Instead divide the conference room into smaller rooms, have more meetings.

By default, all X amount of switch ports on a switch are in VLAN #1 until segmenting/creating more VLANs

VLANs are a layer 2 function.. If you connect to a port, your device will be on the vlan in which the port is assigned

Each VLAN likely has its own IP address:

- VLAN1 10.1.0.0
- VLAN2 10.2.0.0
- VLAN3 10.3.0.0

Each VLAN has a unique subnet address

Show vlan brief

Config t

Vlan 2

Assign ports/interfaces:  
 

- Interface config mode
- Switchport access vlan 2

- Any device connecting to a port assigned to vlan 2 - will be on vlan 2

So general process - create VLAN - assign to interface

L2 VLAN aka L2 broadcast domain, if a broadcast is sent, all devices on the VLAN will receive broadcast