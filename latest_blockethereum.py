from web3 import Web3

# Connect to Ethereum mainnet via Infura
infura_url = "https://mainnet.infura.io/v3/9590977820354ac195d43fc28a08f329"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check connection
if web3.is_connected():
    latest_block = web3.eth.block_number
    print(f"✅ Connected! Latest block number is: {latest_block}")
else:
    print("❌ Failed to connect to Ethereum.")
