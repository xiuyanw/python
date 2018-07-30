import requests
import json
url='http://192.168.1.112/api_jsonrpc.php'
headers={'Content-Type':'application/json-rpc'}
data={
    "jsonrpc": "2.0",
    "method": "hostgroup.create",
    "params": {
        "name": "Linux wang"
    },
    "auth": "3b3294c39803ca8a95f400be2b26b200",
    "id": 1
}
r=requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())