import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()


infura_url = f"https://mainnet.infura.io/v3/{os.getenv('INFURA_API_KEY')}"
web3 = Web3(Web3.HTTPProvider(infura_url))
# Replace with the transaction hash you want to check
tx_hash = "0xTransactionHashHere"

# Get transaction details
tx = web3.eth.get_transaction(tx_hash)

print(f"Transaction Details: {tx}")
