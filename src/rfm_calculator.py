from sklearn.preprocessing import StandardScaler


# --- 3. Calculate RFM Features ---
print("Step 2: Calculating RFM features...")

# Set the reference date as one day after the last transaction date
reference_date = df['InvoiceDate'].max() + dt.timedelta(days=1)

# Calculate Recency, Frequency, and Monetary values for each customer
rfm_df = df.groupby('CustomerID').agg(
    # Recency: Calculate the number of days since the last purchase
    Recency=('InvoiceDate', lambda date: (reference_date - date.max()).days),
    # Frequency: Count the number of unique invoices
    Frequency=('InvoiceNo', 'nunique'),
    # Monetary: Sum the TotalPrice
    Monetary=('TotalPrice', 'sum')
).reset_index()

print("RFM features calculated. Preview of RFM DataFrame:")
print(rfm_df.head())
print("\n")


# --- 4. Standardize/Normalize RFM Values ---
print("Step 3: Standardizing RFM values for clustering...")

# Exclude 'CustomerID' and create a new DataFrame with only RFM values
rfm_values = rfm_df[['Recency', 'Frequency', 'Monetary']]

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit the scaler to the RFM values and transform the data
scaled_rfm = scaler.fit_transform(rfm_values)

# Create a new DataFrame with the standardized values and a CustomerID column
scaled_rfm_df = pd.DataFrame(scaled_rfm, columns=['Recency_Scaled', 'Frequency_Scaled', 'Monetary_Scaled'])
scaled_rfm_df['CustomerID'] = rfm_df['CustomerID']

print("RFM values have been standardized. Preview of the scaled DataFrame:")
print(scaled_rfm_df.head())
print("\n")

print("The final 'scaled_rfm_df' is now ready for clustering algorithms like K-Means.")