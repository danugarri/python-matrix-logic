import random  # Module to generate random numbers


def exception_handler():
    try:
        # Exception controller
        typed_input = int(input("Enter the number of rows and columns:"))
    except ValueError:
        print("Invalid input type. Please enter a positive integer not a letter.")
        return None

    if typed_input <= 0:
        print("The typed input must be bigger than 0.")
        return None
    return typed_input


def populate_matrix(typed_input):
    # Initialize matrix
    matrix = []

    # Matrix population
    for row in range(typed_input):
        row_array = []
        # Loop for column entries
        for column in range(typed_input):
            # Adding random numbers between 0 an 9 inculded
            row_array.append(random.randint(0, 9))
        matrix.append(row_array)
    return matrix


def print_matrix(typed_input, matrix):
    print("\n")
    for row in range(typed_input):
        print("|\t", end="")
        for column in range(typed_input):
            print(matrix[row][column], end="\t")
        print("|")


def rows_sumation(matrix):
    print("\nRows sumation")
    rows_array_sumation = []
    # Adding row_index
    for row_index, row in enumerate(matrix):
        # Each row sumation
        row_sum = sum(row)
        # Appending each sumation to the Rows array sumation
        rows_array_sumation.append(row_sum)
        print("Row", row_index, ":", row, "-> Sum:", row_sum)
    print("\nRows Array sumation:", rows_array_sumation)


def columns_sumation(matrix):
    print("\nColumns sumation")
    columns_array_sumation = []
    # Adding row_index
    for row in matrix:
        for column_index, column in enumerate(matrix):
            # Each row sumation
            column_sum = sum(column)
            # Appending each sumation to the Rows array sumation
            columns_array_sumation.append(column_sum)
        print("Row", column_index, ":", column, "-> Sum:", column_sum)
    print("\nColumns Array sumation:", columns_array_sumation)
