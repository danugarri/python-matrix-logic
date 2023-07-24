import unittest
from .utils import populate_matrix

# Constant definition
TYPED_INPUT = 4


class TestPopulateMatrix(unittest.TestCase):
    def test_rows_number(self):
        print("\nTesting rows matrix length")
        # Test the number of rows to equal the typed input

        result = populate_matrix(TYPED_INPUT)
        print("This Matrix: ", result, "has", len(result), "rows")
        self.assertEqual(len(result), TYPED_INPUT)

    def test_columns_number(self):
        print("\nTesting columns matrix length")
        # Test the number of columns to equal the typed input

        result = populate_matrix(TYPED_INPUT)
        # for each row the number of elemnts must equal the type input
        # Or in other words the number of columns must equal the type input
        for row in result:
            print("this row has: ", len(row), "Columns")
            self.assertEqual(len(row), TYPED_INPUT)

    def test_populated_numbers(self):
        print("\nTesting numbers populated")
        # Test the numbers inserted to be between 0 and 9

        result = populate_matrix(TYPED_INPUT)
        # for each row the number of elemnts must equal the type input
        # Or in other words the number of columns must equal the type input
        print(result)
        for row in result:
            for element in row:
                self.assertGreaterEqual(element, 0)
                self.assertLessEqual(element, 9)
                print(element, "is >= 0 and <= 9")


# In order to test this file separately

if __name__ == "__main__":
    unittest.main()
