import requests
from rich import print
url = "https://n149.meraki.com/api/v1/organizations/549236/networks/L_646829496481105433/devices"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '37278cb621acc170282a8352b9214ed5f128bbe5'
}

response = requests.get( url, headers=headers, data=payload)

print(response.json())
