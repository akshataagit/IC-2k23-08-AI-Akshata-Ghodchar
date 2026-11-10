
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# Set random seed for reproducibility
torch.manual_seed(42)

# 1. Prepare training data
# Relationship: y = 2x + 1

X = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
Y = torch.tensor([[3.0], [5.0], [7.0], [9.0], [11.0]])

print("Input Data:\n", X)
print("Target Data:\n", Y)

# 2. Define Linear Regression Model
model = nn.Linear(1, 1)

# 3. Define Loss Function
criterion = nn.MSELoss()

# 4. Define Optimizer
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 5. Train the model
epochs = 1000

for epoch in range(epochs):

    # Forward propagation
    predictions = model(X)

    # Calculate loss
    loss = criterion(predictions, Y)

    # Clear previous gradients
    optimizer.zero_grad()

    # Backpropagation
    loss.backward()

    # Update parameters
    optimizer.step()

    if (epoch + 1) % 200 == 0:
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.6f}")

# 6. Display learned parameters
weight = model.weight.item()
bias = model.bias.item()

print("\nTraining Completed!")
print("Learned Weight:", round(weight, 4))
print("Learned Bias:", round(bias, 4))

# 7. Make predictions
test_input = torch.tensor([[6.0], [7.0], [8.0]])

with torch.no_grad():
    test_output = model(test_input)

print("\nPredictions:")
for i in range(len(test_input)):
    print(
        f"Input: {test_input[i].item()}, "
        f"Predicted Output: {test_output[i].item():.2f}"
    )

# 8. Visualize results
with torch.no_grad():
    predicted = model(X)

plt.scatter(X.numpy(), Y.numpy(), label="Actual Data")
plt.plot(X.numpy(), predicted.numpy(), color="red",
         label="Regression Line")

plt.xlabel("Input (X)")
plt.ylabel("Output (Y)")
plt.title("Linear Regression Using PyTorch")
plt.legend()
plt.grid(True)
plt.show()
