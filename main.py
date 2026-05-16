cars = [
    {
        "name": "BMW 320d",
        "buy_price": 2000,
        "sell_price": 3500
    },

    {
        "name": "Ford Fiesta",
        "buy_price": 1200,
        "sell_price": 2000
    },

    {
        "name": "Audi A4",
        "buy_price": 4000,
        "sell_price": 5200
    }
]

for car in cars:

    profit = car["sell_price"] - car["buy_price"]

    print(car["name"])
print("Profit:", profit)

if profit >= 1000:
    print("GOOD DEAL")

elif profit >= 500:
    print("OK DEAL")

else:
    print("BAD DEAL")

print()

    