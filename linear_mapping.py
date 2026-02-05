import numpy as np
A=np.array([[2,0],
            [0,2]])   # scaling matrix

x= np.array([3,5])
y= A @ x # matrix multiplication
print(y)  # Output: [6 10]