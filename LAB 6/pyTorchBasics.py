
import torch

# 1. Creating tensors
print("1. Tensor Creation")

a = torch.tensor([1, 2, 3, 4, 5])
b = torch.tensor([10, 20, 30, 40, 50])

print("Tensor A:", a)
print("Tensor B:", b)

# 2. Creating special tensors
print("\n2. Special Tensors")

zeros = torch.zeros(2, 3)
ones = torch.ones(2, 3)
random_tensor = torch.rand(2, 3)

print("Zeros:\n", zeros)
print("Ones:\n", ones)
print("Random Tensor:\n", random_tensor)

# 3. Tensor operations
print("\n3. Tensor Operations")

print("Addition:", a + b)
print("Subtraction:", b - a)
print("Multiplication:", a * b)
print("Division:", b / a)

# 4. Matrix multiplication
print("\n4. Matrix Multiplication")

m1 = torch.tensor([[1, 2], [3, 4]])
m2 = torch.tensor([[5, 6], [7, 8]])

result = torch.matmul(m1, m2)

print("Matrix 1:\n", m1)
print("Matrix 2:\n", m2)
print("Result:\n", result)

# 5. Tensor reshaping
print("\n5. Tensor Reshaping")

x = torch.arange(1, 7)
reshaped = x.reshape(2, 3)

print("Original Tensor:", x)
print("Reshaped Tensor:\n", reshaped)

# 6. Indexing and slicing
print("\n6. Indexing and Slicing")

print("First Element:", a[0])
print("Last Element:", a[-1])
print("First Three Elements:", a[:3])

# 7. Automatic Differentiation
print("\n7. Automatic Differentiation")

x = torch.tensor(3.0, requires_grad=True)

y = x ** 2 + 2 * x + 1

y.backward()

print("Value of x:", x.item())
print("Value of y:", y.item())
print("Gradient of x:", x.grad.item())

print("\nPyTorch Basics Completed Successfully!")
