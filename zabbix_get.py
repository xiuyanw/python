import requests
import json
url='http://192.168.1.112/api_jsonrpc.php'
headers={'Content-Type':'application/json-rpc'}
data={
    "jsonrpc": "2.0",
    "method": "action.get",
    "params": {
        "output":"extend",
        "selectOperations":"extend",
        "selectRecoveryOperations":"extend",
        "selectFilter":"extend",
        "filter":{
            "eventsource": 1
        }
    },
    "auth":"038e1d7b1735c6a5436ee9eae095879e",
    "id":1
}
r=requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())