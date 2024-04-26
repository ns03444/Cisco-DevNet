from ncclient import manager
from pprint import pprint
import xmltodict
import xml.dom.minidom
from router_info import router


# https://github.com/DataKnox/CodeSamples/blob/master/Python/Networking/IOS-XE/
# Two containers in the YANG model - ietf-interfaces.
# 1. interfaces - get config data
# 2. interfaces-state - get operational state data

netconf_filter = """
 <filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Loopback50</name>
    </interface>
  </interfaces>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Loopback50</name>
    </interface>
  </interfaces-state>
</filter>
"""

# with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
#     for capability in m.server_capabilities:
#         print('*' * 50)
#         print(capability)

#     # Get config or operational data with get_config, additionally pass an optional filter.
#     interface_netconf = m.get_config('running', netconf_filter)
#     print('getting running config')
#     xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
#     print(xmlDom.toprettyxml(indent="  "))
#     print('*' * 25 + 'Break' + '*' * 50)
#     m.close_session()

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    # get the running config on the filtered out interface
    print('Connected')
    interface_netconf = m.get(netconf_filter)
    print('getting running config')
    print(interface_netconf.xml)
    print(dir(interface_netconf))
# below, xml is a property of interface_conf
interface_python = xmltodict.parse(interface_netconf.xml)[
    "rpc-reply"]["data"]
pprint(interface_python)
name = interface_python['interfaces']['interface']['name']['#text']
print(name)
# # XMLDOM for formatting output to xml
# xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
# print(xmlDom.toprettyxml(indent="  "))
# print('*' * 25 + 'Break' + '*' * 50)
# # XMLTODICT for converting xml output to a python dictionary
# interface_python = xmltodict.parse(interface_netconf.xml)[
#     "rpc-reply"]["data"]
# pprint(interface_python)
# name = interface_python['interfaces']['interface']['name']['#text']
# print(name)

# config = interface_python["interfaces"]["interface"]
# op_state = interface_python["interfaces-state"]["interface"]

# print("Start")
# print(f"Name: {config['name']['#text']}")
# print(f"Description: {config['description']}")
# print(f"Pakcets In {op_state['statistics']['in-unicast-pkts']}")