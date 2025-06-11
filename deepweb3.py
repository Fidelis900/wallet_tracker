import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()


infura_url = f"https://mainnet.infura.io/v3/{os.getenv('infura_key')}"
web3 = Web3(Web3.HTTPProvider(infura_url))


# Bored Ape Yacht Club Contract
contract_address = Web3.to_checksum_address("0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d")

# ERC-721 ABI (simplified for read-only methods)
abi = [
    {
        "constant": True,
        "inputs": [{"name": "_tokenId", "type": "uint256"}],
        "name": "ownerOf",
        "outputs": [{"name": "owner", "type": "address"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [{"name": "", "type": "string"}],
        "type": "function"
    }
]

# Create contract instance
contract = web3.eth.contract(address=contract_address, abi=abi)

# Read contract data
nft_name = contract.functions.name().call()
owner = contract.functions.ownerOf(1).call()

print(f"🎨 NFT Collection: {nft_name}")
print(f"🧑 Owner of Token ID 1: {owner}")
