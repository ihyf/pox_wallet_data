import threading
import time
import json
import requests
import base64
from multiprocessing import Pool
import os, time, random


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
        # print(url)
        # print(self.payload)
        response = requests.post(url=url, data=json.dumps(self.payload), headers=self.headers)
        d = response.json().get("result")
        if d:
            if isinstance(d, dict):
                print(d["error"])

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
            "address": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK"
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
            "address": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK"
        }
        self.send_request(url=self.url_wai, method=method, data=data)

    def test_get_info(self):
        method = "get_info"
        data = {
        }
        self.send_request(url=self.url_wai, method=method, data=data)

    def test_lllll(self):
        method = "lllll"
        data = {
            "ihyf": 123
        }
        self.send_request(url="http://127.0.0.1:8889/jsonrpc", method=method, data=data)

    def start_thread(self, func, threading_num, args):
        t_list = []
        for i in range(10):
            t = threading.Thread(target=func, args=args)
            t.start()
            t_list.append(t)
        for t in t_list:
            t.join()


if __name__ == '__main__':
    hyf = Hyf()
    import multiprocessing as mp
    processes_num = os.cpu_count()
    threading_num = 700
    times = 500
    p = mp.Pool(processes=processes_num)  # 创建5条进程
    bingfa = processes_num * threading_num
    task_num = times * threading_num
    print("bingfa:" + str(bingfa))
    print("task_num:" + str(task_num))

    start = time.time()
    for i in range(times):
        p.apply_async(hyf.start_thread, args=(hyf.test_get_balance, threading_num, ()))  # 向进程池添加任务

    p.close()  # 关闭进程池，不再接受请求
    p.join()  # 等待所有的子进程结束
    end = time.time()
    time_total = end - start
    print(time_total)





    # hyf.test_my_method()
    # hyf.test_get_difficulty()
    # hyf.test_get_coin_supply()
    # hyf.test_get_distribution()
    # hyf.test_get_info()
    # hyf.test_get_network_hashps()
    # hyf.test_get_node_count()
    # hyf.test_get_balance()
    # hyf.test_get_transaction()
    # hyf.test_get_transactions_by_address()


