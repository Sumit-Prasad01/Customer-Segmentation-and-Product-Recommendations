"""
Configuration file for the Shopper Spectrum Streamlit application
"""

import os
from pathlib import Path

# App Configuration
APP_CONFIG = {
    "app_name": "Shopper Spectrum",
    "app_description": "Customer Segmentation and Product Recommendations in E-Commerce",
    "version": "1.0.0",
    "author": "Data Science Team",
    "contact_email": "support@shopperspectrum.com",
    "last_updated": "2024-01-15"
}

# Page Configuration
PAGE_CONFIG = {
    "layout": "wide",
    "initial_sidebar_state": "expanded",
    "menu_items": {
        'Get Help': 'https://docs.shopperspectrum.com',
        'Report a bug': "https://github.com/shopperspectrum/issues",
        'About': "# Shopper Spectrum\nCustomer Segmentation and Product Recommendations"
    }
}

# Model Paths Configuration
# Update these paths to point to your actual model files
MODEL_PATHS = {
    "recommendation": {
        "similarity_matrix": "models/recommendation/similarity_matrix.pkl",
        "product_data": "models/recommendation/product_data.pkl", 
        "vectorizer": "models/recommendation/tfidf_vectorizer.pkl",
        "product_encoder": "models/recommendation/product_encoder.pkl"
    },
    "segmentation": {
        "clustering_model": "models/segmentation/kmeans_model.pkl",
        "scaler": "models/segmentation/rfm_scaler.pkl",
        "cluster_labels": "models/segmentation/cluster_labels.pkl",
        "label_encoder": "models/segmentation/label_encoder.pkl"
    }
}

# Data Paths Configuration
DATA_PATHS = {
    "raw_data": "data/raw/online_retail.csv",
    "processed_data": "data/processed/",
    "product_catalog": "data/processed/product_catalog.csv",
    "customer_data": "data/processed/customer_rfm.csv"
}

# Model Parameters
MODEL_PARAMS = {
    "recommendation": {
        "n_recommendations": 5,
        "min_similarity_threshold": 0.1,
        "max_features_tfidf": 1000,
        "similarity_metric": "cosine"
    },
    "segmentation": {
        "n_clusters": 4,
        "random_state": 42,
        "max_iter": 300,
        "init": "k-means++",
        "segment_labels": {
            0: "High-Value",
            1: "Regular", 
            2: "Occasional",
            3: "At-Risk"
        }
    }
}

# UI Configuration
UI_CONFIG = {
    "color_palette": {
        "primary": "#667eea",
        "secondary": "#764ba2", 
        "success": "#28a745",
        "warning": "#ffc107",
        "error": "#dc3545",
        "info": "#17a2b8",
        "segments": {
            "High-Value": "#FF6B6B",
            "Regular": "#4ECDC4", 
            "Occasional": "#45B7D1",
            "At-Risk": "#96CEB4"
        }
    },
    "chart_config": {
        "height": 400,
        "theme": "plotly_white",
        "font_family": "Poppins"
    }
}

# Business Rules Configuration
BUSINESS_RULES = {
    "rfm_ranges": {
        "recency": {
            "min": 0,
            "max": 365,
            "excellent": 30,
            "good": 60,
            "average": 120,
            "poor": 365
        },
        "frequency": {
            "min": 1,
            "max": 100,
            "excellent": 15,
            "good": 8,
            "average": 4,
            "poor": 1
        },
        "monetary": {
            "min": 0,
            "max": 10000,
            "excellent": 1000,
            "good": 500,
            "average": 200,
            "poor": 50
        }
    },
    "segment_thresholds": {
        "High-Value": {
            "recency_max": 30,
            "frequency_min": 10,
            "monetary_min": 500
        },
        "Regular": {
            "recency_max": 60,
            "frequency_min": 5,
            "monetary_min": 200
        },
        "Occasional": {
            "recency_max": 180,
            "frequency_min": 2,
            "monetary_min": 50
        }
    }
}

# Analytics Configuration
ANALYTICS_CONFIG = {
    "default_metrics": [
        "total_customers",
        "total_products", 
        "total_revenue",
        "avg_order_value",
        "customer_retention_rate",
        "recommendation_accuracy"
    ],
    "dashboard_charts": [
        "segment_distribution",
        "revenue_trend",
        "product_performance",
        "customer_journey"
    ]
}

# Error Messages
ERROR_MESSAGES = {
    "model_loading": "Failed to load machine learning models. Please check model files.",
    "data_loading": "Failed to load data. Please check data files.",
    "prediction_error": "Error occurred during prediction. Please try again.",
    "invalid_input": "Invalid input provided. Please check your values.",
    "no_recommendations": "No recommendations found for the selected product.",
    "product_not_found": "Product not found in the database.",
    "connection_error": "Connection error. Please check your internet connection."
}

# Success Messages  
SUCCESS_MESSAGES = {
    "model_loaded": "Models loaded successfully!",
    "prediction_complete": "Prediction completed successfully!",
    "recommendations_found": "Recommendations generated successfully!",
    "data_processed": "Data processed successfully!"
}

# Cache Configuration
CACHE_CONFIG = {
    "ttl": 3600,  # 1 hour in seconds
    "max_entries": 1000,
    "allow_output_mutation": True
}

# Logging Configuration
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "log_file": "logs/app.log",
    "max_log_size": 10485760,  # 10MB
    "backup_count": 5
}

# Performance Monitoring
PERFORMANCE_CONFIG = {
    "enable_profiling": False,                
    "track_user_interactions": True,          
    "monitor_model_performance": True,        
    "log_to_file": True,                      
    "display_runtime_metrics": True,          
    "max_log_entries": 1000                   
}