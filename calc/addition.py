"""This is the addition calculation"""

from calc.calculation import Calculation


class Addition(Calculation):
    """The addition class"""
    def get_result(self):
        return self.value_a + self.value_b
