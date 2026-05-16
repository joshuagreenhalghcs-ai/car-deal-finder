print("Car Deal Finder")

running = True

total_profit = 0
cars_checked = 0

while running:

    buy_price = int(input("Enter buy price: "))
    sell_price = int(input("Enter sell price: "))

    profit = sell_price - buy_price

    total_profit = total_profit + profit
    cars_checked = cars_checked + 1

    print("Profit:")
    print(profit)

    if profit >= 5000:
        print("Perfect deal!")

    elif profit >= 2000:
        print("Amazing deal!")

    elif profit >= 1000:
        print("Good deal!")

    elif profit > 0:
        print("Small profit")

    else:
        print("Bad deal")

    print("Total profit so far:")
    print(total_profit)

    print("Cars checked:")
    print(cars_checked)

    again = input("Check another car? yes/no: ")

    if again == "no":
        running = False

print("Program ended")
average_profit = total_profit / cars_checked
