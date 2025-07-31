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