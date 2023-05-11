import requests

url = 'https://ctz.solidwallet.io/api/debug/v3'
payload = {
    "jsonrpc": "2.0",
    "method": "debug_estimateStep",
    "id": 1234,
    "params":{
        "from": "hxe2a1a886fe6618b6702655c46a52fc53f68ef08e",
        "data": {
            "method": "presaleMint",
            "params": {
            "_amount": "1"
            }
        },
        "dataType": "call",
        "nid": "0x1",
        "nonce": "0x1",
        "timestamp": "0x5fb6a63f12ee8",
        "to": "cx546ee1958a1daa64f914c328081e2285ed9973ff",
        "value": "0xd02ab486cedc0000",
        "version": "0x3"
    }
}

req = requests.post(url, json=payload)
print(req.json())