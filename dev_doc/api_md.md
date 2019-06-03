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
# flo-获取账户交易记录
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
		"value": 0.1
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
		"value": 0.09
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