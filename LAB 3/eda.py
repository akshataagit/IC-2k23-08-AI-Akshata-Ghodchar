
import pandas as pd
import numpy as np

# Create sample dataset
data = {
    'Name': ['Amit', 'Riya', 'Rahul', 'Priya', 'Neha'],
    'Age': [20, 21, 19, 22, 20],
    'Marks': [85, 90, 78, 95, 88],
    'Attendance': [90, 95, 80, 98, 92]
}

df = pd.DataFrame(data)

# Display dataset
print("Dataset:")
print(df)

# 1. Dataset information
print("\nDataset Information:")
print(df.info())

# 2. Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# 3. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 4. Check duplicate values
print("\nDuplicate Records:")
print(df.duplicated().sum())

# 5. Average marks
print("\nAverage Marks:")
print(df['Marks'].mean())

# 6. Maximum and minimum marks
print("\nMaximum Marks:")
print(df['Marks'].max())

print("\nMinimum Marks:")
print(df['Marks'].min())

# 7. Correlation
print("\nCorrelation:")
print(df[['Age', 'Marks', 'Attendance']].corr())

# 8. Sort data by marks
print("\nStudents Sorted by Marks:")
print(df.sort_values(by='Marks', ascending=False))
