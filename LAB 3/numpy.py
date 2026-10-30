
import numpy as np

# 1. Create arrays
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([1, 2, 3, 4, 5])

print("Array 1:", arr1)
print("Array 2:", arr2)

# 2. Arithmetic operations
print("\nAddition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)

# 3. Mathematical operations
print("\nSum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Maximum:", np.max(arr1))
print("Minimum:", np.min(arr1))
print("Standard Deviation:", np.std(arr1))

# 4. Two-dimensional array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\n2D Array:")
print(matrix)

# 5. Array properties
print("\nShape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Size:", matrix.size)

# 6. Matrix operations
print("\nTranspose:")
print(matrix.T)

print("\nMatrix Addition:")
print(matrix + matrix)

# 7. Reshaping
arr = np.arange(1, 10)
reshaped = arr.reshape(3, 3)

print("\nReshaped Array:")
print(reshaped)
