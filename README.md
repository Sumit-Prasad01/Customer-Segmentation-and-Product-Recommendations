# Customer-Segmentation-and-Product-Recommendations

```
shopper-spectrum/
│
├── 📁 data/
│   ├── raw/
│   │   └── ecommerce_data.csv          # Original dataset
│   ├── processed/
│   │   ├── cleaned_data.csv            # After preprocessing
│   │   └── rfm_features.csv            # RFM calculated features
│   └── sample/
│       └── sample_data.csv             # Small dataset for testing
│
├── 📁 notebooks/
│   ├── 01_data_exploration.ipynb       # Initial EDA and understanding
│   ├── 02_data_preprocessing.ipynb     # Data cleaning and preparation
│   ├── 03_rfm_analysis.ipynb          # RFM calculation and analysis
│   ├── 04_customer_segmentation.ipynb # Clustering implementation
│   ├── 05_recommendation_system.ipynb # Collaborative filtering
│   └── 06_model_evaluation.ipynb      # Performance metrics and validation
│
├── 📁 src/
│   ├── __init__.py
│   ├── data_preprocessing.py           # Data cleaning functions
│   ├── rfm_calculator.py              # RFM calculation utilities
│   ├── clustering.py                  # Customer segmentation logic
│   ├── recommendation.py              # Product recommendation system
│   └── utils.py                       # Helper functions and utilities
│
├── 📁 models/
│   ├── kmeans_model.pkl               # Saved clustering model
│   ├── scaler.pkl                     # Fitted StandardScaler
│   └── similarity_matrix.pkl          # Product similarity matrix
│
├── 📁 streamlit_app/
│   ├── app.py                         # Main Streamlit application
│   ├── pages/
│   │   ├── 🎯_product_recommendations.py
│   │   └── 👥_customer_segmentation.py
│   ├── components/
│   │   ├── sidebar.py                 # Sidebar components
│   │   └── styling.py                 # CSS and styling
│   └── config.py                      # App configuration
│
├── 📁 visualizations/
│   ├── eda_plots/                     # EDA visualization outputs
│   ├── clustering_plots/              # Cluster analysis plots
│   ├── rfm_distribution.png           # RFM distribution charts
│   └── recommendation_heatmap.png     # Similarity matrix heatmap
│
├── 📁 tests/
│   ├── test_preprocessing.py          # Unit tests for data processing
│   ├── test_clustering.py             # Tests for clustering functions
│   └── test_recommendation.py         # Tests for recommendation system
│
├── 📁 docs/
│   ├── project_report.md              # Detailed project documentation
│   ├── methodology.md                 # Technical approach explanation
│   └── user_guide.md                  # Streamlit app usage guide
│
├── 📄 requirements.txt                # Python dependencies
├── 📄 README.md                       # Project overview and setup
├── 📄 .gitignore                      # Git ignore file
└── 📄 config.yaml                     # Configuration parameters
```

```

Based on the document provided and an initial inspection of the online_retail.csv dataset, here are the data cleaning steps for each module:

For the Customer Segmentation Module
This module relies on RFM (Recency, Frequency, and Monetary) analysis, which requires the InvoiceDate, CustomerID, Quantity, and UnitPrice columns to calculate customer behavior metrics. The following data cleaning steps are essential:


Handling Missing Values: Remove all rows where CustomerID is missing. The dataset inspection showed that there are a significant number of transactions (over 135,000) that are not linked to a specific customer, so these should be removed to ensure accurate customer-level analysis.


Removing Canceled Invoices: Exclude all transactions where the InvoiceNo starts with the letter 'C'. These represent returns or cancellations and should not be included in the purchase history.


Filtering Invalid Quantities and Prices: Remove rows where Quantity or UnitPrice are less than or equal to zero. This ensures that only valid purchase data is used for calculating total spend and frequency.

Data Type Conversion: Convert the InvoiceDate column from its current object type to a datetime format. This is a critical step for accurately calculating the Recency metric, which is the time since a customer's last purchase.

For the Product Recommendation Module
This module is based on item-based collaborative filtering, which uses a CustomerID–StockCode matrix to compute product similarity. The following cleaning steps are necessary to ensure the integrity of the recommendation system:


Handling Missing Values: Similar to the segmentation module, remove any rows where the CustomerID is missing. A recommendation system relies on the purchase history of identified customers, so transactions without a customer ID are not useful.


Removing Canceled Invoices: Exclude transactions where InvoiceNo starts with 'C', as these are returns and do not represent a genuine purchase history.


Filtering Invalid Quantities and Prices: Remove rows with a Quantity or UnitPrice of zero or less. These transactions are not true purchases and would distort the product similarity calculations.


Handling Missing Product Descriptions: While the recommendation model uses StockCode as the primary product identifier, the Description is necessary for user display. The data inspection found a small number of rows with missing descriptions. These rows should be handled by either removing them or imputing a placeholder value like "Unknown Product."
```

```
Based on the project document, here are the detailed steps for data cleaning, exploratory data analysis (EDA), and feature engineering for customer segmentation.

Data Cleaning
This is the first step to prepare the data for analysis. You should perform the following actions in order:


Remove Duplicates: Although not explicitly listed in the preprocessing steps, the project tasks mention identifying duplicates. It's a best practice to remove any completely identical rows to ensure data accuracy.


Handle Missing Customer IDs: Remove all rows where the CustomerID is missing. The customer segmentation model is built on customer-level data, so transactions without an identifier are not useful for this task.


Exclude Canceled Invoices: Filter out any transactions where the InvoiceNo begins with the letter 'C'. These represent returns or cancellations and should not be considered as a purchase.


Remove Invalid Quantities and Prices: Filter out any rows where the Quantity or UnitPrice is a negative or zero value. These are typically errors and can skew your analysis.

Data Type Conversion: Convert the InvoiceDate column from its current object type to a datetime object. This is essential for calculating the Recency metric later.

Exploratory Data Analysis (EDA)
After cleaning the data, EDA is performed to gain insights before modeling. The project outlines specific EDA tasks for this module:


Transaction Volume: Analyze the number of transactions by country. This helps understand where the business has the most activity.


Purchase Trends: Visualize how purchases trend over time, which can reveal seasonality or growth patterns.


Monetary Distribution: Inspect the distribution of monetary values per transaction and for each customer. This helps you understand the spending habits of your customer base.


RFM Distributions: After creating the RFM features, visualize their distributions to understand the spread and characteristics of each metric.

Feature Engineering
The core of the customer segmentation module is creating the RFM features. The project provides a clear methodology for this:

Calculate Recency: This is a measure of how recently a customer made a purchase. To calculate it, subtract the customer's last purchase date from the latest transaction date in the entire dataset. The result is a number of days.


Calculate Frequency: This is the total number of transactions a customer has made. You can calculate this by counting the number of unique invoices for each 

CustomerID.


Calculate Monetary: This is the total amount of money a customer has spent. To get this, first create a 

TotalSpend column for each transaction by multiplying Quantity by UnitPrice, then sum these values for each CustomerID.


Standardize/Normalize RFM Values: Before applying a clustering algorithm like K-Means, you must standardize or normalize the Recency, Frequency, and Monetary values. This ensures that each feature contributes equally to the clustering process.
```

```
Based on the Shopper Spectrum_ Segmentation and Recommendations.docx project brief, your next steps after completing the EDA and RFM feature engineering are to build two main modules:

Clustering Methodology (Customer Segmentation):

Standardize your RFM values.

Choose a clustering algorithm like K-Means.

Use the Elbow Method or Silhouette Score to find the optimal number of clusters.

Run the clustering model and assign a cluster label (e.g., "High-Value," "At-Risk") to each customer based on their average RFM scores.

Visualize the clusters.

Save this trained clustering model for use in the Streamlit app.

Recommendation System Approach:

Create a customer-product matrix to represent user interactions.

Use item-based collaborative filtering to calculate the cosine similarity between products based on their purchase history.

This similarity matrix will be used to recommend the top 5 most similar products when a user inputs a product name.
```