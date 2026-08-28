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
    all_eigenvalues = []
    for _ in range(number_of_matrices):
        A = generate_hermitian_matrix(dimension)
        eigenvalues = np.linalg.eigvalsh(A)
        all_eigenvalues.extend(eigenvalues)

    mean = np.mean(all_eigenvalues)
    standard_deviation = np.std(all_eigenvalues)
    minimum = np.min(all_eigenvalues)
    maximum = np.max(all_eigenvalues)
    results.append({"dimension": dimension, "mean": mean, "standard_deviation": standard_deviation, "minimum": minimum, "maximum": maximum})
    plt.figure()
    plt.hist(all_eigenvalues, bins=30, density=True)
    plt.xlabel("Eigenvalue")
    plt.ylabel("Density")
    plt.title(f"Eigenvalue Distribution for Random {dimension}x{dimension} Hermitian Matrices")
    plt.grid(True)
    plt.savefig(f"Figure_2_{dimension}x{dimension}.png")
    plt.show()

print("\nSummary of Results")
for result in results:
    print(result)

dimensions_for_plot = [result["dimension"] for result in results]
standard_deviations = [result["standard_deviation"] for result in results]

plt.figure()
plt.plot(dimensions_for_plot, standard_deviations, marker="o")

plt.xlabel("Matrix Dimension")
plt.ylabel("Standard Deviation of Eigenvalues")
plt.title("Eigenvalue Spread vs Matrix Dimension")
plt.grid(True)
plt.savefig("Figure_2_summary.png")
plt.show()