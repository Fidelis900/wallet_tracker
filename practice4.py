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

# Whale address (Bitfinex wallet)
whale_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"

# Get the total number of transactions sent by the whale
tx_count = web3.eth.get_transaction_count(whale_address)
print(f"📦 Total Transactions Sent: {tx_count}")

# Let's fetch the details of the last 5 transactions made by this address
# We'll go from the latest transaction to the oldest
for i in range(tx_count - 1, tx_count - 6, -1):
    # Fetch the transaction hash using the transaction count
    tx_hash = web3.eth.get_transaction_by_block('latest', i)
    print(f"\n🔍 Fetching Transaction {i + 1}: {tx_hash}")

    # Fetch the details of the transaction by hash
    tx_details = web3.eth.get_transaction(tx_hash)
    
    # Now print the details of each transaction
    print(f"📤 From: {tx_details['from']}")
    print(f"📥 To: {tx_details['to']}")
    print(f"💰 Value: {web3.fromWei(tx_details['value'], 'ether')} ETH")
    print(f"⛽ Gas used: {tx_details['gas']}")
    print(f"🧾 Tx Hash: {tx_details['hash'].hex()}")
    print(f"🔗 Block Number: {tx_details['blockNumber']}")
