from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi


def main():
    taxi_to_drive = 0
    total_bill = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("let's Drive!")
    menu = input("q)uit, c)hoose taxi, d)rive\n")

    while menu != "q":
        if menu == 'c':
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_to_drive = int(input("Choose taxi: "))
            print("bill to date ${}".format(total_bill))
            current_taxi = taxis[taxi_to_drive]
        elif menu == 'd':
            current_taxi.start_fare()
            distance = float(input("Drive how far? "))
            current_taxi.drive(distance)
            total_bill += taxis[taxi_to_drive].get_fare()
            print("your {} trip cost you ${}".format(current_taxi.name, taxis[taxi_to_drive].get_fare()))
            print("bill to date: ${}".format(total_bill))

        menu = input("q)uit, c)hoose taxi, d)rive\n")

    print("Total cost of trip ${}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Runs through options to drive taxi"""
    list_total = 0

    for i in taxis:
        print(list_total, i)
        list_total += 1


main()
