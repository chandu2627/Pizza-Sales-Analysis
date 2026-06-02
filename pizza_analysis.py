# Pizza Sales Analysis - Python
import pandas as pd

# Load dataset
df = pd.read_csv('pizza_sales.csv')

# Basic analysis
print("Total Orders:", len(df))
print("Total Revenue:", df['total_price'].sum())
print("Top Pizzas:\n", df.groupby('pizza_name')['total_price'].sum().sort_values(ascending=False).head(5))
