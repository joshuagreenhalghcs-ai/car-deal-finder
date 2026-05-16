def rate_deal(profit):

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


def show_totals(total_profit, cars_checked):

    average_profit = total_profit / cars_checked

    print("Total profit so far:")
    print(total_profit)

    print("Cars checked:")
    print(cars_checked)

    print("Average profit:")
    print(average_profit)


print("Car Deal Finder")

running = True

total_profit = 0
cars_checked = 0

cars = []

while running:

    print("")
    print("1. Check Car Deal")
    print("2. View Car History")
    print("3. Exit")
    print("4. Search Car")

    choice = input("Choose an option: ")

    if choice == "1":

        car_name = input("Enter car name: ")

        buy_price = int(input("Enter buy price: "))
        sell_price = int(input("Enter sell price: "))

        profit = sell_price - buy_price

        car = {
            "name": car_name,
            "buy": buy_price,
            "sell": sell_price,
            "profit": profit
        }

        cars.append(car)

        total_profit = total_profit + profit
        cars_checked = cars_checked + 1

        print("Profit:")
        print(profit)

        rate_deal(profit)

        show_totals(total_profit, cars_checked)

    elif choice == "2":

        print("Car History:")

        for car in cars:

            print("----------------")

            print("Car:")
            print(car["name"])

            print("Buy Price:")
            print(car["buy"])

            print("Sell Price:")
            print(car["sell"])

            print("Profit:")
            print(car["profit"])

    elif choice == "3":

        running = False

    elif choice == "4":

        search_name = input("Enter car name to search: ")

        found = False

        for car in cars:

            if car["name"].lower() == search_name.lower():

                print("----------------")

                print("Car found!")

                print("Car:")
                print(car["name"])

                print("Buy Price:")
                print(car["buy"])

                print("Sell Price:")
                print(car["sell"])

                print("Profit:")
                print(car["profit"])

                found = True

        if found == False:

            print("Car not found")

    else:

        print("Invalid option")

print("Program ended")
