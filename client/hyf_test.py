import time
import json
import requests
import base64

class Hyf(object):
    def __init__(self):
        self.appid = "hyf_app"
        self.headers = {
            "content-type": "application/json",
            "Authorization": "flo test"
        }
        self.payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "",
            "params": {

            }
        }
        self.url_local = "http://localhost:9000/api"
        self.url_wai = "http://149.28.56.184:9000/api"
    
    def send_request(self, url, method, data):
        self.payload["method"] = method
        self.payload["params"] = data
        print(url)
        print(self.payload)
        response = requests.post(url=url, data=json.dumps(self.payload), headers=self.headers)
        print(response.json())

    def test_my_method(self):
        method = "my_method"
        data = {
            "time": time.time()
        }
        self.send_request(url=self.url_local, method=method, data=data)

    def test_get_difficulty(self):
        method = "get_difficulty"
        data = {

        }
        self.send_request(url=self.url_wai, method=method, data=data)

    def test_get_coin_supply(self):
        method = "get_coin_supply"
        data = {

        }
        self.send_request(url=self.url_local, method=method, data=data)

    def test_get_distribution(self):
        method = "get_distribution"
        data = {

        }
        self.send_request(url=self.url_local, method=method, data=data)

    def test_get_block_count(self):
        method = "get_block_count"
        data = {

        }
        self.send_request(url=self.url_local, method=method, data=data)

    def test_get_network_hashps(self):
        method = "get_network_hashps"
        data = {

        }
        self.send_request(url=self.url_local, method=method, data=data)

    def test_get_node_count(self):
        method = "get_node_count"
        data = {

        }
        self.send_request(url=self.url_local, method=method, data=data)

    def test_get_balance(self):
        method = "get_balance"
        data = {
            "address": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK"
        }
        self.send_request(url=self.url_local, method=method, data=data)

    def test_get_transaction(self):
        method = "get_transaction"
        data = {
            "tx_id": "d701ebbbce03ba7491f920dd2130265bea166ef7d7a39d7a2689813b6c12cc68"
        }
        self.send_request(url=self.url_local, method=method, data=data)

    def test_get_transactions_by_address(self):
        method = "get_transactions_by_address"
        data = {
            "address": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK"
        }
        self.send_request(url=self.url_local, method=method, data=data)


if __name__ == "__main__":
    hyf = Hyf()

    # hyf.test_my_method()
    # hyf.test_get_difficulty()
    # hyf.test_get_coin_supply()
    # hyf.test_get_distribution()
    # hyf.test_get_block_count()
    # hyf.test_get_network_hashps()
    # hyf.test_get_node_count()
    # hyf.test_get_balance()
    # hyf.test_get_transaction()
    # hyf.test_get_transactions_by_address()
    v = base64.encode("1", "utf-8")
    print(v)
    b'\xa3\xd1\x85{\xe5\xb2;M;\x89\xb8\xc9o\x02\xf6\x03D \xb8\x16\xe6\x96VX\x17\xa5\xdaE\xac_\x98\xdb\xb6\x01\xab\xe9\x16\x81'

