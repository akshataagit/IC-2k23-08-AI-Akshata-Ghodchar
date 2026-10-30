
import pandas as pd
import numpy as np

# Create sample dataset
data = {
    'Name': ['Amit', 'Riya', 'Rahul', 'Priya', 'Amit'],
    'Age': [20, 21, np.nan, 22, 20],
    'Marks': [85, 90, 78, np.nan, 85],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male']
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# 1. Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

print("\nAfter Handling Missing Values:")
print(df)

# 2. Remove duplicate records
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)

# 3. Encode categorical data
df['Gender'] = df['Gender'].map({
    'Male': 0,
    'Female': 1
})

print("\nAfter Encoding:")
print(df)

# 4. Normalize Marks using Min-Max Scaling
df['Marks'] = (
    (df['Marks'] - df['Marks'].min()) /
    (df['Marks'].max() - df['Marks'].min())
)

print("\nAfter Normalization:")
print(df)

# Save processed dataset
df.to_csv("processed_data.csv", index=False)

print("\nPreprocessing Completed Successfully!")
