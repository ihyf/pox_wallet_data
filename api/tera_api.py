# coding:utf-8
import requests
from my_dispatcher import api_add, api
from requests.packages import urllib3

urllib3.disable_warnings()
base_url = "https://194.1.237.94/api/v1/"

urls_dict = {
    "get_current_info": "GetCurrentInfo",
    "get_node_list": "GetNodeList",
    "get_account_list": "GetAccountList",
    "send_transaction_hex": "SendTransactionHex"
}


@api_add
def get_current_info(**kwargs):
    """获取tera当前区块了状态"""
    action = urls_dict.get("get_current_info", None)
    if not action:
        return {
            "error": "no action"
        }
    url = f"{base_url}{action}"
    r = requests.get(url, verify=False)
    info = r.json()
    return {
        "info": info
    }


@api_add
def get_node_list(**kwargs):
    """获取api 节点列表"""
    action = urls_dict.get("get_node_list", None)
    if not action:
        return {
            "error": "no action"
        }
    url = f"{base_url}{action}"
    r = requests.get(url, verify=False)
    info = r.json()
    return {
        "info": info
    }


@api_add
def get_account_list(**kwargs):
    """获取get_account_list"""
    action = urls_dict.get("get_account_list", None)
    if not action:
        return {
            "error": "no action"
        }
    url = f"{base_url}{action}"
    r = requests.get(url, verify=False)
    info = r.json()
    return {
        "info": info
    }


@api_add
def send_tx(**kwargs):
    """send_tx"""
    action = urls_dict.get("send_transaction_hex", None)
    if not action:
        return {
            "error": "no action"
        }
    url = f"{base_url}{action}"
    r = requests.get(url, verify=False)
    info = r.json()
    return {
        "info": info
    }