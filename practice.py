import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()


infura_url = os.getenv('INFURA_URL')
web3 = Web3(Web3.HTTPProvider(infura_url))
# Replace with the contract address you want to interact with
contract_address = Web3.to_checksum_address("0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d")

# Replace with the ABI for the contract
abi = [
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [{"name": "", "type": "string"}],
        "type": "function"
    }
]

# Create the contract instance
contract = web3.eth.contract(address=contract_address, abi=abi)

# Call the 'name' function
token_name = contract.functions.name().call()

print(f"Token Name: {token_name}")
