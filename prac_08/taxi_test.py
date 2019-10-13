from taxi import Taxi


def main():
    """Test Taxi class"""
    taxi = Taxi("Prius 1", 100)
    taxi.start_fare()
    taxi.drive(40)
    print("{}.  Current total fare is ${}".format(taxi, taxi.get_fare()))
    taxi.start_fare()
    taxi.drive(100)
    print("{}.  Current total fare is ${}".format(taxi, taxi.get_fare()))


main()