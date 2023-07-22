def generate_matrix():
    typed_input= int(input("Enter the number of row and columns:"))

    # Initialize matrix
    matrix = []
  
    # Matrix population
    for row in range(typed_input):
        row_array=[]
        # A for loop for column entries
        for column in range(typed_input):
            row_array.append(0)
            matrix.append(row_array)

    # For printing the matrix
    for row in range(typed_input):
        print("|\t" , end="")
        for column in range(typed_input):
            print(matrix[row][column], end='\t' )
        print("|")

generate_matrix()