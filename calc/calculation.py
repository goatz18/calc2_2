"""This is our calculation base class / Abstract Class"""


class Calculation:

    # constructor and it is the first function called when an object of the class is instantiated
    def __init__(self, value_a, value_b):
        # self references the instantiated object of the class
        self.value_a = float(value_a)
        self.value_b = float(value_b)
    # Class Factory Method <- bound to the class and not the instance of the class

    @classmethod
    def create(cls, value_a, value_b):
        return cls(value_a, value_b)
