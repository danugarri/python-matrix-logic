import unittest
from utils import columns_sumation
from test_utils_polulate_matrix import TYPED_INPUT


class TestColumnsSumation(unittest.TestCase):
    # This function is a built in one
    def setUp(self):
        # Setting up a mocked matrix of 4*4
        self.typed_input = TYPED_INPUT
        self.matrix = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 9], [0, 1, 2, 3]]

    def test_columns_sumation(self):
        print("\nTesting Columns sumation:")
        # storing our expected arrays sumation for the provided matrix
        expected_columns_array_sumation = [12, 16, 20, 23]
        result = columns_sumation(self.matrix)
        for sumation_index in range(len(expected_columns_array_sumation)):
            self.assertEqual(
                expected_columns_array_sumation[sumation_index], result[sumation_index]
            )
            print(
                "At the index",
                sumation_index,
                "\n",
                expected_columns_array_sumation[sumation_index],
                "=",
                result[sumation_index],
            )


# In order to test this file separately

if __name__ == "__main__":
    unittest.main()
