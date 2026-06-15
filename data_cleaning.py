import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('sales_data_sample.csv', encoding='latin1')

# 1. Basic Info
print("=== DATASET INFO ===")
print(df.shape)
print(df.dtypes)

# 2. Missing Values
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# 3. Duplicates
print("\n=== DUPLICATES ===")
print("Duplicate rows:", df.duplicated().sum())

# 4. Clean - Remove duplicates
df = df.drop_duplicates()

# 5. Fill missing values
df = df.fillna('Unknown')

# 6. Standardize column names
df.columns = df.columns.str.lower().str.strip()

# 7. Convert date column
df['orderdate'] = pd.to_datetime(df['orderdate'])

# 8. Save cleaned data
df.to_csv('cleaned_sales_data.csv', index=False)

print("\n=== CLEANING DONE ===")
print("Cleaned data saved!")
print(df.shape)