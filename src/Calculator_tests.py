import unittest

from Calculator.Calculator import Calculator

class MyTestCase(unittest.TestCase):

    # default test
    def setUp(self) -> None:
        self.calculator = Calculator()

    # instance check test
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)



if __name__ == '__main__':
    unittest.main()