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
    largest_eigenvalues = []
    for _ in range(number_of_matrices):
        A = generate_hermitian_matrix(dimension)
        eigenvalues = np.linalg.eigvalsh(A)
        largest_eigenvalue = eigenvalues[-1]
        largest_eigenvalues.append(largest_eigenvalue)

    mean_largest = np.mean(largest_eigenvalues)
    standard_deviation = np.std(largest_eigenvalues)

    results.append({
        "dimension": dimension,
        "mean_largest": mean_largest,
        "standard_deviation": standard_deviation
    })

print("\nLargest Eigenvalue Results")
for result in results:
    print(result)

print("\nComparison with Square Root of Dimension")
for result in results:
    dimension = result["dimension"]
    mean_largest = result["mean_largest"]
    ratio = mean_largest / np.sqrt(dimension)
    print(
        f"Dimension: {dimension}, "
        f"Mean largest eigenvalue: {mean_largest:.4f}, "
        f"Ratio: {ratio:.4f}"
    )

dimensions_for_plot = [result["dimension"] for result in results]
mean_largest_values = [
    result["mean_largest"] for result in results
]

plt.figure()
plt.plot(
    dimensions_for_plot,
    mean_largest_values,
    marker="o"
)

plt.xlabel("Matrix Dimension")
plt.ylabel("Mean Largest Eigenvalue")
plt.title("Mean Largest Eigenvalue vs Matrix Dimension")
plt.grid(True)
plt.savefig("Figure_3_mean_largest.png")
plt.show()

sqrt_ratios = []

for result in results:
    dimension = result["dimension"]
    mean_largest = result["mean_largest"]
    ratio = mean_largest / np.sqrt(dimension)
    sqrt_ratios.append(ratio)

plt.figure()
plt.plot(
    dimensions_for_plot,
    sqrt_ratios,
    marker="o"
)
plt.xlabel("Matrix Dimension")
plt.ylabel("Mean Largest Eigenvalue / $\sqrt{n}$")
plt.title("Largest Eigenvalue Scaling with $\sqrt{n}$")
plt.grid(True)
plt.savefig("Figure_3_sqrt_scaling.png")
plt.show()
