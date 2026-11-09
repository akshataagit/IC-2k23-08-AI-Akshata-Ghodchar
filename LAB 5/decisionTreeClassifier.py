# Decision Tree Classifier

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Step 1: Load Iris Dataset
iris = load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

print("DECISION TREE CLASSIFIER")
print("\nDataset Information:")
print("Total Records:", len(X))
print("Features:", iris.feature_names)
print("Classes:", iris.target_names)

# Step 2: Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Records:", len(X_train))
print("Testing Records:", len(X_test))

# Step 3: Create Decision Tree Model
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

# Step 4: Train Model
model.fit(X_train, y_train)

print("\nModel Trained Successfully!")

# Step 5: Make Predictions
y_pred = model.predict(X_test)

print("\nActual Values:")
print(y_test.tolist())

print("\nPredicted Values:")
print(y_pred.tolist())

# Step 6: Feature Importance
print("\nFeature Importance:")

for feature, importance in zip(
    iris.feature_names,
    model.feature_importances_
):
    print(feature, ":", round(importance, 4))

# Step 7: Visualize Decision Tree
plt.figure(figsize=(14, 8))

plot_tree(
    model,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    rounded=True
)

plt.title("Decision Tree Classifier")
plt.show()

# Step 8: Predict New Data
new_data = pd.DataFrame(
    [[5.1, 3.5, 1.4, 0.2]],
    columns=iris.feature_names
)

prediction = model.predict(new_data)

print("\nNew Data Prediction:")
print("Predicted Flower:", iris.target_names[prediction[0]])

print("\nProgram Executed Successfully!")