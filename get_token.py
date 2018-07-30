import requests
import json
url='http://192.168.1.112/api_jsonrpc.php'
headers={'Content-Type':'application/json-rpc'}
data={
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "admin",
        "password": "zabbix"
    },
    "id": 1
}
r=requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())