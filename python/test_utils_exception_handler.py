import unittest
from .utils import exception_handler
from unittest.mock import patch

# Constant definition
BUILTIN_INPUT = "builtins.input"


class TestExceptionHandler(unittest.TestCase):
    def test_negative_inputs(self):
        print("\nTesting negative inputs for matrix:")
        # Test with a negative input
        with patch(BUILTIN_INPUT, return_value="-3"):
            result = exception_handler()
        self.assertIsNone(result)

        print("\nTesting 0 input value for matrix")
        # Test with a 0 input value
        with patch(BUILTIN_INPUT, return_value="0"):
            result = exception_handler()
        self.assertIsNone(result)

        print("\nTesting letters inputs for matrix")
        # Test with a negative input
        with patch(BUILTIN_INPUT, return_value="f"):
            result = exception_handler()
        self.assertIsNone(result)


# In order to test this file separately

if __name__ == "__main__":
    unittest.main()
