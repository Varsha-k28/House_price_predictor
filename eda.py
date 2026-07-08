import pandas as pd

# Load the dataset
data = pd.read_csv("dataset/train.csv")

# Display first 5 rows
print("\nFirst 5 Rows:")
print(data.head())

# Display dataset information
print("\nDataset Information:")
print(data.info())

# Display dataset shape
print("\nDataset Shape:")
print(data.shape)

# Display column names
print("\nColumn Names:")
print(data.columns.tolist())

# Display missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Display statistical summary
print("\nStatistical Summary:")
print(data.describe())