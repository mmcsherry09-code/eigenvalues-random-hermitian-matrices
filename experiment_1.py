import numpy as np
import matplotlib.pyplot as plt

def generate_hermitian_matrix(size):
    A = np.random.randn(size, size)
    A = (A + A.T) / 2
    return A

all_eigenvalues = []

for _ in range(1000):
    A = generate_hermitian_matrix(3)
    eigenvalues = np.linalg.eigvalsh(A)
    all_eigenvalues.extend(eigenvalues)

# Summary of statistics
print("Standard Deviation:", np.std(all_eigenvalues))
print("Mean Eigenvalue:", np.mean(all_eigenvalues))
print("Minimum Eigenvalue:", np.min(all_eigenvalues))
print("Maximum Eigenvalue:", np.max(all_eigenvalues))

plt.figure()
plt.hist(all_eigenvalues, bins=30)
plt.title("Distribution of Eigenvalues for Random 3x3 Hermitian Matrices")
plt.xlabel("Eigenvalue")
plt.ylabel("Frequency")
plt.savefig("Figure_1.png")
plt.show()

