import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel('ApexPlanet_DataAnalytics_Dataset.xlsx')

# 1. Correlation Heatmap
plt.figure(figsize=(10,6))
numeric_df = df[['Age', 'Quantity', 'Unit_Price', 'Total_Sales']]
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.show()
print("Heatmap saved!")

# 2. Scatter Plot - Unit Price vs Total Sales
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='Unit_Price', y='Total_Sales', hue='Category')
plt.title('Unit Price vs Total Sales by Category')
plt.tight_layout()
plt.savefig('scatter_price_sales.png')
plt.show()
print("Scatter plot saved!")

# 3. Box Plot - Sales by Category
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='Category', y='Total_Sales', palette='Set2')
plt.title('Sales Distribution by Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('boxplot_category.png')
plt.show()
print("Box plot saved!")

print("\n=== CORRELATION ANALYSIS COMPLETE ===")