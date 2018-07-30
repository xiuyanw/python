import requests
import json
url='http://192.168.1.112/api_jsonrpc.php'
headers={'Content-Type':'application/json-rpc'}
data={
    "jsonrpc": "2.0",
    "method": "user.create",
    "params": {
        "alias": "John",
        "passwd": "Doe123",
        "usrgrps": [
            {
                "usrgrpid": "7"
            }
        ],
        "user_medias": [
            {
                "mediatypeid": "1",
                "sendto": "support@company.com",
                "active": 0,
                "severity": 63,
                "period": "1-7,00:00-24:00"
            }
        ]
    },
    "auth": "3b3294c39803ca8a95f400be2b26b200",
    "id": 1

}
r=requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())