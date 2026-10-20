"""CodeAlpha Python Internship - Task 2: Stock Portfolio Tracker"""
import csv
from datetime import datetime

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 135,
}


def get_portfolio():
    portfolio = {}
    print("Available stocks and prices:")
    for name, price in STOCK_PRICES.items():
        print(f"  {name}: ${price}")
    print("\nEnter stock name and quantity. Type 'done' when finished.\n")

    while True:
        name = input("Stock name: ").strip().upper()
        if name == "DONE":
            break
        if name not in STOCK_PRICES:
            print("Stock not available. Choose from the list above.")
            continue
        try:
            qty = int(input(f"Quantity of {name}: "))
            if qty <= 0:
                raise ValueError
        except ValueError:
            print("Please enter a positive whole number.")
            continue
        portfolio[name] = portfolio.get(name, 0) + qty
    return portfolio


def summarize(portfolio):
    rows, total = [], 0
    for name, qty in portfolio.items():
        price = STOCK_PRICES[name]
        value = price * qty
        total += value
        rows.append((name, qty, price, value))
    return rows, total


def print_summary(rows, total):
    print("\n" + "=" * 46)
    print(f"{'Stock':<8}{'Qty':>6}{'Price':>10}{'Value':>14}")
    print("-" * 46)
    for name, qty, price, value in rows:
        print(f"{name:<8}{qty:>6}{price:>10.2f}{value:>14.2f}")
    print("-" * 46)
    print(f"{'TOTAL INVESTMENT':<24}{total:>22.2f}")
    print("=" * 46)


def save_to_file(rows, total):
    choice = input("\nSave result to file? (txt/csv/no): ").strip().lower()
    if choice == "txt":
        with open("portfolio.txt", "w") as f:
            f.write(f"Portfolio Report - {datetime.now():%Y-%m-%d %H:%M}\n\n")
            for name, qty, price, value in rows:
                f.write(f"{name}: {qty} x ${price} = ${value}\n")
            f.write(f"\nTotal Investment: ${total}\n")
        print("Saved to portfolio.txt")
    elif choice == "csv":
        with open("portfolio.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            writer.writerows(rows)
            writer.writerow(["TOTAL", "", "", total])
        print("Saved to portfolio.csv")


def main():
    portfolio = get_portfolio()
    if not portfolio:
        print("No stocks entered.")
        return
    rows, total = summarize(portfolio)
    print_summary(rows, total)
    save_to_file(rows, total)


if __name__ == "__main__":
    main()
