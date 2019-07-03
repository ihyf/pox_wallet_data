# flo-get_info
---
URL:http://45.77.220.158:9000/api
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "get_info",
	"params": {

	}
}
```

## 下行
```json
{
    "result": {
        "difficulty": "2437.731013642524",
        "coin_supply": "151166710.48521888",
        "block_count": "3465638",
        "network_hashps": "280.2952 GH/s",
        "node_count": "116"
    },
    "id": 1,
    "jsonrpc": "2.0"
}
```

# flo-获取账户余额
---
URL:http://45.77.220.158:9000/api
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "get_balance",
	"params": {
        "address": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK"
	}
}
```

## 下行
```json
{
    "result": {
        "balance": "29.69991"
    },
    "id": 1,
    "jsonrpc": "2.0"
}
```
# flo-通过tx_id获取交易详情
---
URL:http://45.77.220.158:9000/api
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "get_transaction",
	"params": {
        "tx_id": "40118193c8342d381d3cf4547dbe7fa0c20c93becfe529602dfe2d3fd10d6362"
	}
}
```

## 下行
```json
{
	"result": {
		"transaction": {
			"txid": "d701ebbbce03ba7491f920dd2130265bea166ef7d7a39d7a2689813b6c12cc68",
			"hash": "d701ebbbce03ba7491f920dd2130265bea166ef7d7a39d7a2689813b6c12cc68",
			"version": 2,
			"size": 226,
			"vsize": 226,
			"locktime": 0,
			"vin": [{
				"txid": "8c8ef37dfed13d37810bb63ca8131e08e7f263f0df85eb5a72eea4f467656380",
				"vout": 1,
				"scriptSig": {
					"asm": "304402206097d819cd1043446e09359e9c3c094805888d502e6e7ad51b0460035282c779022029f822e40c24df61b947e220cc4a21f62d7f8632e2667122abbe8bfd96844195[ALL] 024f5374c77ad80945578b1894246798d3ef6abdacba254c0b5b937d3d8b331bb4",
					"hex": "47304402206097d819cd1043446e09359e9c3c094805888d502e6e7ad51b0460035282c779022029f822e40c24df61b947e220cc4a21f62d7f8632e2667122abbe8bfd968441950121024f5374c77ad80945578b1894246798d3ef6abdacba254c0b5b937d3d8b331bb4"
				},
				"sequence": 4294967295
			}],
			"vout": [{
				"value": 0.1,
				"n": 0,
				"scriptPubKey": {
					"asm": "OP_DUP OP_HASH160 964cc27f77366fcd03166c0127f004ac126a0268 OP_EQUALVERIFY OP_CHECKSIG",
					"hex": "76a914964cc27f77366fcd03166c0127f004ac126a026888ac",
					"reqSigs": 1,
					"type": "pubkeyhash",
					"addresses": ["FKXpmwKdTnMrQQBVhBRLpMbQy7PqiicYgV"]
				}
			}, {
				"value": 29.6999325,
				"n": 1,
				"scriptPubKey": {
					"asm": "OP_DUP OP_HASH160 40b1a4a6fc7c8b88ef2a1beac1fe3de118e8d088 OP_EQUALVERIFY OP_CHECKSIG",
					"hex": "76a91440b1a4a6fc7c8b88ef2a1beac1fe3de118e8d08888ac",
					"reqSigs": 1,
					"type": "pubkeyhash",
					"addresses": ["FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK"]
				}
			}],
			"floData": "",
			"hex": "020000000180636567f4a4ee725aeb85dff063f2e7081e13a83cb60b81373dd1fe7df38e8c010000006a47304402206097d819cd1043446e09359e9c3c094805888d502e6e7ad51b0460035282c779022029f822e40c24df61b947e220cc4a21f62d7f8632e2667122abbe8bfd968441950121024f5374c77ad80945578b1894246798d3ef6abdacba254c0b5b937d3d8b331bb4ffffffff0280969800000000001976a914964cc27f77366fcd03166c0127f004ac126a026888ac228006b1000000001976a91440b1a4a6fc7c8b88ef2a1beac1fe3de118e8d08888ac0000000000",
			"blockhash": "577355a5ba95d590caa29464fed0576db5c40fda29ff4ba6974bf63534221aaa",
			"confirmations": 11717,
			"time": 1558597032,
			"blocktime": 1558597032
		}
	},
	"id": 1,
	"jsonrpc": "2.0"
}
```
# flo-获取flo当前价格
---
URL:http://45.77.220.158:9000/api
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "get_flo_price",
	"params": {

	}
}
```

## 下行
```json
{
    "result": {
        "flo_rmb": "0.5427",
        "flo_usd": "0.077910",
        "flo_btc": "0.00000980"
    },
    "id": 1,
    "jsonrpc": "2.0"
}
```
# flo-获取账户交易记录-暂时废弃
---
URL:http://45.77.220.158:9000/api
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "get_transactions_by_address",
	"params": {
        "address": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK"
	}
}
```

## 下行
```json
{
	"result": {
		"info": {
			"address": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
			"sent": 122.099865,
			"received": 151.799775,
			"balance": "29.69991",
			"last_txs": [{
					"type": "vout",
					"addresses": "d9ac50e3ed9ea3c4cf193c502920fb4e1c8a4e22de53994cc480b0f79661fb9b"
				},
				{
					"addresses": "7f636844984f265c32e7182b0d3c41a33ae11e2fe9774dd138b2ed99cdadbe89",
					"type": "vin"
				},
				{
					"addresses": "8c8ef37dfed13d37810bb63ca8131e08e7f263f0df85eb5a72eea4f467656380",
					"type": "vin"
				},
				{
					"addresses": "d701ebbbce03ba7491f920dd2130265bea166ef7d7a39d7a2689813b6c12cc68",
					"type": "vin"
				},
				{
					"addresses": "f9c937f2a42d470a5b268e5a63db7561eccc140d14c10a1859dcf7629b5596dc",
					"type": "vin"
				}
			]
		}
	},
	"id": 1,
	"jsonrpc": "2.0"
}
```
# flo-获取账户交易记录
---
URL:http://45.77.220.158:8889/jsonrpc
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "get_transactions",
	"params": {
		"address":"FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK"
	}
}
```

## 下行
```json
{
    "result": {
        "txs": [
            {
                "txid": "c783ce7fb882282b08dbf43f7f24e440ade4fa7d6f1c6914683c2dc41d38bce8",
                "floData": "",
                "fees": 0.0000225,
                "balance": 28.1890775,
                "fromAddress": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
                "toAddress": "FTZ98LxWP6ksWvrEv9R5R4AAvek8sedwV3",
                "value": "0.10000000",
                "blockheight": 3471997,
                "time": 1559660436,
                "blocktime": 1559660436,
                "status": 1,
                "in_or_out": "out"
            },
            {
                "txid": "b0ca07011de617256facb45be08204574032ebe47390729acb58471f879a3731",
                "floData": "",
                "fees": 0.0000225,
                "balance": 28.2891,
                "fromAddress": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
                "toAddress": "FTZ98LxWP6ksWvrEv9R5R4AAvek8sedwV3",
                "value": "0.10000000",
                "blockheight": 3471989,
                "time": 1559660023,
                "blocktime": 1559660023,
                "status": 1,
                "in_or_out": "out"
            },
            {
                "txid": "8532fe2abb6b4cbc20ccfe1725522ced895ef1b1030b183ed51a25d058476876",
                "floData": "",
                "fees": 0.0000225,
                "balance": 28.3891225,
                "fromAddress": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
                "toAddress": "F85yR5SHbTg2So4DcVtskaNXw2e5A6dnLN",
                "value": "0.10000000",
                "blockheight": 3471980,
                "time": 1559659686,
                "blocktime": 1559659686,
                "status": 1,
                "in_or_out": "out"
            },
            {
                "txid": "b057138d130946bfc152e03c6f82b90021b2844c60e0a325c7f9f5bea6bd2413",
                "floData": "",
                "fees": 0.0000225,
                "balance": 28.399145,
                "fromAddress": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
                "toAddress": "FKXpmwKdTnMrQQBVhBRLpMbQy7PqiicYgV",
                "value": "0.01000000",
                "blockheight": 3471938,
                "time": 1559657768,
                "blocktime": 1559657768,
                "status": 1,
                "in_or_out": "out"
            },
            {
                "txid": "d82a372008cd462fdda5744694778efddc9138ba692ab66ae1905eed5fbb60ac",
                "floData": "",
                "fees": 0.0000225,
                "balance": 28.3991675,
                "fromAddress": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
                "toAddress": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
                "value": "28.39916750",
                "blockheight": 3470067,
                "time": 1559579239,
                "blocktime": 1559579239,
                "status": 1,
                "in_or_out": "out"
            },
            {
                "txid": "027168f3055036336eacd65e1016f1989e3704cfeb9c0dad31dd96880eb2b06b",
                "floData": "",
                "fees": 0.0000225,
                "balance": 28.399235,
                "fromAddress": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
                "toAddress": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
                "value": "28.39923500",
                "blockheight": 3470060,
                "time": 1559578497,
                "blocktime": 1559578497,
                "status": 1,
                "in_or_out": "out"
            },
            {
                "txid": "29c987fd0bdb9e648b0e19d57211d7466a81174ce4a407668480bc0fa4fe2c39",
                "floData": "",
                "fees": 0.0000225,
                "balance": 28.3992575,
                "fromAddress": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
                "toAddress": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
                "value": "28.39925750",
                "blockheight": 3470060,
                "time": 1559578497,
                "blocktime": 1559578497,
                "status": 1,
                "in_or_out": "out"
            },
            {
                "txid": "49b61ccc6b2d49961e50c6635869eb5001e208d71a9a75d0fbe75fc04fcc8acd",
                "floData": "",
                "fees": 0.0000225,
                "balance": 28.39919,
                "fromAddress": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
                "toAddress": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
                "value": "28.39919000",
                "blockheight": 3470060,
                "time": 1559578497,
                "blocktime": 1559578497,
                "status": 1,
                "in_or_out": "out"
            },
            {
                "txid": "54b814fc3f136faa36df309117f36374156a318cdd6d2842d80c79f0ef2fa026",
                "floData": "",
                "fees": 0.0000225,
                "balance": 28.399325,
                "fromAddress": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
                "toAddress": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
                "value": "28.39932500",
                "blockheight": 3470060,
                "time": 1559578497,
                "blocktime": 1559578497,
                "status": 1,
                "in_or_out": "out"
            },
            {
                "txid": "9237b7d62446f6f0ec70aa80bdb910f6fea101fe4807f7046e30bcce9906d4c1",
                "floData": "",
                "fees": 0.0000225,
                "balance": 28.3993475,
                "fromAddress": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
                "toAddress": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
                "value": "28.39934750",
                "blockheight": 3470060,
                "time": 1559578497,
                "blocktime": 1559578497,
                "status": 1,
                "in_or_out": "out"
            }
        ]
    },
    "id": 1,
    "jsonrpc": "2.0"
}
```
# flo-获取交易费
---
URL:http://45.77.220.158:8889/jsonrpc
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "get_transaction_fee",
	"params": {
		"wif":"xxx",
		"address":"FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
		"value": 0.1,
		"flodata": "mc 真有钱"
	}
}
```

## 下行
```json
{
    "result": {
        "inputs": [
            {
                "address": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
                "txId": "29c987fd0bdb9e648b0e19d57211d7466a81174ce4a407668480bc0fa4fe2c39",
                "vout": 0,
                "scriptPubKey": "76a91440b1a4a6fc7c8b88ef2a1beac1fe3de118e8d08888ac",
                "value": 2839925750,
                "confirmations": 0
            }
        ],
        "outputs": [
            {
                "address": "FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
                "value": 10000000
            },
            {
                "value": 2829923500
            }
        ],
        "fee": 2250
    },
    "id": 1,
    "jsonrpc": "2.0"
}
```

# flo-转账
---
URL:http://45.77.220.158:8889/jsonrpc
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "set_transaction",
	"params": {
		"wif":"xx",
		"address":"FBjBWwd4Bm8MAYdJqqLB2pvDXzP1AomBXK",
		"value": 0.09,
		"flodata": "mc 真有钱"
	}
}
```

## 下行
```json
{
    "result": "49b61ccc6b2d49961e50c6635869eb5001e208d71a9a75d0fbe75fc04fcc8acd",
    "id": 1,
    "jsonrpc": "2.0"
}
```