# Model Evaluation using Machine Learning

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

# Step 1: Load Dataset
iris = load_iris()

X = iris.data
y = iris.target

print("MODEL EVALUATION")

# Step 2: Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Step 3: Train Model
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

model.fit(X_train, y_train)

print("\nModel Trained Successfully!")

# Step 4: Predict Values
y_pred = model.predict(X_test)

# Step 5: Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)

# Step 6: Calculate Precision
precision = precision_score(
    y_test, y_pred,
    average="weighted",
    zero_division=0
)

# Step 7: Calculate Recall
recall = recall_score(
    y_test, y_pred,
    average="weighted",
    zero_division=0
)

# Step 8: Calculate F1 Score
f1 = f1_score(
    y_test, y_pred,
    average="weighted",
    zero_division=0
)

# Step 9: Display Evaluation Results
print("\n----- EVALUATION RESULTS -----")

print("Accuracy :", round(accuracy * 100, 2), "%")
print("Precision:", round(precision * 100, 2), "%")
print("Recall   :", round(recall * 100, 2), "%")
print("F1-Score :", round(f1 * 100, 2), "%")

# Step 10: Classification Report
print("\n----- CLASSIFICATION REPORT -----")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names,
        zero_division=0
    )
)

# Step 11: Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\n----- CONFUSION MATRIX -----")
print(cm)

# Step 12: Visualize Confusion Matrix
display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)

display.plot(cmap="Blues")

plt.title("Model Evaluation - Confusion Matrix")
plt.show()

print("\nModel Evaluation Completed Successfully!")