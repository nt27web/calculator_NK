import unittest

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    # default test
    def setUp(self) -> None:
        self.calculator = Calculator()

    # instance check test
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    # addition method test1
    def test_add_method_calculator_success(self):
        self.assertEqual(self.calculator.add(1.36,2.78), 4.14)

    # addition method test2
    def test_add_method_calculator_zero(self):
        self.assertEqual(self.calculator.add(-1.11, 1.11), 0)

    # subtraction method test1
    def test_subtract_method_calculator_success(self):
        self.assertEqual(self.calculator.subtract(4, 10), 6)

    # subtraction method test2
    def test_subtract_method_calculator_zero(self):
        self.assertEqual(self.calculator.subtract(4, 4), 0)

    # multiplication method test1
    def test_multiply_method_calculator_success(self):
        self.assertEqual(self.calculator.multiply(5, 5), 25)

    # multiplication method test2
    def test_multiply_method_calculator_zero(self):
        self.assertEqual(self.calculator.multiply(5, 0), 0)

    # division method test1
    def test_divide_method_calculator_success(self):
        self.assertEqual(self.calculator.divide(5, 20), 4)

    # division method test2
    def test_divide_method_calculator_zero(self):
        self.assertEqual(self.calculator.divide(5, 0), 0)

    # square method test1
    def test_square_method_calculator_success(self):
        self.assertEqual(self.calculator.square(5), 25)

    # square method test2
    def test_square_method_calculator_negative(self):
        self.assertEqual(self.calculator.square(-5), 25)

    # square root test1
    def test_square_root_method_calculator_success(self):
        self.assertEqual(self.calculator.square_root(25), 5)

    # square root test2 - accurate upto 3 decimal points
    def test_square_root_method_calculator_success_decimal(self):
        self.assertEqual(self.calculator.square_root(39.99), 6.324)

    def test_subtraction(self):
        test_data = CsvReader("src/Tests/Data/UnitTestSubtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_addition(self):
        test_data = CsvReader("src/Tests/Data/UnitTestAddition.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiplication(self):
        test_data = CsvReader("src/Tests/Data/UnitTestMultiplication.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_division(self):
        test_data = CsvReader("src/Tests/Data/UnitTestDivision.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)


if __name__ == '__main__':
    unittest.main()