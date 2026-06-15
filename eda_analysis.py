import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel('ApexPlanet_DataAnalytics_Dataset.xlsx')

# Basic Info
print("=== DATASET INFO ===")
print(df.shape)
print(df.dtypes)
print(df.head())

# Missing Values
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# Descriptive Statistics
print("\n=== DESCRIPTIVE STATISTICS ===")
print(df.describe())

# 1. Sales by Category - Bar Chart
plt.figure(figsize=(10,6))
df.groupby('Category')['Total_Sales'].sum().plot(kind='bar', color='steelblue')
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_by_category.png')
plt.show()
print("Chart 1 saved!")

# 2. Monthly Sales Trend - Line Chart
plt.figure(figsize=(10,6))
df.groupby('Order_Date')['Total_Sales'].sum().plot(kind='line', marker='o', color='green')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('monthly_sales_trend.png')
plt.show()
print("Chart 2 saved!")

print("\n=== EDA COMPLETE ===")