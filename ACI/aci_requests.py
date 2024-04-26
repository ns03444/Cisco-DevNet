import requests
import json
# Knox Hutchinson
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
####### LOGIN ###########
url = "https://sandboxapicdc.cisco.com:443/api/aaaLogin.json"

payload = {
    "aaaUser": {
        "attributes": {
            "name": "admin",
            "pwd": "!v3G@!4@Y"
        }
    }
}
headers = {
    'Content-Type': "application/json"
}

response = requests.post(url, data=json.dumps(
    payload), headers=headers, verify=False).json()

# print(json.dumps(response, indent=2, sort_keys=True))

# PARSE TOKEN AND SET COOKIE
token = response['imdata'][0]['aaaLogin']['attributes']['token']
cookie = {}
cookie['APIC-cookie'] = token


######### GET APN ##############
# GET Tenants
# everything under uni -> is a class - usually tenants
url = "https://sandboxapicdc.cisco.com:443/api/class/fvTenant.json"



url = "https://sandboxapicdc.cisco.com:443/api/node/mo/uni/tn-xandi.json?"

headers = {
    'cache-control': "no-cache"
}

get_response = requests.get(
    url, headers=headers, cookies=cookie, verify=False).json()

print(json.dumps(get_response, indent=2, sort_keys=True))