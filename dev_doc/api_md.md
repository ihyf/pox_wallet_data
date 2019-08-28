#正式环境:  http://39.100.40.109:9000/api  

#正式环境:  http://39.100.40.109:8889/jsonrpc  

#测试环境:  http://47.92.250.61:9000/api  

#测试环境:  http://47.92.250.61:8889/jsonrpc  

# flo-get_info
---
URL:http://39.100.40.109:9000/api
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
URL:http://39.100.40.109:9000/api
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
URL:http://39.100.40.109:9000/api
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

# flo-获取账户交易记录
---
URL:http://39.100.40.109:8889/jsonrpc
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

# 新增一条交易记录
---
URL:http://39.100.40.109:9000/api
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "add_transaction",
	"params": {
		"from_address": "F7WTiJVJNREE14MSVzgjiqFYUNTom7WmVG",
		"to_address": "xxWxiJVJNREE14MSVzgjiqFYUNTom7WmVG",
		"tx_id": "tx_id",
		"in_or_out": "out"
	}
}
```

## 下行
```json
{
	"result": {
		"msg": "add transaction success",
		"code": 200
	},
	"id": 1,
	"jsonrpc": "2.0"
}
```

# 获取最新转出交易的时间戳
---
URL:http://39.100.40.109:9000/api
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "get_tr_create_time",
	"params": {
		"address": "F7WTiJVJNREE14MSVzgjiqFYUNTom7WmVG"
	}
}
```

## 下行
```json
{
	"result": {
		"msg": True
	},
	"id": 1,
	"jsonrpc": "2.0"
}
```

# 获取 axe 帐户余额
---
URL:http://39.100.40.109:9000/api
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "get_axe_balance",
	"params": {
		"address": "P9bpHi2xFCMG3N5ZQeryXwV2abyzSC1TZj"
	}
}
```

## 下行
```json
{
	"result": {
		"balance": 16.71430134
	},
	"id": 1,
	"jsonrpc": "2.0"
}
```

# 获取 axe 交易记录
---
URL:http://39.100.40.109:9000/api
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "get_axe_transactions",
	"params": {
		"address": "P9bpHi2xFCMG3N5ZQeryXwV2abyzSC1TZj"
	}
}
```

## 下行
```json
{
	"result": {
		"txs": [{
			"txid": "781e8c5bc342b413e2eeb619ea4458a158cf3daace18dff98383aa8b3f37f675",
			"fees": 1.262e-05,
			"value": 4.17857144,
			"in_or_out": "out",
			"time": 1565208670,
			"blocktime": 1565208670,
			"from_address": "P9bpHi2xFCMG3N5ZQeryXwV2abyzSC1TZj",
			"to_address": "PDwhZsNUprk6RJecGxjXSXfxsEuvFvyGJF"
		}, {
			"txid": "457485e625142b2016c3468eca1aeea6a54371b5c0e105aac9bad1fb2ebd7846",
			"fees": 8.18e-06,
			"value": 4.17857144,
			"in_or_out": "out",
			"time": 1565204879,
			"blocktime": 1565204879,
			"from_address": "P9bpHi2xFCMG3N5ZQeryXwV2abyzSC1TZj",
			"to_address": "PQNduLnvNqdPKMC9FbAhBQNRUP9htqDFyh"
		}, {
			"txid": "8915b52fe02561646f7187d7c54afdebec71419e68cec11e1ccd34fba02d7351",
			"fees": 9.66e-06,
			"value": 4.17864268,
			"in_or_out": "out",
			"time": 1565197669,
			"blocktime": 1565197669,
			"from_address": "P9bpHi2xFCMG3N5ZQeryXwV2abyzSC1TZj",
			"to_address": "PRmd9NDgrCqtWJqd9GXKccNvd5wMZ1MVL1"
		}, {
			"txid": "cee6b619333097181c56c8763d5b741a5d5c7cfdd1894d22c17822a0fb430e1c",
			"fees": 1.558e-05,
			"value": 4.17857814,
			"in_or_out": "out",
			"time": 1565171942,
			"blocktime": 1565171942,
			"from_address": "P9bpHi2xFCMG3N5ZQeryXwV2abyzSC1TZj",
			"to_address": "PVdu8jXt1gq6Z2A69WjM8sFPdvjhQGJyB2"
		}, {
			"txid": "bd2fd88df0453fa944a3abea3fca577118a8dcf1a303b5aa7f2ffc376828fd27",
			"fees": 1.558e-05,
			"value": 4.17857144,
			"in_or_out": "out",
			"time": 1565143224,
			"blocktime": 1565143224,
			"from_address": "P9bpHi2xFCMG3N5ZQeryXwV2abyzSC1TZj",
			"to_address": "PMeSSyZQ2GBUkgSkT14KHg7Lx6TKxEiUEi"
		}, {
			"txid": "dee1c88086f75e8b64a4a3a81531c3248b0a5d172e69ce6419d5dd484a2f0cc7",
			"fees": 1.854e-05,
			"value": 4.17857144,
			"in_or_out": "out",
			"time": 1565109950,
			"blocktime": 1565109950,
			"from_address": "P9bpHi2xFCMG3N5ZQeryXwV2abyzSC1TZj",
			"to_address": "PJWLecCHoTq9q178zgdnR2yaNqb3EJEX8B"
		}, {
			"txid": "d67498a2cbca112c4fb1a21359cdaea2f87e78844367861912ba74f3a172f288",
			"fees": 2.742e-05,
			"value": 4.17857144,
			"in_or_out": "out",
			"time": 1565106079,
			"blocktime": 1565106079,
			"from_address": "P9bpHi2xFCMG3N5ZQeryXwV2abyzSC1TZj",
			"to_address": "PMpF94SfRN5rHnLjjfsgejeECtGVH12Kf6"
		}]
	},
	"id": 1,
	"jsonrpc": "2.0"
}
```

# 获取 axe utxo
---
URL:http://39.100.40.109:9000/api
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "get_axe_address_utxo",
	"params": {
		"address": "P9bpHi2xFCMG3N5ZQeryXwV2abyzSC1TZj"
	}
}
```

## 下行
```json
{
	"result": {
		"utxo": [{
			"address": "P9bpHi2xFCMG3N5ZQeryXwV2abyzSC1TZj",
			"txid": "3a93cfdf9ff8f5f737f299bc80ac62c822474c613923b350b00365b69dcd051c",
			"vout": 0,
			"scriptPubKey": "76a9140b171f8724262930b0a5985c4310e7fd8b4695ab88ac",
			"amount": 4.17857144,
			"satoshis": 417857144,
			"height": 301634,
			"confirmations": 27
		}, {
			"address": "P9bpHi2xFCMG3N5ZQeryXwV2abyzSC1TZj",
			"txid": "dfd132daf86794687249d437a1a7341d984b38d02fb89ab961bd9d0bc23544cc",
			"vout": 0,
			"scriptPubKey": "76a9140b171f8724262930b0a5985c4310e7fd8b4695ab88ac",
			"amount": 4.17858702,
			"satoshis": 417858702,
			"height": 301589,
			"confirmations": 72
		}, {
			"address": "P9bpHi2xFCMG3N5ZQeryXwV2abyzSC1TZj",
			"txid": "6458f1848e88499f85e7cb3b1592296276ff0adb17ec2f3db775c1a37af12b38",
			"vout": 0,
			"scriptPubKey": "76a9140b171f8724262930b0a5985c4310e7fd8b4695ab88ac",
			"amount": 4.17857144,
			"satoshis": 417857144,
			"height": 301584,
			"confirmations": 77
		}, {
			"address": "P9bpHi2xFCMG3N5ZQeryXwV2abyzSC1TZj",
			"txid": "a2d6b6bcbd5b5c55cc0a24278ad6b5a57686e7b69e89d4d7d1fcfed6a75a9cf8",
			"vout": 0,
			"scriptPubKey": "76a9140b171f8724262930b0a5985c4310e7fd8b4695ab88ac",
			"amount": 4.17857144,
			"satoshis": 417857144,
			"height": 301462,
			"confirmations": 199
		}]
	},
	"id": 1,
	"jsonrpc": "2.0"
}
```
# 获取 axe flo 价格
---
URL:http://39.100.40.109:9000/api
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "get_all_price",
	"params": {}
}
```

## 下行
```json
{
	"result": {
		"flo": {
			"flo_rmb": "0.3970",
			"flo_usd": "0.056260",
			"flo_btc": "0.00000495"
		},
		"axe": {
			"axe_rmb": "10.0498",
			"axe_usd": "1.4239",
			"axe_btc": "0.00012535"
		}
	},
	"id": 1,
	"jsonrpc": "2.0"
}
```
# 获取 axe info
---
URL:http://39.100.40.109:9000/api
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "get_axe_info",
	"params": {}
}
```

## 下行
```json
{
	"result": {
		"difficulty": "3055230.17998016",
		"coin_supply": "4963548.33922776",
		"block_count": "316025",
		"network_hashps": "78423.37 GH/s",
		"node_count": "9",
		"master_nodes": "1800",
		"total": "21000000"
	},
	"id": 1,
	"jsonrpc": "2.0"
}
```

# axe 广播接口
---
URL:http://39.100.40.109:9000/api
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "broadcast_axe_raw_hex",
	"params": {
		"hex": "0300000001e275ae6737ec1202f7fabb1df744866101ccd4ff6c9985ae43fc9751615b7eb7010000006a473044022055aef1e7034de6c5fe8b535b28c11c601915db889e2f222a37f2f4d1db61c36a0220315c11964c47ad6bc64f89ce2cdac0024e9c734dfcb8b0c94e3cda5c545a15380121024a89fbb4e93cde5a41656ff04d32435280c9dda07e99b5db0955fa45acd4486effffffff0100e1f505000000001976a91450a57805c915b69d896ca5a3d7dd2a90ad187eaf88ac00000000"
	}
}
```

## 下行
```json
{
	"result": {
		"tx": "xxx"
	},
	"id": 1,
	"jsonrpc": "2.0"
}
```
if error 
```json
{
	"result": {
		"error": "256: absurdly-high-fee. Code:-26"
	},
	"id": 1,
	"jsonrpc": "2.0"
}
```