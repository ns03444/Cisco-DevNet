import requests
import json
from rich import print


# set up connection parameters in a dictionary
router = {"ip": "devnetsandboxiosxe.cisco.com", "port": "443",
          "user": "admin", "password": "C1sco12345"}

# set REST API headers
headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}

response = requests.get(f"https://{router['ip']}:{router['port']}/restconf/data/netconf-state/capabilities?", 
                        headers=headers, 
                        auth=(router['user'], router['password']), 
                        verify=False)
print(response.json())

with open('output/capabilities.json', 'w') as f:
    f.write(json.dumps(response.json()))

