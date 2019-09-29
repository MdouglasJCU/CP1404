from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi class"""
    taxi = SilverServiceTaxi("Lexus 1", 100, 2)
    taxi.start_fare()
    taxi.drive(18)
    print("{}.  Current total fare is ${}".format(taxi, taxi.get_fare()))


main()