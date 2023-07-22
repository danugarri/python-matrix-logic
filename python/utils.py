import random  # Module to generate random numbers


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
