# Simple Bond Price and Yield Calculator

def bond_price(face, coupon, years, rate):
    total = 0
    for t in range(1, years + 1):
        total += (face * coupon) / (1 + rate) ** t
    total += face / (1 + rate) ** years
    return total

def estimate_ytm(face, coupon, years, price):
    rate = 0.05  # Start guess
    for _ in range(100):
        guess_price = bond_price(face, coupon, years, rate)
        if abs(guess_price - price) < 0.0001:
            return rate
        rate += 0.0005 if guess_price < price else -0.0005
    return rate

def main():
    print("Simple Bond Calculator")
    face = float(input("Face value: "))
    coupon = float(input("Coupon rate (as decimal, e.g. 0.05): "))
    years = int(input("Years to maturity: "))
    rate = float(input("Yield to maturity (as decimal): "))
    price = bond_price(face, coupon, years, rate)
    print("Bond price:", round(price, 2))

    price2 = float(input("\nEnter market price to estimate YTM: "))
    ytm = estimate_ytm(face, coupon, years, price2)
    print("Estimated YTM:", round(ytm * 100, 2), "%")

if __name__ == "__main__":
    main()
