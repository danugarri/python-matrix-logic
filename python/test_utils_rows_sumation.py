import unittest
from utils import rows_sumation
from test_utils_polulate_matrix import TYPED_INPUT


class TestRowsSumation(unittest.TestCase):
    # This function is a built in one
    def setUp(self):
        # Setting up a mocked matrix of 4*4
        self.typed_input = TYPED_INPUT
        self.matrix = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 9], [0, 1, 2, 3]]

    def test_rows_sumation(self):
        print("\nTesting rows sumation:")
        # storing our expected arrays sumation for the provided matrix
        expected_rows_array_sumation = [10, 22, 33, 6]
        result = rows_sumation(self.matrix)
        for sumation_index in range(len(expected_rows_array_sumation)):
            self.assertEqual(
                expected_rows_array_sumation[sumation_index], result[sumation_index]
            )
            print(
                "At the index",
                sumation_index,
                "\n",
                expected_rows_array_sumation[sumation_index],
                "=",
                result[sumation_index],
            )
