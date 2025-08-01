# Import necessary libraries
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

# --- 1. Data Cleaning and Preprocessing ---
print("--- Step 1: Data Cleaning and Preprocessing ---")

# Load the dataset
try:
    df = pd.read_csv('online_retail.csv', encoding='ISO-8859-1')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'online_retail.csv' not found. Please ensure the file is in the correct directory.")
    exit()

# Initial Data Inspection
print("\nInitial DataFrame Info:")
df.info()

# Handle Missing Values: Drop rows with missing CustomerID or Description
df.dropna(subset=['CustomerID', 'Description'], inplace=True)
print("\nRows with missing CustomerID or Description have been removed.")

# Remove Duplicates
df.drop_duplicates(inplace=True)
print("Duplicate rows have been removed.")

# Correct Data Types: Convert 'InvoiceDate' to datetime objects
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
print("Converted 'InvoiceDate' to datetime objects.")

# Filter Out Irrelevant Data: Remove transactions with non-positive Quantity
df = df[df['Quantity'] > 0]
print("Removed transactions with non-positive quantity.")

print("\n--- Data Cleaning Complete. Final DataFrame Info: ---")
df.info()


# --- 2. Feature Engineering ---
print("\n\n--- Step 2: Feature Engineering ---")

# Calculate Monetary Value: Create a 'TotalPrice' column
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
print("Created 'TotalPrice' column.")

# Extract Temporal Features
df['InvoiceDayOfWeek'] = df['InvoiceDate'].dt.day_name()
df['InvoiceMonth'] = df['InvoiceDate'].dt.month_name()
df['InvoiceHour'] = df['InvoiceDate'].dt.hour
print("Extracted temporal features: Day of Week, Month, and Hour.")

# Calculate RFM Features (Recency, Frequency, Monetary)
# Define a reference date as one day after the last transaction date
reference_date = df['InvoiceDate'].max() + dt.timedelta(days=1)
rfm_df = df.groupby('CustomerID').agg(
    Recency=('InvoiceDate', lambda date: (reference_date - date.max()).days),
    Frequency=('InvoiceNo', 'nunique'),
    Monetary=('TotalPrice', 'sum')
).reset_index()
print("\nRFM features calculated. Preview of RFM DataFrame:")
print(rfm_df.head())


# --- 3. Univariate Analysis ---
print("\n\n--- Step 3: Univariate Analysis ---")

# Distribution of Customer Activity (Frequency)
customer_activity_dist = rfm_df['Frequency'].value_counts().sort_index().head(20)
print("\nTop 20 most frequent number of purchases per customer:")
print(customer_activity_dist)

# Distribution of Product Popularity
product_popularity = df['Description'].value_counts().head(10)
print("\nTop 10 most popular products:")
print(product_popularity)

# Distribution of Monetary Value (Histograms)
plt.figure(figsize=(12, 6))
plt.hist(df['TotalPrice'], bins=50, color='skyblue', edgecolor='black')
plt.title('Distribution of Total Price per Transaction')
plt.xlabel('Total Price ($)')
plt.ylabel('Frequency')
plt.yscale('log')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('total_price_distribution.png')
plt.close() # Close plot to prevent overlap

plt.figure(figsize=(12, 6))
plt.hist(rfm_df['Monetary'], bins=50, color='lightgreen', edgecolor='black')
plt.title('Distribution of Total Monetary Value per Customer')
plt.xlabel('Total Monetary Value ($)')
plt.ylabel('Frequency')
plt.yscale('log')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('customer_monetary_distribution.png')
plt.close()

# Geographical Analysis
country_transactions = df.groupby('Country')['InvoiceNo'].nunique().sort_values(ascending=False)
print("\nTop 10 countries by number of transactions:")
print(country_transactions.head(10))


# --- 4. Bivariate and Multivariate Analysis ---
print("\n\n--- Step 4: Bivariate and Multivariate Analysis ---")

# Time-Series Analysis: Daily Transaction Volume
daily_transactions = df.groupby(df['InvoiceDate'].dt.date)['InvoiceNo'].nunique().reset_index()
daily_transactions.columns = ['Date', 'Transactions']

# Convert date to string for Altair compatibility
daily_transactions['Date'] = daily_transactions['Date'].astype(str)

# Create an interactive line chart with Altair
line_chart = alt.Chart(daily_transactions).mark_line().encode(
    x=alt.X('Date:T', title='Date'),
    y=alt.Y('Transactions:Q', title='Number of Transactions'),
    tooltip=[
        alt.Tooltip('Date', title='Date'),
        alt.Tooltip('Transactions', title='Number of Transactions')
    ]
).properties(
    title='Daily Transaction Volume Over Time'
).interactive()
line_chart.save('daily_transaction_volume.json')
print("\nAltair chart 'daily_transaction_volume.json' saved.")

# Customer-Product Relationship (Simple Market Basket Analysis)
# Find pairs of products purchased together most frequently
product_pairs = df.groupby('InvoiceNo')['Description'].apply(list)
frequent_pairs = {}
for products in product_pairs:
    products.sort()
    for i in range(len(products)):
        for j in range(i + 1, len(products)):
            pair = (products[i], products[j])
            frequent_pairs[pair] = frequent_pairs.get(pair, 0) + 1

# Get the top 5 most frequent pairs
sorted_pairs = sorted(frequent_pairs.items(), key=lambda item: item[1], reverse=True)
print("\nTop 5 most frequently purchased product pairs:")
for pair, count in sorted_pairs[:5]:
    print(f"  - {pair[0]} & {pair[1]}: {count} times")

print("\n--- EDA Complete ---")
print("Histograms of monetary distributions and a daily transaction volume chart have been saved.")
