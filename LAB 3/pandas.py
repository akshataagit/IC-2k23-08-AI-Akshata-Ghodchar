
import pandas as pd

# 1. Create a Pandas Series
marks = pd.Series([85, 90, 78, 95, 88])

print("Pandas Series:")
print(marks)

# 2. Create a DataFrame
data = {
    'Name': ['Amit', 'Riya', 'Rahul', 'Priya', 'Neha'],
    'Age': [20, 21, 19, 22, 20],
    'Marks': [85, 90, 78, 95, 88],
    'City': ['Indore', 'Bhopal', 'Indore',
             'Ujjain', 'Bhopal']
}

df = pd.DataFrame(data)

print("\nOriginal DataFrame:")
print(df)

# 3. Display first records
print("\nFirst 3 Records:")
print(df.head(3))

# 4. Display column names
print("\nColumn Names:")
print(df.columns)

# 5. Select a column
print("\nStudent Names:")
print(df['Name'])

# 6. Filter records
print("\nStudents with Marks Greater than 85:")
print(df[df['Marks'] > 85])

# 7. Sort records
print("\nSorted by Marks:")
print(df.sort_values(by='Marks'))

# 8. Add a new column
df['Result'] = df['Marks'].apply(
    lambda x: 'Pass' if x >= 40 else 'Fail'
)

print("\nAfter Adding Result Column:")
print(df)

# 9. Group data by city
print("\nAverage Marks by City:")
print(df.groupby('City')['Marks'].mean())

# 10. Save DataFrame
df.to_csv('student_data.csv', index=False)

print("\nData Saved Successfully!")
