## PyDataPurifier 🐍📊🧹
PyDataPurifier is an automated Python tool designed to streamline the process of data cleaning and preprocessing 🧑‍💻. Whether you're handling messy datasets from various sources 📊 or need to prepare data for machine learning models 🤖, PyDataPurifier simplifies the entire workflow. This tool ensures that your datasets are not only clean ✨ but also ready for insightful analysis 🔍, making data wrangling more efficient and less error-prone.

## Features ✨
  **1. Missing Data Imputation 🧹:**
  Automatically handles missing values in your dataset. For numeric columns, missing values are filled with the column's mean value, while for non-numeric columns, rows with missing values are removed, ensuring the data remains clean and consistent.
  🔧 Perfect for datasets with missing entries that could skew analysis.
  
  **2. Duplicate Records Handling 🛑:**
  Identifies duplicate rows in your dataset and removes them to ensure no redundancy in the data. It also saves duplicates in a separate file for review, ensuring that no important data is lost during cleaning.
  ⚠️ Prevents repetitive data entries from affecting your analysis or machine learning models.
  
  **3. Data Type Conversion 🔄:**
  Automatically converts columns to their appropriate data types (e.g., numeric columns to float, date strings to datetime), improving data consistency and compatibility with various tools and models.
  🔧 Ensures that all data is formatted correctly for further processing and analysis.
  
 **4. Flexible Input Support 📂:**
  Supports both .csv and .xlsx file formats, making it easier to work with a variety of data sources. 
  🌍 A versatile solution for handling diverse datasets from multiple sources.
  
  **5. Customizable Cleaning Process ⚙️:**
  Offers a highly customizable cleaning pipeline where you can choose which data cleaning steps to apply based on your dataset's needs. Whether it’s removing duplicates, handling missing values, or more complex transformations, you have full control.
  🛠️ Perfect for users with unique data processing requirements.

## Installation 🛠️
**1. Clone the repository:**

Navigate to your terminal and clone the repository to your local machine:

    git clone https://github.com/reachingkushagra/PyDataPurifier.git
**2. Download Python and Data Files:**

Go to the repository link to download the Python and data files.

    https://github.com/reachingkushagra/PyDataPurifier
Click on the Python file (e.g.,PyDataPurifier.py) and download it by selecting the "Raw" button and saving the file.
Download your data file (e.g., .csv or .xlsx) in the same way.

**3. Install Dependencies:**

After downloading the required files, open a terminal in the folder containing the files, and install the dependencies:

    pip install -r requirements.txt

## Usage 🚀
**1. Prepare Your Files**

Ensure that the Python script **(e.g., PyDataPurifier.py)** and your data file **(e.g., your_data.csv or your_data.xlsx)** are in the same folder or maintain a clear folder structure for easy reference.

**2. Run the Python Script**

Open your terminal (or command prompt) and navigate to the folder containing the Python script and data file.

Run the script by typing the following command:

    python PyDataPurifier.py
**3. Output**

After the script runs, the cleaned dataset will be saved as a new file in the same folder, typically named cleaned_data.csv or similar, depending on your script's configuration.

## Example 📂📸

**1️⃣ Original Dataset**
<img width="1405" alt="image" src="https://github.com/user-attachments/assets/2dd4936d-a4f6-49e2-8c2e-6317b7d68a3e" />

**2️⃣ PyDataPurifier running in the terminal:**
<img width="1399" alt="image" src="https://github.com/user-attachments/assets/84cdec07-f22c-45f6-9d8b-a705ad68fd42" />

**3️⃣ PyDataPurifier cleaned the data and saved the file.**
<img width="1398" alt="image" src="https://github.com/user-attachments/assets/ed5e28bc-0707-449a-be5c-9deda388da24" />

**4️⃣ It also saved another file containing duplicates.**
<img width="1256" alt="image" src="https://github.com/user-attachments/assets/a71ae767-acd5-4d75-ae89-14ca19f3419c" />

## Conclusion 🚀

PyDataPurifier is a powerful and user-friendly tool designed to streamline the data cleaning process. 🧹✨ It efficiently detects and removes duplicates, ensuring high-quality, structured data for analysis. By automating tedious data preprocessing tasks, it saves time and reduces human error, making it an essential tool for data professionals, analysts, and researchers
Whether you're working with small datasets or handling large-scale data pipelines, PyDataPurifier helps optimize workflows, improve data accuracy, and enhance productivity. 📊🔍 Its intuitive approach makes it accessible for both beginners and experienced users, allowing seamless integration into various data-driven projects.

**Let me know if you need any further refinements! 😊**
