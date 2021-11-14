"""This is the subtraction calculation"""

from calc.calculation import Calculation


class Subtraction(Calculation):
    # pylint: disable=missing-function-docstring
    """The subtraction class"""
    def get_result(self):
        return self.value_a - self.value_b
