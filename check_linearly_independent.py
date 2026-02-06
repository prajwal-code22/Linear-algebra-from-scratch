""" This code shows how to check if two vectors are linearly independent. Two vectors are linearly independent 
if one vector cannot be expressed as a scalar multiple of the other. 
In this code, we will use NumPy to check for linear independence by 
calculating the determinant of a matrix formed by the two vectors. If the determinant is non-zero, 
the vectors are linearly independent; otherwise, they are dependent."""


""" This code only work for square matrix. If the vectors are in higher dimensions, we can use the rank of the matrix to check for linear independence.
In this case, we can create a matrix with the vectors as rows and check if the rank 
of the matrix is equal to the number of vectors. 
If the rank is less than the number of vectors, then they are linearly dependent; otherwise, they are independent."""
import numpy as np

def are_linearly_independent(vector1, vector2):
    # Create a matrix with the two vectors as rows
    matrix = np.array([vector1, vector2])
    # Calculate the determinant of the matrix
    determinant = np.linalg.det(matrix)
    if determinant != 0:
        print("The vectors are linearly independent.")
    else:
        print("The vectors are linearly dependent.")
    
    
if __name__ == "__main__":
    vector1 = np.array([1, 2])
    vector2 = np.array([2, 6])

    
    are_linearly_independent(vector1, vector2)
   