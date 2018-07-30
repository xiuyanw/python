import requests
import json
url='http://192.168.1.112/api_jsonrpc.php'
headers={'Content-Type':'application/json-rpc'}
data={
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "python linux server",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.1.112",
                "dns": "192.168.1.254",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "4"
            }
        ],
        # "templates": [
        #     {
        #         "templateid": "20045"
        #     }
        # ],
        # "inventory_mode": 0,
        # "inventory": {
        #     "macaddress_a": "01234",
        #     "macaddress_b": "56768"
        # }
    },
    "auth": "3b3294c39803ca8a95f400be2b26b200",
    "id": 1
}
r=requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())