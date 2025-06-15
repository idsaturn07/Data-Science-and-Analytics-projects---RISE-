#Project 5: E-Commerce Data Insights

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("ecommerce_data.csv")

# Convert order_time to datetime
df['order_time'] = pd.to_datetime(df['order_time'])

# Top 5 selling products
top_products = df.groupby('product')['quantity'].sum().sort_values(ascending=False).head(5)

# Top 5 users (most quantity ordered)
top_users = df.groupby('user_id')['quantity'].sum().sort_values(ascending=False).head(5)

# Average review score per product
avg_rating = df.groupby('product')['review_score'].mean().sort_values(ascending=False).head(5)

# Extract hour of order
df['order_hour'] = df['order_time'].dt.hour
orders_by_hour = df['order_hour'].value_counts().sort_index()

# --- Visualizations ---

# Bar chart: Top-selling products
plt.figure(figsize=(6, 4))
sns.barplot(x=top_products.values, y=top_products.index, hue=top_products.index, palette='Blues_d', legend=False)
plt.title("Top 5 Selling Products")
plt.xlabel("Quantity Sold")
plt.tight_layout()
plt.savefig("top_products.png")
plt.show()

# Pie chart: Top 5 users by quantity
plt.figure(figsize=(6, 6))
plt.pie(top_users.values, labels=top_users.index, autopct='%1.1f%%', startangle=90)
plt.title("Top 5 Users by Quantity Ordered")
plt.tight_layout()
plt.savefig("top_users.png")
plt.show()

# Line chart: Order volume by hour
plt.figure(figsize=(7, 4))
sns.lineplot(x=orders_by_hour.index, y=orders_by_hour.values, marker='o')
plt.title("Orders by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Orders")
plt.xticks(range(0, 24))
plt.tight_layout()
plt.savefig("orders_by_hour.png")
plt.show()

# Bar chart: Top-rated products
plt.figure(figsize=(6, 4))
sns.barplot(x=avg_rating.values, y=avg_rating.index, hue=avg_rating.index, palette='Greens_d', legend=False)
plt.title("Top 5 Products by Avg Review Score")
plt.xlabel("Avg Rating")
plt.tight_layout()
plt.savefig("top_rated_products.png")
plt.show()

print("\n✅ E-commerce data insights generated and visualized.")