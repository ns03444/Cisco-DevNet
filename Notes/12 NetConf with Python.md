[https://github.com/YangModels/yang/tree/main](https://github.com/YangModels/yang/tree/main)

[https://github.com/DataKnox/CodeSamples/blob/master/Python/Networking/IOS-XE/](https://github.com/DataKnox/CodeSamples/blob/master/Python/Networking/IOS-XE/)

[https://datatracker.ietf.org/doc/html/rfc6241](https://datatracker.ietf.org/doc/html/rfc6241)

[https://datatracker.ietf.org/doc/html/rfc6020](https://datatracker.ietf.org/doc/html/rfc6020)

Network Configuration Protocol (NETCONF)Abstract

The Network Configuration Protocol (NETCONF) defined in this document  
   provides mechanisms to install, manipulate, and delete the  
   configuration of network devices.  It uses an Extensible Markup  
   Language (XML)-based data encoding for the configuration data as well  
   as the protocol messages.  The NETCONF protocol operations are  
   realized as remote procedure calls (RPCs).  This document obsoletes   [RFC 4741](https://datatracker.ietf.org/doc/html/rfc4741).

From <[https://datatracker.ietf.org/doc/html/rfc6241](https://datatracker.ietf.org/doc/html/rfc6241)>

               YANG - A Data Modeling Language forthe Network Configuration Protocol (NETCONF)Abstract

YANG is a data modeling language used to model configuration and  
   state data manipulated by the Network Configuration Protocol  
   (NETCONF), NETCONF remote procedure calls, and NETCONF notifications.

From <[https://datatracker.ietf.org/doc/html/rfc6020](https://datatracker.ietf.org/doc/html/rfc6020)>

1. Using the ncclient library which uses the netconf protocol to connect to a remote network device

1. Note, netconf is just SSH, which is just TCP with encryption

Your explanation is generally correct, but it needs a bit more clarity and accuracy. Let's refine it:

1. **Using the ncclient Library with Netconf Protocol**:

   The ncclient library is a Python library that facilitates communication with network devices using the Netconf protocol. Netconf, or Network Configuration Protocol, is indeed a standardized protocol for managing network devices. It operates over secure transport layers like SSH or TLS and facilitates structured data exchange, typically using XML.

   Netconf provides capabilities for configuring, managing, and monitoring network devices remotely. Through the ncclient library, Python scripts can establish Netconf sessions with remote devices, allowing for tasks such as configuration changes, software updates, and data retrieval.

   **Note on Netconf as SSH**:

   While it's true that Netconf sessions are often secured using SSH, Netconf itself is not SSH. Netconf operates over SSH, providing a secure channel for communication between the client and the server. SSH ensures confidentiality and integrity of data exchanged during the Netconf session. However, Netconf goes beyond SSH in providing a standardized protocol specifically tailored for network device management, including features like transaction support, structured data exchange, and standardized operations.

   In summary, while Netconf sessions are often established over SSH, Netconf itself represents a distinct protocol designed for network management tasks, offering features and capabilities beyond those provided by SSH alone

NEED TO REVIEW YANG CATALOGS/CONTAINERS