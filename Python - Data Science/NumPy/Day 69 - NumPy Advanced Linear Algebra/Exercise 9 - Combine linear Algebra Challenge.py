import numpy as np

A = np.array([
    [2, 1],
    [1, 3]
])

# Transpose
print("Transpose:\n", A.T)

# Determinant
print("Determinant:", np.linalg.det(A))

# Inverse
inverse = np.linalg.inv(A)
print("Inverse:\n", inverse)

# Matrix Rank
print("Matrix Rank:", np.linalg.matrix_rank(A))

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Verify inverse
print("Identity Verification:", np.allclose(A @ inverse, np.eye(2)))