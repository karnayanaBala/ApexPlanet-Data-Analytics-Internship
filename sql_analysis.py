import pandas as pd
import sqlite3

# Load dataset
df = pd.read_excel('ApexPlanet_DataAnalytics_Dataset.xlsx')

# Create SQLite database
conn = sqlite3.connect('sales_data.db')
df.to_sql('sales_data', conn, if_exists='replace', index=False)

print("=== Q1: Total Sales by Category ===")
q1 = pd.read_sql_query("""
SELECT Category, SUM(Total_Sales) AS Total_Revenue
FROM sales_data
GROUP BY Category
ORDER BY Total_Revenue DESC
""", conn)
print(q1)

print("\n=== Q2: Top 5 Customers by Sales ===")
q2 = pd.read_sql_query("""
SELECT Customer_Name, SUM(Total_Sales) AS Total_Spent
FROM sales_data
GROUP BY Customer_Name
ORDER BY Total_Spent DESC
LIMIT 5
""", conn)
print(q2)

print("\n=== Q3: Sales by Gender ===")
q3 = pd.read_sql_query("""
SELECT Gender, SUM(Total_Sales) AS Total_Sales,
COUNT(*) AS Total_Orders
FROM sales_data
GROUP BY Gender
""", conn)
print(q3)

print("\n=== Q4: Top 5 Products by Revenue ===")
q4 = pd.read_sql_query("""
SELECT Product, SUM(Total_Sales) AS Revenue
FROM sales_data
GROUP BY Product
ORDER BY Revenue DESC
LIMIT 5
""", conn)
print(q4)

print("\n=== Q5: Average Order Value by City ===")
q5 = pd.read_sql_query("""
SELECT City, ROUND(AVG(Total_Sales),2) AS Avg_Order_Value,
COUNT(*) AS Total_Orders
FROM sales_data
GROUP BY City
ORDER BY Avg_Order_Value DESC
LIMIT 10
""", conn)
print(q5)

conn.close()
print("\n=== SQL ANALYSIS COMPLETE ===")