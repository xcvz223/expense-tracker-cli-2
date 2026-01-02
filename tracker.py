import sys
import json
import os

DB_FILE = "expenses.json"

def load_data():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_data(expenses):
    with open(DB_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def main():
    if len(sys.argv) < 2:
        print("Usage: python tracker.py [add <description> <amount> | list]")
        return

    command = sys.argv[1].lower()
    expenses = load_data()

    if command == "add" and len(sys.argv) == 4:
        description = sys.argv[2]
        try:
            amount = float(sys.argv[3])
            expenses.append({"description": description, "amount": amount})
            save_data(expenses)
            print(f"Successfully added: {description} (${amount})")
        except ValueError:
            print("Error: Amount must be a number.")

    elif command == "list":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("--- Expense List ---")
            total = 0
            for idx, item in enumerate(expenses, 1):
                print(f"{idx}. {item['description']}: ${item['amount']:.2f}")
                total += item['amount']
            print(f"Total: ${total:.2f}")
    else:
        print("Unknown command or missing arguments.")

if __name__ == '__main__':
    main()