import time

import requests
import json


class Hyf(object):
    def __init__(self):
        self.appid = "hyf_app"
        # self.appid = "c66816dbb90591b1a1740ea0dc9b602e"
        self.headers = {
            "content-type": "application/json",
            "Authorization": "poa test"
        }
        self.payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "",
            "params": {
                "appid": self.appid,
                "sign": "",
                "data": {
                
                }
            }
        }
        self.url_local = "http://localhost:9000/api"
    
    def send_request(self, url, method, data):
        self.payload["method"] = method
        self.payload["params"]["sign"] = self.ec_cli.sign_str(data)
        self.payload["params"]["data"] = self.ec_srv.encrypt_str(data)
        
        response = requests.post(url=url, data=json.dumps(self.payload), headers=self.headers)
        if isinstance(response, bytes):
            response = response.decode()
        else:
            response = response.json()
        print(response)
        ddata = self.ec_cli.decrypt(response["result"]["data"])
        print(ddata)
        print(self.ec_srv.verify(ddata, response["result"]["sign"]))

    def test_my_method(self):
        method = "my_method"
        data = {
            "time": time.time()
        }
        self.send_request(url=self.url_neiwang, method=method, data=data)


if __name__ == "__main__":
    hyf = Hyf()
    # hyf.test_add_master_contract()
    # hyf.test_deploy_contract()
    # hyf.test_use_contract()
    # hyf.test_create_account()
    # hyf.test_get_balance()
    hyf.test_send_transaction()
    # hyf.test_add_master_contract()
