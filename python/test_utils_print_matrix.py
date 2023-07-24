import unittest
import io
import sys
from python.utils import print_matrix
from python.test_utils_polulate_matrix import TYPED_INPUT


class TestPrintMatrix(unittest.TestCase):
    # This function is a built in one
    def setUp(self):
        print("\nTesting printed matrix:")
        # Setting up a mocked matrix of 4*4
        self.typed_input = TYPED_INPUT
        self.matrix = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 9], [0, 1, 2, 3]]

    def capture_print_output(self):
        # Captures the output of the print statements and returns them as a string
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        return output_buffer

    def test_print_matrix(self):
        # Test the function with the provided matrix
        expected_output = "\n\n|\t1\t2\t3\t4\t|\n|\t4\t5\t6\t7\t|\n|\t7\t8\t9\t9\t|\n|\t0\t1\t2\t3\t|\n"

        output_buffer = self.capture_print_output()  # Call to our defined method
        print_matrix(self.typed_input, self.matrix)
        sys.stdout = sys.__stdout__  # Restore the default stdout

        self.assertEqual(output_buffer.getvalue(), expected_output)
        print(
            "stdout output: ", output_buffer.getvalue(), "\nEquals\n:", expected_output
        )


# In order to test this file separately

if __name__ == "__main__":
    unittest.main()
