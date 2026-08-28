import numpy as np
import matplotlib.pyplot as plt

def generate_hermitian_matrix(size):
    A = np.random.randn(size, size)
    A = (A + A.T) / 2 
    return A

dimensions = [3, 5, 10, 20]
number_of_matrices = 1000

results = []

for dimension in dimensions:
    smallest_eigenvalues = []
    largest_eigenvalues = []
    for _ in range(number_of_matrices):
        A= generate_hermitian_matrix(dimension)
        eigenvalues = np.linalg.eigvalsh(A)
        smallest_eigenvalues.append(eigenvalues[0])
        largest_eigenvalues.append(eigenvalues[-1])
    mean_smallest = np.mean(smallest_eigenvalues)
    mean_largest = np.mean(largest_eigenvalues)
    mean_symmetry = np.mean(np.array(largest_eigenvalues) + np.array(smallest_eigenvalues))
    results.append({"dimension": dimension, "mean_smallest": mean_smallest, "mean_largest": mean_largest, "mean_symmetry": mean_symmetry})

print("\nLargest and Smallest Eigenvalue Results")
for result in results:
    print(result)

negative_mean_smallest = [-result["mean_smallest"] for result in results]
mean_largest_values = [result["mean_largest"] for result in results]

plt.figure()
plt.scatter(negative_mean_smallest, mean_largest_values)
plt.plot(negative_mean_smallest, negative_mean_smallest, linestyle="--", label="y = x")
plt.xlabel(r"$-\lambda_{\min}$")
plt.ylabel(r"$\lambda_{\max}$")
plt.title(r"Symmetry of Largest and Smallest Eigenvalues")
plt.legend()
plt.grid(True)
plt.savefig("Figure_4_eigenvalue_symmetry.png")
plt.show()