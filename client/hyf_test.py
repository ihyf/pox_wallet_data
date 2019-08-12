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
        self.url_local_flask = "http://localhost:9000/api"
        self.url_local_node = "http://localhost:8889/jsonrpc"
        self.url_wai_flask = "http://39.100.40.109:9000/api"
        self.url_wai_node = "http://39.100.40.109:8889/jsonrpc"

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
        self.send_request(url=self.url_wai, method=method, data=data)

    def test_get_difficulty(self):
        method = "get_difficulty"
        data = {

        }
        self.send_request(url=self.url_wai, method=method, data=data)

    def test_get_coin_supply(self):
        method = "get_coin_supply"
        data = {

        }
        self.send_request(url=self.url_wai, method=method, data=data)

    def test_get_distribution(self):
        method = "get_distribution"
        data = {

        }
        self.send_request(url=self.url_wai, method=method, data=data)

    def test_get_block_count(self):
        method = "get_block_count"
        data = {

        }
        self.send_request(url=self.url_wai, method=method, data=data)

    def test_get_network_hashps(self):
        method = "get_network_hashps"
        data = {

        }
        self.send_request(url=self.url_wai, method=method, data=data)

    def test_get_node_count(self):
        method = "get_node_count"
        data = {

        }
        self.send_request(url=self.url_wai, method=method, data=data)

    def test_get_balance(self):
        method = "get_balance"
        data = {
            "address": "F7WTiJVJNREE14MSVzgjiqFYUNTom7WmVG"
        }
        self.send_request(url=self.url_wai_node, method=method, data=data)

    def test_get_transaction(self):
        method = "get_transaction"
        data = {
            "tx_id": "d701ebbbce03ba7491f920dd2130265bea166ef7d7a39d7a2689813b6c12cc68"
        }
        self.send_request(url=self.url_wai, method=method, data=data)

    def test_get_transactions_by_address(self):
        method = "get_transactions_by_address"
        data = {
            "address": "F7WTiJVJNREE14MSVzgjiqFYUNTom7WmVG"
        }
        self.send_request(url=self.url_wai_flask, method=method, data=data)

    def test_get_info(self):
        method = "get_info"
        data = {
        }
        self.send_request(url=self.url_local_flask, method=method, data=data)

    def test_get_address_utxo(self):
        method = "get_address_utxo"
        data = {
            "address": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK"
        }
        self.send_request(url=self.url_wai_node, method=method, data=data)

    def test_get_transactions(self):
        method = "get_transactions"
        data = {
            "address": "F7WTiJVJNREE14MSVzgjiqFYUNTom7WmVG"
        }
        self.send_request(url=self.url_wai_node, method=method, data=data)

    def test_add_transaction(self):
        method = "add_transaction"
        data = {
            "from_address": "F7WTiJVJNREE14MSVzgjiqFYUNTom7WmVG",
            "to_address": "123456789",
            "tx_id": "tx_id",
            "in_or_out": "out"
        }
        self.send_request(url=self.url_wai_flask, method=method, data=data)

    def test_get_tr_create_time(self):
        method = "get_tr_create_time"
        data = {
            "address": "F7WTiJVJNREE14MSVzgjiqFYUNTom7WmVG"
        }
        self.send_request(url=self.url_wai_flask, method=method, data=data)

    def test_get_flo_price(self):
        method = "get_flo_price"
        data = {
        }
        self.send_request(url=self.url_local_flask, method=method, data=data)
    """axe"""
    def test_get_axe_block(self):
        method = "get_axe_block"
        data = {
        }
        self.send_request(url=self.url_local_flask, method=method, data=data)

    def test_get_axe_balance(self):
        method = "get_axe_balance"
        data = {
            "address": "P9bpHi2xFCMG3N5ZQeryXwV2abyzSC1TZj"
        }
        self.send_request(url=self.url_local_flask, method=method, data=data)

    def test_get_axe_transactions(self):
        method = "get_axe_transactions"
        data = {
            "address": "P9bpHi2xFCMG3N5ZQeryXwV2abyzSC1TZj"
        }
        self.send_request(url=self.url_local_flask, method=method, data=data)

    def test_get_axe_address_utxo(self):
        method = "get_axe_address_utxo"
        data = {
            "address": "P9bpHi2xFCMG3N5ZQeryXwV2abyzSC1TZj"
        }
        self.send_request(url=self.url_local_flask, method=method, data=data)

    def test_get_all_price(self):
        method = "get_all_price"
        data = {
        }
        self.send_request(url=self.url_local_flask, method=method, data=data)

    def test_get_axe_info(self):
        method = "get_axe_info"
        data = {
        }
        self.send_request(url=self.url_local_flask, method=method, data=data)


if __name__ == "__main__":
    hyf = Hyf()

    # hyf.test_my_method()
    # hyf.test_get_difficulty()
    # hyf.test_get_coin_supply()
    # hyf.test_get_distribution()
    # hyf.test_get_info()
    # hyf.test_get_flo_price()
    # hyf.test_get_network_hashps()
    # hyf.test_get_node_count()
    # for i in range(1):
    #     hyf.test_get_address_utxo()
    # hyf.test_get_balance()
    # hyf.test_get_transaction()
    # hyf.test_get_transactions_by_address()
    # hyf.test_get_transactions()
    # hyf.test_add_transaction()
    # hyf.test_get_tr_create_time()

    # axe
    # hyf.test_get_axe_block()
    # hyf.test_get_axe_balance()
    hyf.test_get_axe_transactions()
    # hyf.test_get_axe_address_utxo()
    # hyf.test_get_all_price()
    # hyf.test_get_axe_info()

