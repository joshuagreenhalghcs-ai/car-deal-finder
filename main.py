print("Car Deal Finder")

buy_price = int(input("Enter buy price: "))
sell_price = int(input("Enter sell price: "))

profit = sell_price - buy_price

print("Profit:")
print(profit)

if profit >= 2000:
    print("Amazing deal!")

elif profit >= 1000:
    print("Good deal!")

elif profit > 0:
    print("Small profit")

else:
    print("Bad deal")
    