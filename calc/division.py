"""This is the division calculation"""

from calc.calculation import Calculation


class Division(Calculation):
    """Division is easy..."""
    def get_Result(self):
        return self.value_a * self.value_b
