def print_matrix(typed_input, matrix):
    for row in range(typed_input):
        print("|\t", end="")
        for column in range(typed_input):
            print(matrix[row][column], end="\t")
        print("|")
