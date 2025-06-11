from web3 import Web3

# Connect to Infura
infura_url = 'https://mainnet.infura.io/v3/9590977820354ac195d43fc28a08f329'
web3 = Web3(Web3.HTTPProvider(infura_url))

# Get latest block
block = web3.eth.get_block('latest', full_transactions=True)

# Get list of transactions
transactions = block['transactions']

# Let's pick the first transaction
tx = transactions[0]

# Print details
print(f"📤 From: {tx['from']}")
print(f"📥 To: {tx['to']}")
print(f"💰 Value: {web3.from_wei(tx['value'], 'ether')} ETH")
print(f"⛽ Gas used: {tx['gas']}")
print(f"🧾 Tx Hash: {tx['hash'].hex()}")
