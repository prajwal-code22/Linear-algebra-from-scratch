import numpy as np
import matplotlib.pyplot as plt

def span_of_one_vector(vector ,scalar):
    points=np.array([a*vector for a in scalar])
    return points

def plot_span_of_vector(vector, scalar):
    points=span_of_one_vector(vector,scalar)
    plt.figure(figsize=(8,8))
    plt.plot(points[:,0], points[:,1], label='Span of the vector')
    plt.scatter(vector[0], vector[1], color='red', label='Original Vector')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Span of a Single Vector')
    plt.legend()
    plt.grid()
    plt.show()
    

if __name__ == "__main__":
    vector=np.array([2,3])
    scalar=np.linspace(-10,10,100)
    plot_span_of_vector(vector,scalar)

