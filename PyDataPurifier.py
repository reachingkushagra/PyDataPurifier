import pandas as pd
import numpy as np
import time
import os
import random
import streamlit as st

def data_cleaning_master(data, data_name):
    st.write("Thank you for providing the dataset!")
    st.write(f"Dataset contains {data.shape[0]} rows and {data.shape[1]} columns.")
    duplicates = data.duplicated()
    total_duplicate = duplicates.sum()
    st.write(f"Dataset contains {total_duplicate} duplicate rows.")
    if total_duplicate > 0:
        deplicate_records = data[duplicates]
        deplicate_records.to_csv(f'{data_name}_duplicates.csv', index=None)
        st.write(f"Duplicate rows saved as '{data_name}_duplicates.csv'")
    data = data.drop_duplicates()
    total_missing_value = data.isnull().sum().sum()
    missing_value_by_columns = data.isnull().sum()
    st.write(f"Total missing values: {total_missing_value}")
    st.write(f"Missing values by column:\n{missing_value_by_columns}")
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())
    non_numeric_cols = data.select_dtypes(exclude=[np.number]).columns
    for col in non_numeric_cols:
        data.dropna(subset=[col], inplace=True)
    st.write("Cleaning complete!")
    st.write(f"Cleaned dataset contains {data.shape[0]} rows and {data.shape[1]} columns.")
    return data

def main():
    st.title("PyDataPurifier: Automated Data Cleaning")
    st.sidebar.header("Upload Dataset")
    file = st.sidebar.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])
    if file is not None:
        file_extension = file.name.split('.')[-1]
        data_name = file.name.split('.')[0]
        if file_extension == 'csv':
            data = pd.read_csv(file, encoding_errors='ignore')
        elif file_extension == 'xlsx':
            data = pd.read_excel(file)
        else:
            st.error("Unsupported file type!")
            return
        st.write("Dataset Preview:")
        st.dataframe(data.head())
        if st.button("Clean Data"):
            cleaned_data = data_cleaning_master(data, data_name)
            st.write("Download the cleaned dataset:")
            st.download_button(
                label="Download Cleaned Data",
                data=cleaned_data.to_csv(index=False).encode(),
                file_name=f"{data_name}_Cleaned.csv",
                mime="text/csv"
            )

if __name__ == "__main__":
    main()
