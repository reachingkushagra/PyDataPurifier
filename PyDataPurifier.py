import pandas as pd
import numpy as np
import time
import openpyxl
import os
import random

def data_cleaning_master(data_path, data_name):
    print("Thank you for giving the details!")
    
    sec = random.randint(1, 4)
    print(f"Please wait for {sec}seconds! Checking file path")
    time.sleep(sec)
    
    # checking if the path exists
    if not os.path.exists(data_path):
        print("Incorrect path! Try again with correct path")
        return
    else:
        # checking the file type
        if data_path.endswith('.csv'):
            print('Dataset is csv!')
            data = pd.read_csv(data_path, encoding_errors='ignore')
        elif data_path.endswith('.xlsx'):
            print('Dataset is excel file!')
            data = pd.read_excel(data_path)
        else:
            print("Unknown file type")
            return
            
    # print delay message
    sec = random.randint(1, 4)
    print(f"Please wait for {sec}seconds! Checking total columns and rows")
    time.sleep(sec)
            
    # showing number of records
    print(f"Dataset contains total rows: {data.shape[0]} \nTotal Columns: {data.shape[1]}")

    # start cleaning
    sec = random.randint(1, 4)
    print(f"Please wait for {sec}seconds! Checking total duplicates")
    time.sleep(sec)
    
    # checking duplicates
    duplicates = data.duplicated()
    total_duplicate = duplicates.sum()

    print(f"Datasets has total duplicate records: {total_duplicate}")

    # saving duplicates
    sec = random.randint(1, 4)
    print(f"Please wait for {sec}seconds! Saving duplicate rows")
    time.sleep(sec)

    if total_duplicate > 0:
        deplicate_records = data[duplicates]
        deplicate_records.to_csv(f'{data_name}_duplicates.csv', index=None)

    # deleting duplicates
    data = data.drop_duplicates()

    # print delay message
    sec = random.randint(1, 10)
    print(f"Please wait for {sec}seconds! Checking for missing values")
    time.sleep(sec)

    # find missing values
    total_missing_value = data.isnull().sum().sum()
    missing_value_by_columns = data.isnull().sum()

    print(f"Dataset has Total missing value: {total_missing_value}")
    print(f"Dataset contains missing values by columns:\n{missing_value_by_columns}")

    # filling missing values for numeric columns
    sec = random.randint(1, 6)
    print(f"Please wait for {sec}seconds! Cleaning datasets")
    time.sleep(sec)

    # Fill missing values for numeric columns
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

    # Drop rows with missing values for non-numeric columns
    non_numeric_cols = data.select_dtypes(exclude=[np.number]).columns
    for col in non_numeric_cols:
        data.dropna(subset=[col], inplace=True)

    # print delay message
    sec = random.randint(1, 5)
    print(f"Please wait for {sec}seconds! Exporting cleaned datasets")
    time.sleep(sec)

    # cleaned data
    print(f"Congrats! Dataset is cleaned! \nNumber of Rows: {data.shape[0]} Number of columns: {data.shape[1]}")

    # saving the cleaned dataset
    data.to_csv(f'{data_name}_Clean_data.csv', index=None)
    print("Dataset is saved!")

if __name__ == "__main__":
    print("Welcome to Data Cleaning Master!")
    
    # ask path and file name
    data_path = input("Please enter dataset path: ")
    data_name = input("Please enter dataset name: ")
    
    # calling the function
    data_cleaning_master(data_path, data_name)
