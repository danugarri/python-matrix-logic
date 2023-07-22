# Importing functions from utils
from utils import populate_matrix, print_matrix, rows_sumation


def generate_matrix():
    try:
        # Exception controller
        typed_input = int(input("Enter the number of rows and columns:"))
    except ValueError:
        print("Invalid input type. Please enter a positive integer not a letter.")
        return

    if typed_input <= 0:
        print("The typed input must be bigger than 0.")
        return
    # Initialise and populate Matrix
    matrix = populate_matrix(typed_input)
    # For printing the matrix
    print_matrix(typed_input, matrix)
    # Rows sumation
    rows_sumation(matrix)


generate_matrix()
