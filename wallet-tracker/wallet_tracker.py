import os
import time
import csv
import json
from dotenv import load_dotenv
import re
import requests
from datetime import datetime, timezone

load_dotenv()
# Replace with your API key
API_KEY = os.getenv("API_KEY")  # Ensure you have a .env file with API_KEY set
if not API_KEY:
    raise ValueError("API_KEY not found. Please set it in your .env file.")



# Replace with the wallet address you want to track (e.g., Bitfinex wallet)
WALLET_ADDRESS = input("Enter your Ethereum/Token wallet address: ").strip().lower()
# Example: "0x32Be343B94f860124dC4fEe278FDCBD38C102D88"


def is_valid_eth_address(address):
    return re.fullmatch(r"0x[a-fA-F0-9]{40}", address) is not None

if not is_valid_eth_address(WALLET_ADDRESS):
    raise ValueError("Invalid Ethereum address format.")


try:
    num_to_display = int(input("How many recent transactions would you like to see? (e.g., 5, 10, 20): "))
    if num_to_display < 1:
        raise ValueError
except ValueError:
    print("Invalid input. Defaulting to 10 transactions.")
    num_to_display = 10
    
    
    


def get_transactions(address, api_key, retries=3, delay=2):
    url = "https://api.etherscan.io/api"
    params = {
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "desc",
        "apikey": api_key
    }

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            if data["status"] != "1":
                print("⚠️ Etherscan error (txlist):", data.get("message", "Unknown error"))
                return []

            return data["result"]

        except requests.exceptions.RequestException as e:
            print(f"❌ Attempt {attempt} failed: {e}")
            if attempt < retries:
                print(f"⏳ Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("❌ All retry attempts failed.")
                return []

    
    
    


def get_token_transfers(address, api_key, retries=3, delay=2):
    url = "https://api.etherscan.io/api"
    params = {
        "module": "account",
        "action": "tokentx",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "desc",
        "apikey": api_key
    }



    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            if data["status"] != "1":
                print("⚠️ Etherscan error (txlist):", data.get("message", "Unknown error"))
                return []

            return data["result"]

        except requests.exceptions.RequestException as e:
            print(f"❌ Attempt {attempt} failed: {e}")
            if attempt < retries:
                print(f"⏳ Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("❌ All retry attempts failed.")
                return []

    
    

def print_transactions(transactions, num_to_display):
    print("\n📄 Recent ETH Transactions\n" + "=" * 30)
    for tx in transactions[:num_to_display]:
        value_eth = int(tx["value"]) / 10**18
        timestamp = int(tx["timeStamp"])
        time_str = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

        from_addr = tx["from"].lower()
        to_addr = tx["to"].lower()
        wallet_addr = WALLET_ADDRESS.lower()

        direction = "Outgoing 🡲" if from_addr == wallet_addr else "Incoming 🡸" if to_addr == wallet_addr else "Other"

        print(f"🔹 {direction}")
        print(f"   • Value     : {value_eth:.6f} ETH")
        print(f"   • Timestamp : {time_str} UTC")
        print(f"   • Tx Hash   : {tx['hash']}")
        print("-" * 40)

        
        
        
        
def print_token_transfers(transfers, num_to_display):
    print("\n📦 Recent Token Transfers\n" + "=" * 30)
    for tx in transfers[:num_to_display]:
        token = tx["tokenSymbol"]
        value = int(tx["value"]) / 10 ** int(tx["tokenDecimal"])
        timestamp = int(tx["timeStamp"])
        time_str = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

        from_addr = tx["from"].lower()
        to_addr = tx["to"].lower()
        wallet_addr = WALLET_ADDRESS.lower()

        direction = "Sent 🡲" if from_addr == wallet_addr else "Received 🡸" if to_addr == wallet_addr else "Other"

        print(f"🔸 {direction} {value:.4f} {token}")
        print(f"   • Timestamp : {time_str} UTC")
        print(f"   • Tx Hash   : {tx['hash']}")
        print("-" * 40)

        
        
def save_results(data, filename_base, data_type="eth", file_format="json"):
    filename = f"{filename_base}_{data_type}.{file_format}"
    
    if file_format == "json":
        with open(filename, "w", newline="", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    else:  # CSV
        if data_type == "eth":
            keys = ["hash", "from", "to", "value", "timeStamp"]
        else:  # token
            keys = ["hash", "from", "to", "value", "tokenSymbol", "tokenDecimal", "timeStamp"]

        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            for tx in data:
                writer.writerow({k: tx.get(k, "") for k in keys})
    
    print(f"✔️ {data_type.capitalize()} transactions saved to {filename}")
    
    
def get_eth_balance(address, api_key):
    url = "https://api.etherscan.io/api"
    params = {
        "module": "account",
        "action": "balance",
        "address": address,
        "tag": "latest",
        "apikey": api_key
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data["status"] == "1":
            wei = int(data["result"])
            eth = wei / 10**18
            return eth
        else:
            print("⚠️ Etherscan error (eth balance):", data.get("message", "Unknown error"))
            return 0.0
    except requests.RequestException as e:
        print(f"❌ Failed to fetch ETH balance: {e}")
        return 0.0

      


if __name__ == "__main__":
    
    print("🔹 ETH Transactions:")
    time.sleep(0.5)
    eth_transactions = get_transactions(WALLET_ADDRESS, API_KEY)
    eth_balance = get_eth_balance(WALLET_ADDRESS, API_KEY)
    print(f"\n💰 ETH Balance: {eth_balance:.6f} ETH")

    if eth_transactions:
        print_transactions(eth_transactions, num_to_display )
    else:
        print("No ETH transactions found.")

    print("\n🔸 Token Transfers:")
    token_transfers = get_token_transfers(WALLET_ADDRESS, API_KEY, retries=3, delay=2)
    if token_transfers:
        print_token_transfers(token_transfers, num_to_display)
    else:
        print("No token transfers found.")
# Note: The above code assumes you have a valid Etherscan API key and the wallet address is correct.



    save_choice = input("\nDo you want to save the results to a file? (y/n): ").strip().lower()
    if save_choice == 'y':
        format_choice = input("Choose file format - JSON or CSV (default is JSON): ").strip().lower()
        if format_choice != "csv":
            format_choice = "json"

        filename_base = WALLET_ADDRESS[:6] + "_transactions"

        if eth_transactions:
            save_results(eth_transactions, filename_base, data_type="eth", file_format=format_choice)

        if token_transfers:
            save_results(token_transfers, filename_base, data_type="tokens", file_format=format_choice)

    
                