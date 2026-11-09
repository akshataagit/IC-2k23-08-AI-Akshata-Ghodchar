# Decision Tree Classifier and Model Evaluation

## 1. Problem Statement

To implement a Decision Tree Classifier using Python and evaluate its performance using different model evaluation metrics.

The Decision Tree algorithm is a supervised machine learning algorithm used for classification and regression problems. In this experiment, the Iris dataset is used to train a Decision Tree Classifier and predict the category of flowers.

The performance of the trained model is evaluated using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix.

## 2. Objectives

- To understand the concept of supervised machine learning.
- To implement a Decision Tree Classifier using Scikit-learn.
- To load and understand the Iris dataset.
- To divide the dataset into training and testing sets.
- To train a Decision Tree model.
- To make predictions using the trained model.
- To evaluate model performance using different evaluation metrics.
- To visualize the decision tree and confusion matrix.

## 3. Dataset Description

The experiment uses the built-in Iris dataset provided by Scikit-learn.

The dataset contains information about three types of Iris flowers:

1. Iris Setosa
2. Iris Versicolor
3. Iris Virginica

It contains 150 records and four input features:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The target variable represents the flower category.

## 4. Algorithm / Approach

### A. Data Loading

1. Import the required libraries.
2. Load the Iris dataset using Scikit-learn.
3. Separate the independent features (X) and dependent target variable (y).
4. Display the dataset information.

### B. Data Splitting

1. Divide the dataset into training and testing sets.
2. Use 80% of the data for training.
3. Use 20% of the data for testing.
4. Use stratified splitting to maintain class proportions.

### C. Decision Tree Classifier

1. Create a DecisionTreeClassifier object.
2. Set the splitting criterion to Gini Index.
3. Set the maximum tree depth to 3.
4. Train the model using the training dataset.
5. Predict the output using testing data.

### D. Model Evaluation

1. Calculate Accuracy.
2. Calculate Precision.
3. Calculate Recall.
4. Calculate F1-Score.
5. Generate the Classification Report.
6. Generate the Confusion Matrix.
7. Display feature importance.
8. Visualize the Decision Tree and Confusion Matrix.

### E. New Data Prediction

1. Accept or define new flower measurements.
2. Pass the measurements to the trained model.
3. Predict the flower category.
4. Display the predicted result.

## 5. Pseudocode

```text
START

Load Iris Dataset

Separate Features (X) and Target (Y)

Split Dataset into Training and Testing Sets

Create Decision Tree Classifier

Train Model using Training Data

Predict Results using Testing Data

Calculate:
    Accuracy
    Precision
    Recall
    F1-Score

Generate Confusion Matrix

Generate Classification Report

Display Feature Importance

Visualize Decision Tree

Predict New Data

STOP
```

## 6. Sample Output

```text
DECISION TREE CLASSIFIER AND MODEL EVALUATION

Dataset Information:
Total Records: 150
Total Features: 4

Target Classes:
['setosa' 'versicolor' 'virginica']

Training Records: 120
Testing Records: 30

Decision Tree Model Trained Successfully!

----- MODEL EVALUATION RESULTS -----

Accuracy : 96.67 %
Precision: 96.97 %
Recall   : 96.67 %
F1-Score : 96.66 %

----- CONFUSION MATRIX -----

[[10  0  0]
 [ 0  9  1]
 [ 0  0 10]]
```

### Visualization Output

The program generates two graphical outputs:

1. **Decision Tree Visualization:** Displays the decision-making structure, conditions, branches, and predicted classes.
2. **Confusion Matrix Visualization:** Displays the correctly and incorrectly classified observations for each flower category.

### New Data Prediction

```text
----- NEW DATA PREDICTION -----

Input Features: [[5.1, 3.5, 1.4, 0.2]]

Predicted Flower: setosa

Program Executed Successfully!
```

*Note: The evaluation values above correspond to the specified Iris dataset split and model configuration.*

## 7. Model Evaluation Metrics

### Accuracy

Accuracy measures the percentage of total predictions that are correct.

### Precision

Precision measures how many observations predicted as positive actually belong to the positive class.

### Recall

Recall measures how many actual positive observations are correctly identified by the model.

### F1-Score

F1-Score is the harmonic mean of Precision and Recall. It provides a balance between both metrics.

### Confusion Matrix

A Confusion Matrix is a table used to compare actual and predicted classifications. It helps identify correct and incorrect predictions for each class.

## 8. Time and Space Complexity

Let:
- N = Number of training samples.
- F = Number of features.
- D = Maximum depth of the decision tree.

| Operation | Complexity |
|---|---|
| Dataset splitting | O(N) |
| Decision Tree Training | Approximately O(F × N × log N) per typical balanced-tree analysis |
| Prediction | O(D) per sample |
| Model Evaluation | O(N) for a fixed number of classes |
| Confusion Matrix | O(N) |

The exact training complexity depends on the tree structure, implementation, and dataset.

## 9. Applications

- Medical diagnosis.
- Customer classification.
- Fraud detection.
- Credit risk analysis.
- Student performance prediction.
- Email spam detection.
- Business decision-making.
- Predictive analytics.

## 10. Conclusion

In this experiment, a Decision Tree Classifier was successfully implemented using Python and Scikit-learn.

The Iris dataset was divided into training and testing sets, and the classifier was trained to predict different flower categories.

The model was evaluated using Accuracy, Precision, Recall, F1-Score, Classification Report, and Confusion Matrix.

The experiment demonstrates how machine learning models can be trained, tested, evaluated, and visualized for classification problems.