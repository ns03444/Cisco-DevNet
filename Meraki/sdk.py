from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json
from pprint import pprint


# CREATE Connection Object
x_cisco_meraki_api_key = '37278cb621acc170282a8352b9214ed5f128bbe5'  # Demo DevNet Sandbox
meraki = MerakiSdkClient(x_cisco_meraki_api_key)
print(dir(meraki))
print(dir(meraki.http_servers.get_network_http_servers('549236')))
# GET Org devices
# orgs = meraki.organizations.get_organizations()
# print(json.dumps(orgs, indent=2, sort_keys=True))
# pprint(orgs)


# Set OrgId
# for org in orgs:
#     if org['name'] == "DevNet Sandbox":
#         orgId = org['id']

# # Get Networks in Org
# params = {}
# params['organization_id'] = orgId
# networks = meraki.networks.get_organization_networks(params)
# pprint(networks)

# # Set NetworkId
# for network in networks:
#     if network['name'] == "DevNet Always On Read Only":
#         netId = network['id']
# # print(netId)

# # GET VLANS
# vlans = meraki.vlans.get_network_vlans(netId)

# print(vlans)
# vlan = vlans[0]
# # CHANGE VLAN NAME HERE
# vlan['name'] = 'Default'


# updatedVlan = {}
# updatedVlan['network_id'] = netId
# updatedVlan['vlan_id'] = vlan['id']
# updatedVlan['update_network_vlan'] = vlan
# # pprint(updatedVlan)
# result = meraki.vlans.update_network_vlan(updatedVlan)

# # VERIFY
# vlans = meraki.vlans.get_network_vlans(netId)
# pprint(vlans)