# coding:utf-8
import time
import json
import requests
from my_dispatcher import api_add, api
import asyncio
import aiohttp
from lxml import etree
import config
from util.check_fuc import check_kv
from util.db_redis import redis_store
from util.db_tools_func import add_transaction_db, get_transaction_db

sema = asyncio.Semaphore(3)
event_loop = asyncio.get_event_loop()


async def get_data(url):
    async with aiohttp.request('GET', url) as r:
        if r.status == 200:
            data = await r.json(content_type=None)
            return data
        else:
            # todo log error
            return [0, 0, 0, 0, 0]


@api_add
def get_difficulty(*args, **kwargs):
    """获取难度值"""
    r = requests.get("http://network.flo.cash/api/getdifficulty")

    if r.status_code != 200:
        return {"error": "get difficulty fail"}

    if r.json() != "":
        difficulty = str(r.json())

    return {
        "difficulty": difficulty or ""
    }


@api_add
def get_coin_supply(*args, **kwargs):
    """获取当前硬币总供给量"""
    r = requests.get("http://network.flo.cash/ext/getmoneysupply")
    if r.status_code != 200:
        return {"error": "get coin supply fail"}

    if r.json() != "":
        coin_supply = str(r.json())

    return {
        "coin_supply": coin_supply or ""
    }


@api_add
def get_network_hashps(*args, **kwargs):
    """全网算力"""
    r = requests.get("http://network.flo.cash/api/getnetworkhashps")
    if r.status_code != 200:
        return {"error": "get network hashps fail"}

    if r.json() != "":
        network_hashps = str(r.json()*pow(10, -9))[0:8] + " GH/s"

    return {
        "network_hashps": network_hashps or ""
    }


@api_add
def get_distribution(*args, **kwargs):
    """获取财富分配"""
    r = requests.get("http://network.flo.cash/ext/getdistribution")
    if r.status_code != 200:
        return {"error": "get coin supply fail"}

    if r.json() != "":
        distribution = str(r.json())

    return {
        "distribution": distribution or {}
    }


@api_add
def get_info(*args, **kwargs):
    """获取当前块数"""
    try:
        flo_info = redis_store.get("flo_info")
        if flo_info:
            return json.loads(flo_info)
        url = ["http://network.flo.cash/api/getdifficulty",
               "http://network.flo.cash/ext/getmoneysupply",
               "http://network.flo.cash/api/getblockcount",
               "http://network.flo.cash/api/getnetworkhashps",
               "http://network.flo.cash/api/getconnectioncount"]
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        tasks = [get_data(u) for u in url]
        results = loop.run_until_complete(asyncio.gather(*tasks))
        info = {
            "difficulty": str(results[0]),
            "coin_supply": str(results[1]),
            "block_count": str(results[2]),
            "network_hashps": str(results[3]*pow(10, -9))[0:8] + " GH/s",
            "node_count": str(results[4]),
            "total": "160000000"

        }
        redis_store.set("flo_info", json.dumps(info), config.redis_expire_time)
        return info
    except Exception as e:
        return {
            "difficulty": "0",
            "coin_supply": "0",
            "block_count": "0",
            "network_hashps": "0 GH/s",
            "node_count": "0",
            "total": "160000000"
        }


@api_add
def get_node_count(*args, **kwargs):
    """获取节点数"""
    r = requests.get("http://network.flo.cash/api/getconnectioncount")
    if r.status_code != 200:
        return {"error": "get node count fail"}

    if r.json() != "":
        node_count = str(r.json())

    return {
        "node_count": node_count or ""
    }


@api_add
def get_transaction(*args, **kwargs):
    """通过txid 获取交易详情"""
    tx_id = kwargs.get("tx_id", "")
    if tx_id == "":
        return {"error": "tx_id is null"}
    r = requests.get(f"http://network.flo.cash/api/getrawtransaction?txid={tx_id}&decrypt=1")
    if r.status_code != 200:
        return {"error": "get transaction fail"}

    if r.json() != "":
        transaction = r.json()

    return {
        "transaction": transaction or ""
    }


@api_add
def get_balance(*args, **kwargs):
    """获取余额"""
    address = kwargs.get("address", "")
    r = requests.get(f"http://network.flo.cash/ext/getbalance/{address}")
    if r.status_code != 200:
        return {"error": "get balance fail"}

    if r.json() != "":
        balance = str(r.json())

    return {
        "balance": balance or ""
    }


@api_add
def get_transactions_by_address(*args, **kwargs):
    """获取交易记录"""
    address = kwargs.get("address", "")
    r = requests.get(f"http://network.flo.cash/ext/getaddress/{address}")
    if r.status_code != 200:
        return {"error": "get_transactions_by_address fail"}

    if r.json() != "":
        info = r.json()

    return {
        "info": info or ""
    }


@api_add
def get_all_price(*args, **kwargs):
    """获取flo axe 价格"""
    try:
        r = requests.get("https://www.feixiaohao.com/currencies/florincoin/")
        selector = etree.HTML(r.text)
        flo_rmb = selector.xpath("//span[@class='convert']")[0].text
        flo_usd = selector.xpath("//span[@class='convert']")[1].text
        flo_btc = selector.xpath("//span[@class='convert']")[2].text
        flo = {
            "flo_rmb": flo_rmb,
            "flo_usd": flo_usd,
            "flo_btc": flo_btc
        }
    except Exception as e:
        flo = {
            "flo_rmb": "0",
            "flo_usd": "0",
            "flo_btc": "0"
        }

    try:
        r = requests.get("https://www.feixiaohao.com/currencies/axe/")
        selector = etree.HTML(r.text)
        axe_rmb = selector.xpath("//span[@class='convert']")[0].text
        axe_usd = selector.xpath("//span[@class='convert']")[1].text
        axe_btc = selector.xpath("//span[@class='convert']")[2].text
        axe = {
            "axe_rmb": axe_rmb,
            "axe_usd": axe_usd,
            "axe_btc": axe_btc
        }
    except Exception as e:
        axe = {
            "axe_rmb": "0",
            "axe_usd": "0",
            "axe_btc": "0"
        }

    return {
        "flo": flo,
        "axe": axe
    }


@api_add
def add_transaction(**kwargs):
    necessary_keys = ["from_address", "to_address", "tx_id", "in_or_out"]
    check = check_kv(kwargs, necessary_keys)
    if check != "success":
        return {
            "error": check
        }

    from_address = kwargs.get("from_address")
    to_address = kwargs.get("to_address")
    tx_id = kwargs.get("tx_id")
    in_or_out = kwargs.get("in_or_out")
    time_stamp =time.time()
    tr = add_transaction_db(from_address, to_address, tx_id, in_or_out, time_stamp)
    if not tr:
        return {
            "error": "add transaction fail",
            "code": -40000
        }
    return {
        "msg": "add transaction success",
        "code": 200
    }


@api_add
def get_tr_create_time(**kwargs):
    necessary_keys = ["address"]
    check = check_kv(kwargs, necessary_keys)
    if check != "success":
        return {
            "error": check
        }
    address = kwargs.get("address")
    tr = get_transaction_db(address)
    if not tr:
        return {
            "msg": True
        }
    if time.time()-tr.time_stamp > 60:
        return {
            "msg": True
        }
    else:
        return {
            "msg": False
        }

