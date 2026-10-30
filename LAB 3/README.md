
# Experiment 8: Data Preprocessing

## Aim
To perform data preprocessing using Python.

## Introduction
Data preprocessing is the process of cleaning
and transforming raw data into a useful format.

It improves data quality and prepares data for
analysis and machine learning.

## Operations Performed

1. Handling Missing Values
2. Removing Duplicate Records
3. Encoding Categorical Data
4. Normalization of Numerical Data

## Functions Used

- fillna(): Handles missing values.
- drop_duplicates(): Removes duplicate records.
- map(): Converts categorical values into numbers.
- min-max scaling: Normalizes numerical values.
- to_csv(): Saves the processed dataset.

## Execution
python Experiment8.py

## Output
The missing values are replaced, duplicate
records are removed, categorical data is encoded,
and numerical data is normalized.

## Result
Data preprocessing was successfully performed
using Python and Pandas.



# Experiment 9: Exploratory Data Analysis (EDA)

## Aim
To perform Exploratory Data Analysis on a dataset
using Python and Pandas.

## Introduction
Exploratory Data Analysis (EDA) is the process
of examining and understanding datasets.

It helps identify patterns, trends, missing values,
outliers and relationships between variables.

## Operations Performed

1. Displaying the dataset.
2. Checking dataset information.
3. Generating statistical summaries.
4. Identifying missing values.
5. Checking duplicate records.
6. Calculating mean, maximum and minimum.
7. Finding correlation between variables.
8. Sorting records.

## Functions Used

- head()
- info()
- describe()
- isnull()
- duplicated()
- mean()
- max()
- min()
- corr()
- sort_values()

## Execution
python Experiment9.py

## Result
Exploratory Data Analysis was successfully
performed using Python and Pandas.




# Experiment 10: NumPy

## Aim
To perform numerical operations using NumPy
in Python.

## Introduction
NumPy stands for Numerical Python.

It is a Python library used for numerical
computations and scientific computing.

It provides support for multidimensional arrays,
mathematical functions and matrix operations.

## Operations Performed

1. Creating one-dimensional arrays.
2. Performing arithmetic operations.
3. Calculating sum, mean, maximum and minimum.
4. Creating two-dimensional arrays.
5. Finding array shape, size and dimensions.
6. Performing matrix addition.
7. Finding matrix transpose.
8. Reshaping arrays.

## Functions Used

- np.array()
- np.sum()
- np.mean()
- np.max()
- np.min()
- np.std()
- np.arange()
- reshape()
- transpose()

## Execution
python Experiment10.py

## Installation
pip install numpy

## Result
Basic numerical and mathematical operations
were successfully performed using NumPy.




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




# Experiment 12: Data Visualization

## Aim
To create different types of charts and graphs
using Python and Matplotlib.

## Introduction
Data Visualization is the graphical representation
of information and data.

It helps to understand patterns, trends and
relationships in a dataset.

## Charts Implemented

1. Bar Chart
2. Line Chart
3. Pie Chart
4. Scatter Plot
5. Histogram

## Functions Used

- plt.figure()
- plt.bar()
- plt.plot()
- plt.pie()
- plt.scatter()
- plt.hist()
- plt.title()
- plt.xlabel()
- plt.ylabel()
- plt.savefig()
- plt.show()

## Library Used
Matplotlib

## Execution
python Experiment12.py

## Installation
pip install matplotlib

## Output
Five different graphical representations are
generated and saved in the outputs folder.

## Result
Data visualization was successfully performed
using Python and Matplotlib.
