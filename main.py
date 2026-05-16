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

try:

    file = open("cars.txt", "r")

    lines = file.readlines()

    file.close()

    for i in range(0, len(lines), 5):

        car = {
            "name": lines[i].strip(),
            "buy": int(lines[i + 1].strip()),
            "sell": int(lines[i + 2].strip()),
            "profit": int(lines[i + 3].strip()),
        }

        cars.append(car)

except:

    print("No saved cars found")

while running:

    print("")
    print("1. Check Car Deal")
    print("2. View Car History")
    print("3. Exit")
    print("4. Search Car")
    print("5. Delete Car")
    print("6. View Statistics")
    print("7. Sort Cars By Profit")
    print("8. Export Report")

    choice = input("Choose an option: ")

    if choice == "1":

        car_name = input("Enter car name: ")

        while True:
            try:
                buy_price = int(input("Enter buy price: "))
                break
            except:
                print("Invalid number. Try again.")

        while True:
            try:
                sell_price = int(input("Enter sell price: "))
                break
            except:
                print("Invalid number. Try again.")

        profit = sell_price - buy_price

        car = {"name": car_name, "buy": buy_price, "sell": sell_price, "profit": profit}

        cars.append(car)

        file = open("cars.txt", "a")

        file.write(car_name + "\n")
        file.write(str(buy_price) + "\n")
        file.write(str(sell_price) + "\n")
        file.write(str(profit) + "\n")
        file.write("----------------\n")

        file.close()

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

    elif choice == "5":

        delete_name = input("Enter car name to delete: ")

        found = False

        for car in cars:

            if car["name"].lower() == delete_name.lower():

                cars.remove(car)

                file = open("cars.txt", "w")

                for saved_car in cars:

                    file.write(saved_car["name"] + "\n")
                    file.write(str(saved_car["buy"]) + "\n")
                    file.write(str(saved_car["sell"]) + "\n")
                    file.write(str(saved_car["profit"]) + "\n")
                    file.write("----------------\n")

                file.close()

                print("Car deleted")

                found = True

                break

        if found == False:

            print("Car not found")

    elif choice == "6":

        if len(cars) == 0:

            print("No cars available")

        else:

            profits = []

            for car in cars:

                profits.append(car["profit"])

            print("Highest Profit:")
            print(max(profits))

            print("Lowest Profit:")
            print(min(profits))

            print("Total Profit:")
            print(sum(profits))

            print("Average Profit:")
            print(sum(profits) / len(profits))

    elif choice == "7":

        sorted_cars = sorted(cars, key=lambda car: car["profit"], reverse=True)

        print("Cars Sorted By Profit:")

        for car in sorted_cars:

            print("----------------")

            print("Car:")
            print(car["name"])

            print("Profit:")
            print(car["profit"])

    elif choice == "8":

        file = open("report.txt", "w")

        file.write("CAR DEAL REPORT\n")
        file.write("====================\n\n")

        if len(cars) == 0:

            file.write("No cars stored\n")

        else:

            profits = []

            for car in cars:

                profits.append(car["profit"])

                file.write("Car: " + car["name"] + "\n")
                file.write("Buy Price: " + str(car["buy"]) + "\n")
                file.write("Sell Price: " + str(car["sell"]) + "\n")
                file.write("Profit: " + str(car["profit"]) + "\n")
                file.write("--------------------\n")

            file.write("\nSTATISTICS\n")
            file.write("====================\n")

            file.write("Highest Profit: " + str(max(profits)) + "\n")

            file.write("Lowest Profit: " + str(min(profits)) + "\n")

            file.write("Total Profit: " + str(sum(profits)) + "\n")

            file.write("Average Profit: " + str(sum(profits) / len(profits)) + "\n")

        file.close()

        print("Report exported successfully")

    else:

        print("Invalid option")

print("Program ended")
