from prac_8.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi."""
    falling_flag = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return "{} plus falling flag of ${:.2f}".format(super().__str__(), self.falling_flag)

    def get_fare(self):
        # Get the current fare.
        return self.falling_flag + super().get_fare()