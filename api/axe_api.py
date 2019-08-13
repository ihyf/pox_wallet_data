# coding:utf-8
import time
import json
import requests
from my_dispatcher import api_add, api
import asyncio
import aiohttp
import config
from lxml import etree
from api.flo_api import sema, event_loop, get_data
from util.check_fuc import check_kv
from util.db_redis import redis_store
from util.db_tools_func import add_transaction_db, get_transaction_db
from util.oip_tools import get_axe_oip


@api_add
def get_axe_block(*args, **kwargs):
    necessary_keys = ["the_hash"]
    check = check_kv(kwargs, necessary_keys)
    if check != "success":
        return {
            "error": check
        }
    the_hash = kwargs.get("the_hash")
    oip = get_axe_oip()
    block = oip.get_block(the_hash=the_hash)
    return {
        "block": block
    }


@api_add
def get_axe_balance(*args, **kwargs):
    necessary_keys = ["address"]
    check = check_kv(kwargs, necessary_keys)
    if check != "success":
        return {
            "error": check
        }
    address = kwargs.get("address")
    oip = get_axe_oip()
    balance = oip.getAddressProperties(address, properties="balance")*pow(10, -8)
    return {
        "balance": balance
    }


@api_add
def get_axe_transactions(*args, **kwargs):
    necessary_keys = ["address"]
    check = check_kv(kwargs, necessary_keys)
    if check != "success":
        return {
            "error": check
        }
    address = kwargs.get("address")
    oip = get_axe_oip()
    transactions = oip.getTransactionsForAddress(address)
    txs = []
    for t in transactions["txs"]:
        in_or_out = "out"
        d = {}
        if t["version"] == 3:
            continue
        vin_addrs = [vin["addr"] for vin in t["vin"]]
        vout_addrs = [vout["scriptPubKey"]["addresses"][0] for vout in t["vout"]]
        d["txid"] = t["txid"]
        d["fees"] = t["fees"]

        if address in vin_addrs and address not in vout_addrs:
            in_or_out = "out"
            for i in t["vin"]:
                if address == i["addr"]:
                    value = i["value"]
            from_address = address
            to_address = vout_addrs[0]
        elif address in vin_addrs and address in vout_addrs:
            in_or_out = "out"
            for i in t["out"]:
                if address != i["scriptPubKey"]["addresses"][0]:
                    value = i["value"]
            from_address = address
            to_address = vout_addrs[0]
        else:
            in_or_out = "in"
            for i in t["vout"]:
                if address == i["scriptPubKey"]["addresses"][0]:
                    value = i["value"]
            from_address = vin_addrs[0]
            to_address = address
        d["value"] = value
        d["in_or_out"] = in_or_out
        d["time"] = t["time"]
        d["blocktime"] = t["blocktime"]
        d["from_address"] = from_address
        d["to_address"] = to_address
        txs.append(d)

    return {
        "txs": txs
    }


@api_add
def get_axe_address_utxo(*args, **kwargs):
    necessary_keys = ["address"]
    check = check_kv(kwargs, necessary_keys)
    if check != "success":
        return {
            "error": check
        }
    address = kwargs.get("address")
    oip = get_axe_oip()
    utxo = oip.get_address_utxo(address)
    return {
        "utxo": utxo
    }


@api_add
def broadcast_axe_raw_hex(*args, **kwargs):
    necessary_keys = ["hex"]
    check = check_kv(kwargs, necessary_keys)
    if check != "success":
        return {
            "error": check
        }
    hex = kwargs.get("hex")
    oip = get_axe_oip()
    _, tx = oip.broadcast_raw_transaction(hex)
    if not _:
        return {
            "error": tx
        }
    return {
        "tx": tx
    }


# @api_add
# def get_axe_price(*args, **kwargs):
#     """获取axe价格"""
#     try:
#         r = requests.get("https://www.feixiaohao.com/currencies/axe/")
#         selector = etree.HTML(r.text)
#         axe_rmb = selector.xpath("//span[@class='convert']")[0].text
#         axe_usd = selector.xpath("//span[@class='convert']")[1].text
#         axe_btc = selector.xpath("//span[@class='convert']")[2].text
#         return {
#             "axe_rmb": axe_rmb,
#             "axe_usd": axe_usd,
#             "axe_btc": axe_btc
#         }
#     except Exception as e:
#         return {
#             "axe_rmb": "0",
#             "axe_usd": "0",
#             "axe_btc": "0"
#         }


@api_add
def get_axe_info(*args, **kwargs):
    """获取axe当前 info"""
    try:
        axe_info = redis_store.get("axe_info")
        if axe_info:
            return json.loads(axe_info)
        url = ["https://axe-explorer.arcpool.com/api/getdifficulty",
               "https://axe-explorer.arcpool.com/ext/getmoneysupply",
               "https://axe-explorer.arcpool.com/api/getblockcount",
               "https://axe-explorer.arcpool.com/api/getnetworkhashps",
               "https://axe-explorer.arcpool.com/api/getconnectioncount"]
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        tasks = [get_data(u) for u in url]
        results = loop.run_until_complete(asyncio.gather(*tasks))
        axe_info = {
            "axe_difficulty": str(results[0]),
            "axe_coin_supply": str(results[1]),
            "axe_block_count": str(results[2]),
            "axe_network_hashps": str(results[3]*pow(10, -9))[0:8] + " GH/s",
            "axe_node_count": str(results[4]),

        }
        redis_store.set("axe_info", json.dumps(axe_info), config.redis_expire_time)
        return axe_info
    except Exception as e:
        return {
            "difficulty": "0",
            "coin_supply": "0",
            "block_count": "0",
            "network_hashps": "0 GH/s",
            "node_count": "0",
        }
