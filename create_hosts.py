import requests
import json
def create_hosts(name,ip):
    url='http://192.168.1.112/api_jsonrpc.php'
    headers={'Content-Type':'application/json-rpc'}
    data={
        "jsonrpc":"2.0",
        "method":"host.create",
        "params":{
            "host":name,
            "interfaces":[
                {
                    "type":1,
                    "main":1,
                    "useip":1,
                    "ip":ip,
                    "dns":"192.168.1.254",
                    "port":10050
                }
            ],
            "groups": [
                {
                    "groupid": "2"
                }
            ],
        },
        "auth":"84951c53a38e6fd8708f0a6e3f9f9734",
        'id':1,
    }
    r=requests.post(url,headers=headers,data=json.dumps(data))
    return  r.json()
if __name__ == '__main__':
    adict={
        'b2':'192.168.1.183',"b5":"192.168.1.195",
        "b3":"192.168.1.186","b6":"192.168.1.194",
        "b4":"192.168.1.173"}
    for key in adict:
        print(create_hosts(key,adict[key]))
