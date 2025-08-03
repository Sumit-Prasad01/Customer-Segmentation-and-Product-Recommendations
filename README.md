# 🛍️ Shopper Spectrum: Segmentation & Recommendation App

A Streamlit-based interactive web application for:
- **Product Recommendations** using item-based collaborative filtering
- **Customer Segmentation** using RFM (Recency, Frequency, Monetary) analysis and KMeans clustering

---

## 🚀 Features

### 🔍 Product Recommendation
- Input a product name
- Get top 5 similar product recommendations
- Based on cosine similarity of purchase patterns

### 📊 Customer Segmentation
- Input RFM values manually
- Predict customer segment using a pre-trained KMeans model
- Segments: `High-Value`, `Regular`, `Occasional`, `At-Risk`

---

## 🧠 Models Used

| Model              | Description                                         |
|--------------------|-----------------------------------------------------|
| `kmeans_model.pkl` | Trained KMeans clustering model on RFM features     |
| `scaler_model.pkl` | StandardScaler fitted on log-transformed RFM data   |
| `item_similarity.pkl` | Cosine similarity matrix of item purchase vectors |

---

## 🧰 Tech Stack

- **Python**, **Streamlit**
- **Pandas**, **NumPy**, **scikit-learn**
- **Cosine Similarity**, **KMeans Clustering**
- **Joblib** for model serialization

---

## 🗂️ Project Structure
```
shopper-spectrum/
│
├── 📁 data/
│   ├── raw/
│   │   └── ecommerce_data.csv          # Original dataset
│   ├── processed/
│      ├── cleaned_data.csv            # After preprocessing
│      └── rfm_features.csv            # RFM calculated features
│   
│
├── 📁 notebooks/
│   ├── 01_data_exploration.ipynb       # Initial EDA and understanding
│   ├── 02_data_preprocessing.ipynb     # Data cleaning and preparation
│   ├── 03_rfm_analysis.ipynb          # RFM calculation and analysis
│   ├── 04_customer_segmentation.ipynb # Clustering implementation
│   └── 05_recommendation_system.ipynb # Collaborative filtering
│   
│
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
│
├── 📄 requirements.txt                # Python dependencies
├── 📄 app.py                          # Initial Sreamlit App
├── 📄 README.md                       # Project overview and setup
├── 📄 .gitignore                      # Git ignore file
└── 📄 Documentation.md                # Project Documentation
```

## Streamlit App Link - https://sumit-prasad01-customer-segmentation-and-product-rec-app-73szsl.streamlit.app/

