import pandas as pd
import numpy as np

# Creating a sample student dataset
data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 102],
    "Name": ["Kiran", "Ravi", "Priya", "Suresh", "Anu", "Rahul", "Ravi"],
    "Age": [23, 24, np.nan, 22, 21, "twenty", 24],
    "Gender": ["Male", "Male", "Female", "Male", "Female", "Male", "Male"],
    "Marks": [85, 90, 78, np.nan, 88, "eighty", 90],
    "Attendance": [90, 85, 95, 80, np.nan, 88, 85],
    "Join_Date": [
        "2026-06-01", "2026-06-02", "2026-06-03",
        "2026-06-04", "2026-06-05", "2026-06-06",
        "2026-06-02"
    ]
}

# Converting the data into a DataFrame
df = pd.DataFrame(data)

# Saving the original data
df.to_csv("original_dataset.csv", index=False)

print("Original Student Dataset:")
print(df)

# Checking the dataset details
print("\nDataset Information:")
df.info()

# Finding missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Converting columns into the correct data types
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
df["Attendance"] = pd.to_numeric(df["Attendance"], errors="coerce")

df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce")

# Filling missing values with the median
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Marks"] = df["Marks"].fillna(df["Marks"].median())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].median())

# Filling missing text values
df["Name"] = df["Name"].fillna("Unknown")
df["Gender"] = df["Gender"].fillna("Unknown")

# Removing duplicate records
df = df.drop_duplicates()

# Resetting the row numbers
df = df.reset_index(drop=True)

# Displaying the cleaned dataset
print("\nCleaned Student Dataset:")
print(df)

# Checking missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Saving the cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nFinal Dataset Information:")
df.info()

print("\nData Cleaning Completed Successfully!")
print("Original and cleaned datasets saved successfully.")
