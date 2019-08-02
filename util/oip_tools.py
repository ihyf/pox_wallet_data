# coding:utf-8
import config
import requests
import json


class Oip(object):
    def __init__(self, base_url):
        self.base_url = base_url

    def get_block(self, the_hash):
        url = self.base_url + "/block/" + the_hash
        r = requests.get(url)
        return r.json()

    def get_block_index(self, the_hash):
        url = self.base_url + "/block/" + the_hash
        r = requests.get(url)
        return r.json()

    def getRawBlock(self, the_hash):
        url = self.base_url + "/block/" + the_hash
        r = requests.get(url)
        return r.json()

    def getBlockSummary(self, the_hash):
        url = self.base_url + "/block/" + the_hash
        r = requests.get(url)
        return r.json()

    def getTransaction(self, the_hash):
        url = self.base_url + "/block/" + the_hash
        r = requests.get(url)
        return r.json()

    def getRawTransaction(self, the_hash):
        url = self.base_url + "/block/" + the_hash
        r = requests.get(url)
        return r.json()

    def getAddress(self, the_hash):
        url = self.base_url + "/block/" + the_hash
        r = requests.get(url)
        return r.json()

    def getAddressProperties(self, address, properties="balance"):
        url = self.base_url + "/addr/" + address + "/" + properties
        r = requests.get(url)
        return r.json()

    def get_address_utxo(self, address):
        url = self.base_url + "/addr/" + address + "/utxo"
        r = requests.get(url)
        return r.json()

    def getAddressesUtxo(self, the_hash):
        url = self.base_url + "/block/" + the_hash
        r = requests.get(url)
        return r.json()

    def getTransactionsForBlock(self, the_hash):
        url = self.base_url + "/block/" + the_hash
        r = requests.get(url)
        return r.json()

    def getTransactionsForAddress(self, address):
        url = self.base_url + "/txs/?address=" + address
        r = requests.get(url)
        return r.json()

    def getTransactionsForAddresses(self, the_hash):
        url = self.base_url + "/block/" + the_hash
        r = requests.get(url)
        return r.json()

    def broadcast_raw_transaction(self, ops):
        url = self.base_url + "/tx/send"
        headers = {
            "content-type": "application/json",
            "Authorization": ""
        }
        r = requests.post(url=url, data=json.dumps(ops), headers=headers)
        return r.json()

    def getSync(self, the_hash):
        url = self.base_url + "/block/" + the_hash
        r = requests.get(url)
        return r.json()

    def getPeer(self, the_hash):
        url = self.base_url + "/block/" + the_hash
        r = requests.get(url)
        return r.json()

    def getStatus(self, the_hash):
        url = self.base_url + "/block/" + the_hash
        r = requests.get(url)
        return r.json()

    def getExchangeRate(self, the_hash):
        url = self.base_url + "/block/" + the_hash
        r = requests.get(url)
        return r.json()

    def estimateFee(self, the_hash):
        url = self.base_url + "/block/" + the_hash
        r = requests.get(url)
        return r.json()

    def createErrorString(self, the_hash):
        url = self.base_url + "/block/" + the_hash
        r = requests.get(url)
        return r.json()

    def onAddressUpdate(self, the_hash):
        url = self.base_url + "/block/" + the_hash
        r = requests.get(url)
        return r.json()

    def onTX(self, the_hash):
        url = self.base_url + "/block/" + the_hash
        r = requests.get(url)
        return r.json()

    def onBlock(self, the_hash):
        url = self.base_url + "/block/" + the_hash
        r = requests.get(url)
        return r.json()


def get_axe_oip():
    oip = Oip(config.axe_livenet)
    return oip
