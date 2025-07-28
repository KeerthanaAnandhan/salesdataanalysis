import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style="whitegrid")
df = pd.read_csv('SampleSuperstore.csv', encoding='ISO-8859-1')
print(df.head())
# Check null values
print(df.isnull().sum())

# Drop duplicates
df.drop_duplicates(inplace=True)

# Convert 'Order Date' to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract Month and Year
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print(category_sales)
region_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
print(region_profit)
monthly_sales = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()
print(monthly_sales)
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
print(top_products)
category_sales.plot(kind='bar', title='Total Sales by Category', color='skyblue')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()
region_profit.plot(kind='bar', title='Profit by Region', color='salmon')
plt.ylabel('Profit')
plt.tight_layout()
plt.show()
# Pivot for line plot
pivot = monthly_sales.pivot(index='Month', columns='Year', values='Sales')
pivot.plot(marker='o', title='Monthly Sales Trend (All Years)')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()
