"""This is the division calculation"""

from calc.calculation import Calculation


class Multiplication(Calculation):
    """Division is easy..."""
    def get_result(self):
        return self.value_a * self.value_b
