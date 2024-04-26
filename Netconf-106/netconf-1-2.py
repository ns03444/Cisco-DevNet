from ncclient import manager
import json
# logging.basicConfig(level=logging.DEBUG)
# https://github.com/DataKnox/CodeSamples/blob/master/Python/Networking/IOS-XE/
router = {"host": "sandbox-iosxr-1.cisco.com", "port": 830,
          "username": "admin", "password": "C1sco12345"}

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)