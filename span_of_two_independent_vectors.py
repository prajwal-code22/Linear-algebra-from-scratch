#span of 2 independent vectors create flat plane in 3D space
""" Independent vectors means that they dont have same direction and they are not scalar multiples of each other.
In 3D space, if we have two independent vectors, they can be used to define a plane. The span of these two vectors will include all the points that can be expressed as a linear combination of the two vectors. This means that any point on the plane can be represented as a
 combination of the two independent vectors. The plane will be flat and will extend infinitely in all directions, as long as it is defined by the two independent vectors. The span of these vectors will create a 2D subspace within the 3D space, which is the plane defined by the two vectors.
    """
import numpy as np
import matplotlib.pyplot as plt

def span_of_two_independent_vectors(vector1, vector2, scalar1, scalar2):
    points = np.array([a*vector1 + b*vector2 for a in scalar1 for b in scalar2])    
    return points

def plot_span_of_two_independent_vectors(vector1, vector2, scalar1, scalar2):
    points = span_of_two_independent_vectors(vector1, vector2, scalar1, scalar2)
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], label='Span of the two vectors', alpha=0.5)
    ax.scatter(vector1[0], vector1[1], vector1[2], color='red', label='Vector 1')
    ax.scatter(vector2[0], vector2[1], vector2[2], color='blue', label='Vector 2')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Span of Two Independent Vectors in 3D Space')
    ax.legend()
    plt.show()

if __name__ == "__main__":
    vector1 = np.array([1, 0, 0])
    vector2 = np.array([0, 1, 0])
    scalar1 = np.linspace(-10, 10, 100)
    scalar2 = np.linspace(-10, 10, 100)
    plot_span_of_two_independent_vectors(vector1, vector2, scalar1, scalar2)