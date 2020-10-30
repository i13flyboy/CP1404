from prac_8.silver_service_taxi import SilverServiceTaxi


def main():
    # Test SilverServiceTaxi
    taxi = SilverServiceTaxi("Test fancy silver service Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()