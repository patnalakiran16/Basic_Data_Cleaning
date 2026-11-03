Student Data Cleaning Using Python and Pandas

Project Overview

This project demonstrates basic data cleaning techniques using Python and the Pandas library. A sample student dataset is created with missing values, duplicate records, and incorrect data types.

The main goal is to clean the dataset and make it suitable for further data analysis.

Objective

To understand and implement basic data cleaning operations, including:

- Handling missing values.
- Removing duplicate records.
- Correcting incorrect data types.
- Inspecting dataset information.
- Saving the original and cleaned datasets.

Technologies Used

- Python
- Pandas
- NumPy
- Jupyter Notebook

Dataset Description

The project uses a sample student dataset containing the following columns:

Column Name| Description
Student_ID| Unique student identification number
Name| Student name
Age| Student age
Gender| Student gender
Marks| Student examination marks
Attendance| Student attendance percentage
Join_Date| Student joining date

Data Cleaning Steps

1. Dataset Creation

Created a sample student dataset using Pandas.

2. Missing Value Detection

Used "isnull().sum()" to identify missing values.

3. Data Type Correction

Used "pd.to_numeric()" and "pd.to_datetime()" to convert columns into appropriate data types.

4. Handling Missing Values

Used the median method to fill missing numerical values and replaced missing text values with "Unknown".

5. Duplicate Removal

Used "drop_duplicates()" to remove duplicate records.

6. Index Resetting

Used "reset_index()" to organise the cleaned dataset.

7. Exporting Data

Saved the original and cleaned datasets as CSV files.

Files Generated

- "data_cleaning.ipynb" – Jupyter Notebook containing the Python code.
- "original_dataset.csv" – Original student dataset.
- "cleaned_dataset.csv" – Cleaned student dataset.

Expected Results

Description| Result
Original Records| 7
Duplicate Records Removed| 1
Final Records| 6
Missing Numerical Values| Handled
Incorrect Data Types| Corrected

How to Run the Project

1. Install Python on your system.
2. Install the required libraries:

pip install pandas numpy jupyter

3. Open Jupyter Notebook:

jupyter notebook

4. Open "data_cleaning.ipynb".
5. Run all the cells.
6. Check the generated CSV files.

Key Learning Outcomes

- Learned how to work with Pandas DataFrames.
- Understood missing-value handling techniques.
- Practised duplicate removal.
- Learned data type conversion.
- Gained practical experience in data preprocessing.

Conclusion

This project helped me understand the importance of data cleaning in data analysis. By handling missing values, removing duplicate records, and correcting data types, I learned how to prepare raw data for further analysis and machine learning applications.

---

Project Type: Python Internship Task
Domain: Data Analytics
Status: Completed