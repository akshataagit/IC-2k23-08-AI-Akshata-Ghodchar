
# Experiment 1: PyTorch Basics

## Problem Statement
To study the fundamentals of PyTorch and perform basic tensor operations, matrix multiplication, reshaping, indexing, slicing, and automatic differentiation.

## Objective
- Understand PyTorch and its applications in Machine Learning.
- Learn how to create tensors.
- Perform mathematical operations on tensors.
- Understand matrix multiplication.
- Learn tensor reshaping and indexing.
- Understand automatic differentiation using Autograd.

## Requirements
- Python 3.x
- PyTorch
- NumPy

## Installation
Install PyTorch using:

```bash
pip install torch numpy
```

## Algorithm / Approach
1. Import the PyTorch library.
2. Create tensors using torch.tensor().
3. Create zero, one, and random tensors.
4. Perform addition, subtraction, multiplication, and division.
5. Perform matrix multiplication using torch.matmul().
6. Reshape tensors using reshape().
7. Perform indexing and slicing.
8. Use requires_grad=True to enable gradient tracking.
9. Use backward() to calculate gradients.
10. Display the results.

## Functions Used
- torch.tensor()
- torch.zeros()
- torch.ones()
- torch.rand()
- torch.arange()
- torch.matmul()
- reshape()
- backward()

## Output
The program successfully demonstrates tensor creation, mathematical operations, matrix multiplication, reshaping, indexing, slicing, and automatic differentiation.

## Result
Successfully implemented basic PyTorch operations and understood the working of tensors and automatic differentiation.




# Experiment 2: Linear Regression Using PyTorch

## Problem Statement
To implement a Linear Regression model using PyTorch for predicting continuous values based on input data.

## Objective
- Understand the concept of Linear Regression.
- Implement a regression model using PyTorch.
- Understand loss functions and optimizers.
- Learn forward propagation and backpropagation.
- Predict outputs for new input values.
- Visualize the regression line.

## Requirements
- Python 3.x
- PyTorch
- Matplotlib

## Installation

```bash
pip install torch matplotlib
```

## Theory

Linear Regression is a supervised machine learning algorithm
used to predict continuous numerical values.

The mathematical equation is:

y = mx + c

Where:
- y = Predicted output
- x = Input variable
- m = Weight or slope
- c = Bias or intercept

## Algorithm / Approach

1. Import PyTorch, Matplotlib, and required libraries.
2. Prepare input and target training data.
3. Define the Linear Regression model using nn.Linear().
4. Define Mean Squared Error as the loss function.
5. Initialize the SGD optimizer.
6. Perform forward propagation.
7. Calculate the loss.
8. Clear previous gradients.
9. Perform backpropagation using backward().
10. Update model parameters using optimizer.step().
11. Train the model for multiple epochs.
12. Predict values for new inputs.
13. Visualize actual data and the predicted regression line.

## Functions Used

- nn.Linear()
- nn.MSELoss()
- optim.SGD()
- optimizer.zero_grad()
- loss.backward()
- optimizer.step()
- torch.no_grad()
- plt.scatter()
- plt.plot()

## Output

The model learns the relationship between input and
output data and predicts values for new inputs.

The learned weight approaches 2 and bias approaches 1.

## Result

Successfully implemented Linear Regression using
PyTorch and predicted continuous values with the
help of a trained model.



# Experiment 3: Neural Network Fundamentals Using PyTorch

## Problem Statement
To implement a basic Artificial Neural Network (ANN) using PyTorch and understand its architecture, forward propagation, backpropagation, activation functions, loss functions, and optimization.

## Objective
- Understand the fundamentals of Artificial Neural Networks.
- Learn the architecture of a neural network.
- Understand input, hidden, and output layers.
- Implement a neural network using PyTorch.
- Understand forward propagation and backpropagation.
- Train a model using an optimizer.
- Perform binary classification.

## Requirements
- Python 3.x
- PyTorch

## Installation

```bash
pip install torch
```

## Theory

An Artificial Neural Network (ANN) is a machine learning
model inspired by the structure of the human brain.

It consists of interconnected artificial neurons organized
into different layers.

### Main Components

1. Input Layer:
   Receives input features from the dataset.

2. Hidden Layer:
   Processes input using weights, biases, and activation
   functions.

3. Output Layer:
   Produces the final prediction.

### Important Concepts

- Forward Propagation: Passing input data through the
  network to generate predictions.

- Backpropagation: Calculating gradients to update
  network weights.

- ReLU: Activation function that introduces
  non-linearity.

- Loss Function: Measures the difference between
  actual and predicted outputs.

- Optimizer: Updates weights to minimize the loss.

## Algorithm / Approach

1. Import PyTorch and required libraries.
2. Prepare input features and target labels.
3. Define a Neural Network class using nn.Module.
4. Create an input layer, hidden layer, and output layer.
5. Apply the ReLU activation function.
6. Initialize the neural network model.
7. Define BCEWithLogitsLoss as the loss function.
8. Initialize the Adam optimizer.
9. Perform forward propagation.
10. Calculate the loss.
11. Clear existing gradients.
12. Perform backpropagation.
13. Update weights using the optimizer.
14. Repeat training for multiple epochs.
15. Generate predictions using the trained model.
16. Calculate classification accuracy.

## Functions Used

- nn.Module
- nn.Linear()
- nn.ReLU()
- nn.BCEWithLogitsLoss()
- optim.Adam()
- optimizer.zero_grad()
- loss.backward()
- optimizer.step()
- torch.sigmoid()
- torch.no_grad()

## Output

The neural network is trained using the given dataset.
It generates predictions for each input and calculates
the classification accuracy.

## Result

Successfully implemented an Artificial Neural Network
using PyTorch and understood its architecture,
forward propagation, backpropagation, and training process.
