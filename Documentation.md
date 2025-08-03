# 📄 Shopper Spectrum – Project Documentation

## 🧾 Introduction

The "Shopper Spectrum" project is a full-cycle data science and machine learning application designed to understand customer behavior and provide actionable business intelligence through segmentation and product recommendations. Built using Python and Streamlit, the project encapsulates key components of unsupervised learning, collaborative filtering, and interactive UI design. With over 540,000 retail transaction records, the application helps identify behavioral segments of customers and recommends products based on past purchases using similarity metrics.

---

## 📊 Data Preprocessing and Feature Engineering

The initial step of the project involved ingesting a large transactional dataset containing invoices, customer IDs, purchase dates, product descriptions, quantities, and prices. We began by cleaning the data:

* Removed cancelled orders (InvoiceNo starting with 'C')
* Dropped records with null CustomerIDs or product descriptions
* Filtered out zero or negative quantity and price entries

A new feature `TotalPrice` was created by multiplying Quantity and UnitPrice to represent the revenue generated per transaction. This cleaned dataset formed the foundation for both the recommendation system and the customer segmentation analysis.

---

## 📈 RFM Feature Construction

To segment customers, we used the RFM (Recency, Frequency, Monetary) model:

* **Recency:** Days since the customer's last purchase
* **Frequency:** Number of unique invoices per customer
* **Monetary:** Total revenue from the customer

The most recent purchase date in the dataset was used as a reference to compute the Recency for each customer. Log transformation was applied to RFM features to normalize the skewed distributions. A StandardScaler was then used to scale these features for clustering.

---

## 🧠 Clustering for Customer Segmentation

After scaling, we applied KMeans clustering to segment customers. We experimented with different cluster numbers and evaluated model performance using:

* **Silhouette Score**
* **Calinski-Harabasz Index**
* **Davies-Bouldin Index**

We determined that `k=4` offered a good trade-off between performance and interpretability. The clusters were then interpreted and mapped to meaningful segments:

* **Cluster 0:** High-Value
* **Cluster 1:** Regular
* **Cluster 2:** Occasional
* **Cluster 3:** At-Risk

PCA (Principal Component Analysis) was applied to project customer segments into two dimensions, enabling intuitive visualization.

---

## 🤖 Product Recommendation System

For recommendations, we implemented an item-based collaborative filtering model:

* Created a customer-product matrix
* Populated it with purchase quantities
* Computed cosine similarity between items

The result was a similarity matrix (`item_similarity.pkl`) representing how closely products are bought together. This model helps suggest similar items to users based on their search input.

Additional enhancements included:

* Filtering out rarely purchased items (e.g., purchased < 10 times)
* Applying TF-IDF-like weighting to normalize frequency bias

---

## 🎯 Model Evaluation

To evaluate the recommendation model, we used **Hit Rate @ 5**:

* Randomly split transactions into train/test sets
* For each product bought in test, check if it appears in top 5 recommendations from training set

The final model achieved a **Hit Rate of 0.1976 (≈19.76%)**, which is considered a strong baseline for unsupervised, item-based filtering in e-commerce scenarios.

---

## 🖥️ Streamlit App Design

The final product was deployed as a Streamlit web application with two main modules:

### 1. Product Recommendation

* Users input a product name
* App retrieves top 5 most similar products using the similarity matrix

### 2. Customer Segmentation

* Users enter RFM values manually
* The app log-transforms, scales the input, and uses a pre-trained KMeans model to predict the segment
* Outputs the customer's behavioral label (e.g., High-Value)

The user interface includes clean tabs, interactive inputs, and color-coded visual outputs for clarity.

---

## 🗂️ Supporting Artifacts

* `scaler_model.pkl`: StandardScaler trained on RFM log-transformed data
* `kmeans_model.pkl`: Trained KMeans model for clustering
* `item_similarity.pkl`: Cosine similarity matrix of products

These files are preloaded into the app and used for real-time prediction and recommendations.

---

## 🔧 Tools and Technologies

* **Languages:** Python
* **Libraries:** Pandas, NumPy, scikit-learn, Matplotlib, Plotly, Joblib
* **Frameworks:** Streamlit
* **ML Techniques:** KMeans clustering, collaborative filtering, TF-IDF weighting, PCA

---

## ✅ Outcomes and Use Cases

The Shopper Spectrum solution is designed not just as a technical demonstration, but as a powerful tool that can deliver tangible value to businesses across various retail sectors.

* Enables retailers to identify loyal, at-risk, or high-value customers
* Helps improve retention and engagement via personalized marketing
* Suggests relevant product bundles and alternatives to users
* Facilitates data-driven customer relationship strategies
* Helps marketing and sales teams prioritize resources by focusing on high-value segments
* Enables businesses to improve upselling and cross-selling through targeted product suggestions
* Provides insights into customer lifetime value (CLV) and churn risk for strategic planning

---

## 📈 Future Enhancements

* Integrate user authentication to track customer profiles
* Add real-time product search and autocomplete
* Allow upload of new transaction datasets for fresh insights
* Enable admin dashboard to monitor segment trends over time
* Expand to include session-based and time-aware recommendations

---

## 🧾 Conclusion

Shopper Spectrum demonstrates how classic unsupervised learning techniques like RFM and clustering can be fused with recommendation systems to deliver intelligent, business-friendly insights. From data preprocessing to deployment, the project encapsulates a well-rounded ML pipeline with high practical value and extensibility.

It provides a scalable foundation for enhancing customer engagement and boosting e-commerce sales through smart segmentation and recommendations.

