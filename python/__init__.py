# Mandatory file to treat the directory as a Python package.
# Entry point

# Importing functions from utils
from .utils import (
    exception_handler,
    populate_matrix,
    print_matrix,
    rows_sumation,
    columns_sumation,
)


def generate_matrix():
    typed_input = exception_handler()
    if typed_input is None:
        print("Invalid input or value not provided. Exiting....")
        return
    # Initialise and populate Matrix
    matrix = populate_matrix(typed_input)
    # For printing the matrix
    print_matrix(typed_input, matrix)
    # Rows sumation
    rows_sumation(matrix)
    # Columns sumation
    columns_sumation(matrix)


generate_matrix()


# Necesa
if __name__ == "__main__":
    generate_matrix()
