import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 3, 5) == 15

    def test_division_calculation_correctly(self):
        assert self.calc.division(self, 16, 4) == 4

    def test_substraction_corractly(self):
        assert self.calc.subtraction(self, 24, 10) == 14

    def test_adding_correctly(self):
        assert self.calc.adding(self, 9, 91) == 100