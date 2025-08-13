import csv
from datetime import datetime

# File name
csv_filename = 'transactions1.csv'

# Column headers
headers = ['Date', 'Details', 'Amount', 'Currency', 'Debit/Credit', 'Status']
dict_headers={"name":"sham"}

# Function to get user inputs
def get_transaction_input():
    print("Enter transaction details:")
    date_input = input("Date (e.g., 28 Feb 2025): ")
    details = input("Details (e.g., Card Payment Received): ")
    amount = input("Amount (e.g., 18,551.62): ")
    currency = input("Currency (e.g., AED): ")
    type_dc = input("Type (Debit/Credit): ")
    status = input("Status (e.g., SETTLED): ")
    
    return [date_input, details, amount, currency, type_dc, status]

# Write header if file is empty or doesn't exist
def write_header_if_needed():
    try:
        with open(csv_filename, 'r', newline='') as file:
            if file.readline().strip() == '':
                raise FileNotFoundError  # Trigger writing header
    except FileNotFoundError:
        with open(csv_filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(dict_headers)

# Append transaction to CSV
def append_transaction(transaction):
    with open(csv_filename, 'a', newline=' ') as file:
        writer = csv.writer(file)
        writer.writerow(transaction)

# Main flow
if __name__ == '__main__':
    write_header_if_needed()
    transaction = get_transaction_input()
    append_transaction(transaction)
    print("Transaction saved successfully!")
