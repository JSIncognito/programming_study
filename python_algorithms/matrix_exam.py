import numpy as np

A = np.array([[1],[2]])
B = np.array([[3, 4]])

print("A * B : \n", np.dot(A, B))
print("At * Bt : \n", np.dot(A.T, B.T))
print("B * A : \n", np.dot(B, A))
print("Bt * At : \n", np.dot(B.T, A.T))