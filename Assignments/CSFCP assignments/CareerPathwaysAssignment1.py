# Simple stock portfolio profit/loss calculator
# User enters stock details, and the program calculates total profit or loss

num_stocks = int(input("How many stocks do you have? "))
total_profit = 0

for i in range(num_stocks):
	print(f"\nStock {i+1}:")
	buy_price = float(input("  Buy price per share: "))
	sell_price = float(input("  Sell price per share: "))
	shares = int(input("  Number of shares: "))
	profit = (sell_price - buy_price) * shares
	print(f"  Profit/Loss for this stock: {profit}")
	total_profit += profit

print(f"\nTotal portfolio profit/loss: {total_profit}")
