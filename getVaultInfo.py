import requests
from dotenv import load_dotenv
import os
from web3 import Web3

load_dotenv()
infura_api = os.environ["infura_api_mainnet"]
etherscan_api_key = os.environ["etherscan_api_key"]

web3 = Web3(Web3.HTTPProvider(infura_api))

eth_c_vault_address = "0x25751853eab4d0eb3652b5eb6ecb102a2789644b"
start_block = 1320000 # Before any Ribbon Vaults went live
current_block = web3.eth.block_number

api_url = f"https://api.etherscan.io/api?module=logs \
    &action=getLogs                                  \
    &address={eth_c_vault_address}                   \
    &fromBlock={start_block}                         \
    &toBlock={current_block}                         \
    &page=1                                          \
    &offset=1000                                     \
    &apikey={etherscan_api_key}"

# headers = {'Content-Type': "application/x-www-form-urlencoded"}
headers = {'Content-Type': "application/json"}

response = requests.get(api_url, headers=headers)

print(response)
print(response.json())