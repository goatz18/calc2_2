"""This is the division calculation"""

from calc.calculation import Calculation


class Division(Calculation):
    # pylint: disable=missing-function-docstring
    """Division is easy..."""
    def get_result(self):
        return self.value_a / self.value_b
