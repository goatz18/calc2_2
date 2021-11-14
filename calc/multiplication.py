"""This is the multiplication calculation"""

from calc.calculation import Calculation


class Multiplication(Calculation):
    # pylint: disable=missing-function-docstring
    """The multiplication class"""
    def get_result(self):
        return self.value_a * self.value_b
