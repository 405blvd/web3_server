from web3 import Web3, EthereumTesterProvider
import json

w3 = Web3(Web3.HTTPProvider('https://polygon-mumbai.infura.io/v3/2c07a0a9ff2c4ea3bcb38b6e4bf073fd'))

jsonAbi="""[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "previousOwner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "account",
				"type": "address"
			}
		],
		"name": "Paused",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "account",
				"type": "address"
			}
		],
		"name": "Unpaused",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_address",
				"type": "address"
			}
		],
		"name": "deleteAdmin",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_address",
				"type": "address"
			}
		],
		"name": "deleteMinter",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_address",
				"type": "address"
			}
		],
		"name": "getAdmin",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_address",
				"type": "address"
			}
		],
		"name": "getMinter",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "pause",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "paused",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "renounceOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_address",
				"type": "address"
			}
		],
		"name": "setAdmin",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_address",
				"type": "address"
			}
		],
		"name": "setMinter",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "unpause",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]"""


contract = w3.eth.contract(address="0x8dD525e6dEe037A3f248F2a8FB4e6c9089ed98c2",abi=jsonAbi)
nonce = w3.eth.getTransactionCount("0x2FCC7b6400eD578C1bEBBEaC35eed342660a58EC")
privateKey="3e68c66a86c4bf2a03823985fe4b1c1528baefb80f4318d9e0f6e00c418f066a"
transaction = contract.functions.setMinter("0x7Eb61275390d8F3fB5e53c679aC60D7A270C44d9").buildTransaction(
    {'chainId':w3.eth.chainId,
     #'gas':1000000,
     'gas':10000,
     #'gasPrice':Web3.toWei(1000000,'gwei'),
     'maxFeePerGas': w3.toWei('2', 'gwei'),
     'maxPriorityFeePerGas': w3.toWei('1', 'gwei'),
     #'from':"0x2FCC7b6400eD578C1bEBBEaC35eed342660a58EC",
     'nonce':nonce
     })
singed_txn=w3.eth.account.sign_transaction(transaction,private_key=privateKey)
try:
 w3.eth.send_raw_transaction(singed_txn.rawTransaction)
except ValueError as err:
 e=err.args
 print(e)
 errorCode= e[0]['code']
 message = e[0]['message']
tx_hash = w3.toHex(w3.keccak(singed_txn.rawTransaction))
print(tx_hash)
while True:
 a=w3.eth.get_transaction(tx_hash)
 if a['blockNumber'] is not None:
  print(a)
  break

receipt=w3.eth.getTransactionReceipt(tx_hash)
print(receipt)


