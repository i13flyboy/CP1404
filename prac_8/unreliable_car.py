from random import randint
from prac_8.car import Car


class UnreliableCar(Car):
    """An unreliable car."""

    def __init__(self, name, fuel, reliability):
        """Start the UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        # Drive the car, and see what happens.
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven