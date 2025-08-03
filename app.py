import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity

# Load models and data
scaler = joblib.load("models/scaler.pkl")
kmeans_model = joblib.load("models/kmeans_model.pkl")
similarity_matrix = joblib.load("models/item_similarity_model.pkl")

st.set_page_config(page_title="Shopper Spectrum", layout="wide")
st.title("🛍️ Shopper Spectrum: Segmentation & Recommendation App")

# Tabs for modular UI
recommendation_tab, segmentation_tab = st.tabs(["🔍 Product Recommendation", "📊 Customer Segmentation"])

# 1️⃣ Product Recommendation Module
with recommendation_tab:
    st.header("🔍 Product Recommendation")
    product_name = st.text_input("Enter a product name:")

    if st.button("Get Recommendations"):
        if product_name in similarity_matrix.columns:
            recommendations = similarity_matrix.loc[product_name].sort_values(ascending=False).iloc[1:6].index.tolist()
            st.success("Top 5 Similar Products:")
            for i, rec in enumerate(recommendations, 1):
                st.write(f"{i}. {rec}")
        else:
            st.error("Product not found. Please check the name or try another.")

# 2️⃣ Customer Segmentation Module
with segmentation_tab:
    st.header("📊 Customer Segmentation")
    recency = st.number_input("Recency (days)", min_value=0)
    frequency = st.number_input("Frequency (number of purchases)", min_value=0)
    monetary = st.number_input("Monetary (total spend)", min_value=0.0)

    if st.button("Predict Cluster"):
        input_rfm = pd.DataFrame([[recency, frequency, monetary]], columns=["Recency", "Frequency", "Monetary"])
        input_log = np.log1p(input_rfm)
        input_scaled = scaler.transform(input_log)
        cluster_label = kmeans_model.predict(input_scaled)[0]

        segment_map = {
            0: "High-Value",
            1: "Regular",
            2: "Occasional",
            3: "At-Risk"
        }

        segment = segment_map.get(cluster_label, f"Cluster {cluster_label}")
        st.success(f"Predicted Segment: {segment}")

