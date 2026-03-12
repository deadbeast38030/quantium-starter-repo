import pandas as pd
import os

# Load all 3 CSV files
df0 = pd.read_csv('data/daily_sales_data_0.csv', header=None)
df1 = pd.read_csv('data/daily_sales_data_1.csv', header=None)
df2 = pd.read_csv('data/daily_sales_data_2.csv', header=None)

# Combine all 3 files into one
df = pd.concat([df0, df1, df2], ignore_index=True)

# Name the columns
df.columns = ['product', 'price', 'quantity', 'date', 'region']

# Keep only Pink Morsel rows
df = df[df['product'] == 'pink morsel']

# Clean price column (remove $ sign) and convert to number
df['price'] = df['price'].str.replace('$', '').astype(float)
df['quantity'] = df['quantity'].astype(int)

# Calculate sales = price x quantity
df['sales'] = df['price'] * df['quantity']

# Keep only the 3 required columns
df = df[['sales', 'date', 'region']]

# Save to output file
df.to_csv('data/output.csv', index=False)

print("Done! output.csv created successfully!")
print(df.head())
