import asyncio
import aiohttp
import requests
from lxml import etree


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


def get_axe_info():
    try:
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
            "difficulty": str(results[0]),
            "coin_supply": str(results[1]),
            "block_count": str(results[2]),
            "network_hashps": str(results[3]*pow(10, -9))[0:8] + " GH/s",
            "node_count": str(results[4]),
            "master_nodes": str(1800),
            "total": str(21000000)

        }
        return axe_info
    except Exception as e:
        return {
            "difficulty": "0",
            "coin_supply": "0",
            "block_count": "0",
            "network_hashps": "0 GH/s",
            "node_count": "0",
            "master_nodes": "0",
            "total": str(21000000)
        }


def get_flo_info(*args, **kwargs):
    try:
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
