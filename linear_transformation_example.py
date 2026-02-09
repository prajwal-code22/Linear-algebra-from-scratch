import numpy as np
import matplotlib.pyplot as plt

def linear_transformation():
    matrix=np.array([[2,1],[1,2]])
    b1=np.array([1,1])
    b2=np.array([1,-1])

    P=np.column_stack((b1,b2))
    print("P matrix",P)
    P_inv=np.linalg.inv(P)
    print("P inverse in :",P_inv)
    A_tilde=P_inv@matrix@P
    print("Matrix in new basis:\n",A_tilde)
 

if __name__=="__main__":
    linear_transformation()