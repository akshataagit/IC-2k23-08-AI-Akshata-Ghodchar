
import torch
import torch.nn as nn
import torch.optim as optim

# Set random seed
torch.manual_seed(42)

# 1. Prepare dataset
# Two input features and binary output

X = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.2, 0.3],
    [0.3, 0.8],
    [0.8, 0.2],
    [0.9, 0.9]
])

Y = torch.tensor([
    [0.0],
    [0.0],
    [0.0],
    [1.0],
    [0.0],
    [1.0],
    [1.0],
    [1.0]
])

print("Input Dataset:\n", X)
print("Target Output:\n", Y)

# 2. Define Neural Network
class NeuralNetwork(nn.Module):

    def __init__(self):
        super(NeuralNetwork, self).__init__()

        # Input layer to hidden layer
        self.hidden = nn.Linear(2, 8)

        # Hidden layer to output layer
        self.output = nn.Linear(8, 1)

        self.relu = nn.ReLU()

    def forward(self, x):

        x = self.hidden(x)
        x = self.relu(x)
        x = self.output(x)

        return x


# 3. Create model
model = NeuralNetwork()

# 4. Define loss function
criterion = nn.BCEWithLogitsLoss()

# 5. Define optimizer
optimizer = optim.Adam(model.parameters(), lr=0.05)

# 6. Train the neural network
epochs = 1000

for epoch in range(epochs):

    # Forward propagation
    outputs = model(X)

    # Calculate loss
    loss = criterion(outputs, Y)

    # Clear gradients
    optimizer.zero_grad()

    # Backpropagation
    loss.backward()

    # Update weights
    optimizer.step()

    if (epoch + 1) % 200 == 0:
        print(
            f"Epoch [{epoch+1}/{epochs}], "
            f"Loss: {loss.item():.6f}"
        )

# 7. Test the model
print("\nModel Predictions:")

with torch.no_grad():

    outputs = model(X)

    # Convert logits into probabilities
    probabilities = torch.sigmoid(outputs)

    # Convert probabilities into classes
    predicted = (probabilities >= 0.5).float()

    for i in range(len(X)):
        print(
            f"Input: {X[i].tolist()}, "
            f"Actual: {Y[i].item():.0f}, "
            f"Predicted: {predicted[i].item():.0f}"
        )

# 8. Calculate accuracy
correct = (predicted == Y).sum().item()
accuracy = (correct / len(Y)) * 100

print("\nModel Accuracy:", accuracy, "%")

print("\nNeural Network Training Completed Successfully!")
