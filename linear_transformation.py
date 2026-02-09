import numpy as np
import matplotlib.pyplot as plt

def linear_transformation(vector):
    # Standard basis (for reference)
    e1 = np.array([1,0],dtype=float)
    e2 = np.array([0,1],dtype=float)

    # New basis
    b1 = np.array([2,3],dtype=float)
    b2 = np.array([1,4],dtype=float)

    P = np.column_stack((b1,b2))   # new basis as columns
    P_inv = np.linalg.inv(P)

    # Coordinates of vector in new basis
    vector_tilde = P_inv @ vector

    # Reconstruct vector back to standard coordinates (for plotting)
    vector_reconstructed = P @ vector_tilde

    # ----- Plot -----
    plt.figure(figsize=(7,7))
    plt.axhline(0,color='black')
    plt.axvline(0,color='black')
    plt.grid(True)

    # Draw standard basis
    plt.quiver(0,0, e1[0], e1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='e1,e2')
    plt.quiver(0,0, e2[0], e2[1], angles='xy', scale_units='xy', scale=1, color='blue')

    # Draw new basis
    plt.quiver(0,0, b1[0], b1[1], angles='xy', scale_units='xy', scale=1, color='green', label='b1,b2')
    plt.quiver(0,0, b2[0], b2[1], angles='xy', scale_units='xy', scale=1, color='green')

    # Draw vector
    plt.quiver(0,0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='red', label='vector')

    #draw vecto_tilde
    plt.quiver(0,0, vector_tilde[0],vector_tilde[1], angles='xy',scale_units='xy', scale=1, color='orange', label='vector in new basis')
    
    # draw reconstructed vector
    plt.quiver(0,0, vector_reconstructed[0], vector_reconstructed[1], angles='xy', scale_units='xy', scale=1, color='purple', label='reconstructed vector')
    
    plt.xlim(-1,10)
    plt.ylim(-1,10)
    plt.legend()
    plt.title("Vector and basis change")
    plt.show()

    return vector_tilde

if __name__=="__main__":
    v = np.array([5,6])
    coords_new_basis = linear_transformation(v)
    print("Vector coordinates in new basis:", coords_new_basis)
