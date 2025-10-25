import copy

def get_determinant(matrix):
    """
    Calculates the determinant of a square matrix 
    This function handles 2x2 and 3x3 matrices as base case
    calls itself for larger matrices using the cofactor expansion method.
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    # Iterate through the first row to apply cofactor expansion
    for j in range(n):
        sub_matrix = []
        # Create the sub-matrix by removing the first row and the current column
        for i in range(1, n):
            row = []
            for k in range(n):
                if k != j:
                    row.append(matrix[i][k])
            sub_matrix.append(row)
        
        # Add or subtract the term based on the position (i, j)
        sign = (-1)**(0 + j)
        determinant += sign * matrix[0][j] * get_determinant(sub_matrix)
    
    return determinant

def solve_cramers_rule(A, B):
    """
    Solves a system of linear equations Ax = B using Cramer's Rule.
    
    Args:
        A (list of lists): The square coefficient matrix of the system.
        B (list): The column vector of constants.
    
    Returns:
        list: The solution vector x, or None if the determinant is zero.
    """
    n = len(A)
    # Check if the matrix is square
    if any(len(row) != n for row in A):
        print("Error: The coefficient matrix must be square.")
        return None

    # Check if the constant vector has the correct dimension
    if len(B) != n:
        print("Error: The constants vector must have the same dimension as the matrix.")
        return None

    # Calculate the determinant of the main coefficient matrix
    det_A = get_determinant(A)

    # Cramer's Rule is not applicable if the determinant is zero
    if det_A == 0:
        print("The determinant of the main matrix is zero. Cramer's Rule cannot be used.")
        return None

    solution = []
    # Iterate through each variable to find its value
    for i in range(n):
        # Create a copy of the original matrix
        A_i = copy.deepcopy(A)
        # Replace the i-th column with the constants vector B
        for j in range(n):
            A_i[j][i] = B[j]
        
        # Calculate the determinant of the new matrix
        det_A_i = get_determinant(A_i)
        
        # Calculate the value of the variable and add to the solution
        x_i = det_A_i / det_A
        solution.append(x_i)
        
    return solution

# --- Example Usage ---

# Define a system of linear equations:
# $2x + 3y - z = 1$
# $-4x - y + 2z = 2$
# $5x + 3y + 4z = 3$

# The coefficient matrix A
A = [
    [2, 3, -1],
    [-4, -1, 2],
    [5, 3, 4]
]

# The constants vector B
B = [1, 2, 3]

# Solve the system
solution_vector = solve_cramers_rule(A, B)

# Print the results
if solution_vector:
    print("Solution found:")
    for i, value in enumerate(solution_vector):
        print(f"x_{i+1} = {value:.4f}")

# Example of a system where Cramer's Rule is not applicable (determinant is zero)
A_singular = [
    [1, 2],
    [2, 4]
]
B_singular = [5, 6]

print("\n--- Testing a singular matrix ---")
solve_cramers_rule(A_singular, B_singular)
