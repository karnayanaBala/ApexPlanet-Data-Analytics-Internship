-- Task 2: SQL Queries for Business Intelligence

-- Q1: Total Sales by Category
SELECT Category, SUM(Total_Sales) AS Total_Revenue
FROM sales_data
GROUP BY Category
ORDER BY Total_Revenue DESC;

-- Q2: Top 5 Customers by Sales
SELECT Customer_Name, SUM(Total_Sales) AS Total_Spent
FROM sales_data
GROUP BY Customer_Name
ORDER BY Total_Spent DESC
LIMIT 5;

-- Q3: Monthly Sales Trend
SELECT Order_Date, SUM(Total_Sales) AS Monthly_Sales
FROM sales_data
GROUP BY Order_Date
ORDER BY Order_Date;

-- Q4: Sales by Gender
SELECT Gender, SUM(Total_Sales) AS Total_Sales,
COUNT(*) AS Total_Orders
FROM sales_data
GROUP BY Gender;

-- Q5: Average Order Value by City
SELECT City, AVG(Total_Sales) AS Avg_Order_Value,
COUNT(*) AS Total_Orders
FROM sales_data
GROUP BY City
ORDER BY Avg_Order_Value DESC;

-- Q6: Top 5 Products by Revenue
SELECT Product, SUM(Total_Sales) AS Revenue
FROM sales_data
GROUP BY Product
ORDER BY Revenue DESC
LIMIT 5;

-- Q7: Age Group Analysis
SELECT 
CASE 
    WHEN Age < 25 THEN 'Young (18-24)'
    WHEN Age < 40 THEN 'Adult (25-39)'
    WHEN Age < 55 THEN 'Middle Age (40-54)'
    ELSE 'Senior (55+)'
END AS Age_Group,
COUNT(*) AS Customers,
SUM(Total_Sales) AS Total_Sales
FROM sales_data
GROUP BY Age_Group;