#Project 1: Sales Forecasting with Linear Regression

import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# load CSV data
df = pd.read_csv("sales_data.csv")
df['date'] = pd.to_datetime(df['date'], dayfirst=True)  # FIXED: handles dates like "13-01-2023"

# handle missing values
df = df.dropna(subset=['date', 'revenue', 'quantity', 'product']).copy()
df['quantity'] = df['quantity'].fillna(df['quantity'].median())

# optional: aggregate if multiple transactions per day per product
df = df.groupby(['date', 'product']).agg({'quantity': 'sum', 'revenue': 'sum'}).reset_index()

# feature engineering
df['dayofyear'] = df['date'].dt.dayofyear
df['year'] = df['date'].dt.year

# one-hot encode product field
df = pd.get_dummies(df, columns=['product'], drop_first=True)
feature_cols = ['dayofyear', 'year'] + [col for col in df.columns if col.startswith('product_')]

# train-test split
train_df = df.iloc[:-60]
test_df = df.iloc[-60:]
X_train = train_df[feature_cols]
y_train = train_df['revenue']
X_test = test_df[feature_cols]
y_test = test_df['revenue']

# model training
model = LinearRegression()
model.fit(X_train, y_train)

# prediction and evaluation
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)

# forecasting future values
future_dates = pd.date_range(start=df['date'].max() + pd.Timedelta(days=1), periods=30, freq='D')
future_df = pd.DataFrame({'date': future_dates})
future_df['dayofyear'] = future_df['date'].dt.dayofyear
future_df['year'] = future_df['date'].dt.year

# replicate dummy columns
for col in feature_cols:
    if col not in future_df.columns:
        future_df[col] = 0

future_df['revenue_pred'] = model.predict(future_df[feature_cols])

# plotting results
plt.figure(figsize=(12, 4))
plt.plot(df['date'], df['revenue'], label='actual')
plt.plot(test_df['date'], y_pred, label='predicted', color='red')
plt.plot(future_df['date'], future_df['revenue_pred'], label='forecast', color='green', linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()

# outputs
print(df.head())
print('MAE:', mae)
print(future_df.head())

# save forecast to CSV
future_df.to_csv('30_day_forecast.csv', index=False)