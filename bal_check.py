from web3 import Web3

# Infura Mainnet URL
infura_url = "https://mainnet.infura.io/v3/9590977820354ac195d43fc28a08f329"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Any Ethereum address (e.g., Binance wallet)
wallet_address = '0x95222290DD7278Aa3Ddd389Cc1E1d165CC4BAfe5'

# Get balance in Wei
balance_wei = web3.eth.get_balance(wallet_address)

# Convert to ETH
balance_eth = web3.from_wei(balance_wei, "ether")

print(f"Wallet balance: {balance_eth} ETH")

