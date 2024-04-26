from ncclient import manager
from rich import print

router = {"ip": "devnetsandboxiosxe.cisco.com", "port": 830,
          "user": "admin", "password": "C1sco12345"}

with manager.connect(host=router["ip"], port=router["port"], username=router["user"], password=router["password"], hostkey_verify=False) as m:
    scmhema = m.get_schema("openconfig-lldp-types")
    print(scmhema)

    with open ('aaa-types.yang', 'w') as f:
        f.write(str(scmhema))