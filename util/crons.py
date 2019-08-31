import json
from util.tools import get_axe_info, get_flo_info, get_all_price
from util.db_redis import redis_store


def async_info():
    axe_info = get_axe_info()
    flo_info = get_flo_info()
    prices = get_all_price()
    flo_price = prices["flo"]
    axe_price = prices["axe"]

    redis_store.set("axe_info", json.dumps(axe_info))
    redis_store.set("flo_info", json.dumps(flo_info))
    redis_store.set("flo_price", json.dumps(flo_price))
    redis_store.set("axe_price", json.dumps(axe_price))
