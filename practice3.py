from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to Infura
infura_url = os.getenv('INFURA_URL')
web3 = Web3(Web3.HTTPProvider(infura_url))

# Confirm connection
if web3.is_connected():
    print("✅ Connected to Ethereum")

# Whale address
whale_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"  # Bitfinex wallet

# Get the transaction count (total txs by this address)
tx_count = web3.eth.get_transaction_count(whale_address)
print(f"📦 Total Transactions Sent: {tx_count}")
