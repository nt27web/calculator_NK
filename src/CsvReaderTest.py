import unittest
import pprint
from CsvReader.CsvReader import CsvReader, class_factory


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('src/Tests/Data/UnitTestSubtraction.csv')

    def test_return_data_as_objects(self):
        value1 = self.csv_reader.return_data_as_class('Value 1')
        value2 = self.csv_reader.return_data_as_class('Value 2')
        result = self.csv_reader.return_data_as_class('result')

        self.assertIsInstance(value1, list)
        self.assertIsInstance(value2, list)
        self.assertIsInstance(result, list)

        test_class1 = class_factory('Value 1', self.csv_reader.data[0])
        test_class2 = class_factory('Value 2', self.csv_reader.data[0])
        test_class3 = class_factory('result', self.csv_reader.data[0])

        for value in value1:
            self.assertEqual(value.__name__, test_class1.__name__)
            pprint(vars(value))

        for value in value2:
            self.assertEqual(value.__name__, test_class2.__name__)
            pprint(vars(value))

        for value in result:
            self.assertEqual(value.__name__, test_class3.__name__)
            pprint(vars(value))


if __name__ == '__main__':
    unittest.main()
