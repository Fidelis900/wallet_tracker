# Wallet Tracker

A Python tool to track Ethereum wallet balances, ETH transactions, and token transfers using the Etherscan API.

## Features

- Fetch and display recent ETH transactions for any Ethereum wallet.
- Fetch and display recent ERC-20 token transfers.
- Show current ETH balance.
- Save results to JSON or CSV files.
- Robust error handling and retry logic for API calls.

## Requirements

- Python 3.7+
- Etherscan API key

## Installation

1. Clone this repository.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the `wallet-tracker` directory with your Etherscan API key:
   ```
   API_KEY=your_etherscan_api_key_here
   ```

## Usage

Run the main script:

```sh
python main.py
```

- Enter the Ethereum wallet address you want to track.
- Enter the number of recent transactions to display.
- View the ETH balance, transactions, and token transfers.
- Optionally, save the results to a file (JSON or CSV).

## Example

```
Enter your Ethereum/Token wallet address: 0x32Be343B94f860124dC4fEe278FDCBD38C102D88
How many recent transactions would you like to see? (e.g., 5, 10, 20): 5

🔹 ETH Transactions:
...

💰 ETH Balance: 1.234567 ETH

🔸 Token Transfers:
...

Do you want to save the results to a file? (y/n): y
Choose file format - JSON or CSV (default is JSON): csv
✔️ Eth transactions saved to 0x32Be3_transactions.csv
✔️ Tokens transactions saved to 0x32Be3_transactions.csv
```

## Notes

- You must have a valid Etherscan API key.
- The script only supports Ethereum mainnet addresses.
- For any issues, please check your API key and wallet address format.

## License

MIT License
