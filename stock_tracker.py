# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "MSFT": 300,
    "AMZN": 140
}

# Dictionary to store user's portfolio
portfolio = {}

print("📊 Stock Portfolio Tracker")

# Taking user input
while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    # Check if stock exists
    if stock not in stock_prices:
        print("❌ Stock not available!")
        continue

    quantity = int(input("Enter quantity: "))

    # Add stock to portfolio
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

# Calculate total investment
total = 0

print("\n📈 Portfolio Summary")

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price

    total += value

    print(f"{stock}: {qty} shares × ${price} = ${value}")

print("\n💰 Total Investment:", total)

# Save results to text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n\n")

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = qty * price

        file.write(f"{stock}: {qty} shares = ${value}\n")

    file.write(f"\nTotal Investment: ${total}")

print("\n✅ Portfolio saved to portfolio.txt")