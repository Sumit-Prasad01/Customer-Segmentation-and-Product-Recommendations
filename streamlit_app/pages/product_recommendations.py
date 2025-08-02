import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
from components.styling import apply_custom_css

# Page configuration
st.set_page_config(
    page_title="🎯 Product Recommendations",
    page_icon="🎯",
    layout="wide"
)

apply_custom_css()

# Model loading functions - Replace these with your actual model loading
@st.cache_resource
def load_recommendation_model():
    """
    Load your trained recommendation model and related data
    Replace this with your actual model loading logic
    """
    try:
        # Example: Load your trained models
        # similarity_matrix = pickle.load(open('models/similarity_matrix.pkl', 'rb'))
        # product_data = pickle.load(open('models/product_data.pkl', 'rb'))
        # vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))
        
        # For now, return None - you'll replace this with actual model loading
        return None, None, None
    except Exception as e:
        st.error(f"Error loading recommendation model: {str(e)}")
        return None, None, None

def get_product_recommendations(product_name, model_data, n_recommendations=5):
    """
    Get product recommendations from your trained model
    Replace this function with your actual recommendation logic
    
    Args:
        product_name (str): Name of the product to get recommendations for
        model_data: Your loaded model data (similarity matrix, product data, etc.)
        n_recommendations (int): Number of recommendations to return
    
    Returns:
        list: List of recommended products with details
    """
    
    # PLACEHOLDER - Replace with your actual recommendation logic
    sample_recommendations = [
        {
            'product_name': 'WHITE METAL LANTERN',
            'similarity_score': 0.95,
            'description': 'Beautiful white metal lantern for home decoration',
            'category': 'Home Decor',
            'price': 3.39
        },
        {
            'product_name': 'GLASS STAR FROSTED T-LIGHT HOLDER',
            'similarity_score': 0.88,
            'description': 'Elegant glass star t-light holder',
            'category': 'Home Decor', 
            'price': 1.25
        },
        {
            'product_name': 'SILVER HEART DOOR KNOCKER',
            'similarity_score': 0.82,
            'description': 'Decorative silver heart door knocker',
            'category': 'Home Decor',
            'price': 2.55
        },
        {
            'product_name': 'NATURAL SLATE HEART CHALKBOARD',
            'similarity_score': 0.78,
            'description': 'Natural slate heart-shaped chalkboard',
            'category': 'Home Decor',
            'price': 1.85
        },
        {
            'product_name': 'HEART OF WICKER SMALL',
            'similarity_score': 0.75,
            'description': 'Small decorative wicker heart',
            'category': 'Home Decor',
            'price': 3.45
        }
    ]
    
    return sample_recommendations[:n_recommendations]

def search_products(query, model_data):
    """
    Search for products based on query
    Replace with your actual product search logic
    
    Args:
        query (str): Search query
        model_data: Your product data
    
    Returns:
        list: List of matching products
    """
    
    # PLACEHOLDER - Replace with your actual search logic
    sample_products = [
        'WHITE HANGING HEART T-LIGHT HOLDER',
        'WHITE METAL LANTERN', 
        'CREAM CUPID HEARTS COAT HANGER',
        'RED WOOLLY HOTTIE WHITE HEART',
        'GREEN WOOLLY HOTTIE WHITE HEART',
        'SET OF 3 CAKE TINS PANTRY DESIGN',
        'GLASS STAR FROSTED T-LIGHT HOLDER',
        'PARTY BUNTING',
        'LUNCH BAG RED RETROSPOT',
        'CHARLOTTE BAG PINK POLKADOT'
    ]
    
    if query:
        matching = [p for p in sample_products if query.lower() in p.lower()]
        return matching if matching else sample_products[:5]
    
    return sample_products[:10]

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎯 Product Recommendations</h1>
        <p>Get personalized product suggestions using collaborative filtering</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load models
    with st.spinner("Loading recommendation models..."):
        similarity_matrix, product_data, vectorizer = load_recommendation_model()
    
    model_data = {
        'similarity_matrix': similarity_matrix,
        'product_data': product_data,
        'vectorizer': vectorizer
    }
    
    # Sidebar for product selection
    with st.sidebar:
        st.markdown("### 🔍 Product Search")
        st.markdown("---")
        
        # Search input
        search_query = st.text_input(
            "Search for products:",
            placeholder="e.g., heart, bag, kitchen, lantern...",
            key="product_search"
        )
        
        # Get matching products
        matching_products = search_products(search_query, model_data)
        
        # Product selection
        if matching_products:
            selected_product = st.selectbox(
                "Select a product:",
                options=matching_products,
                key="product_select"
            )
        else:
            st.warning("No products found. Try a different search term.")
            selected_product = None
        
        st.markdown("---")
        
        # Advanced options
        st.markdown("### ⚙️ Options")
        n_recommendations = st.slider(
            "Number of recommendations:",
            min_value=3,
            max_value=10,
            value=5,
            key="n_recs"
        )
        
        show_similarity_scores = st.checkbox(
            "Show similarity scores",
            value=True,
            key="show_scores"
        )
    
    # Main content area
    if selected_product:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Display selected product
            st.markdown("### 🎯 Selected Product")
            st.markdown(f"""
            <div class="product-card selected">
                <h4>{selected_product}</h4>
                <p>Click "Get Recommendations" to find similar products!</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Get recommendations button
            if st.button("🚀 Get Recommendations", type="primary", key="get_recs"):
                with st.spinner("Analyzing product similarities..."):
                    recommendations = get_product_recommendations(
                        selected_product, model_data, n_recommendations
                    )
                    
                    if recommendations:
                        st.markdown("### 🎯 Recommended Products")
                        
                        # Display recommendations
                        for i, rec in enumerate(recommendations, 1):
                            similarity_info = f"Similarity: {rec['similarity_score']:.2%}" if show_similarity_scores else ""
                            
                            st.markdown(f"""
                            <div class="recommendation-card">
                                <div class="rec-header">
                                    <h4>#{i} {rec['product_name']}</h4>
                                    <span class="similarity-badge">{similarity_info}</span>
                                </div>
                                <p><strong>Category:</strong> {rec['category']}</p>
                                <p><strong>Price:</strong> £{rec['price']:.2f}</p>
                                <p>{rec['description']}</p>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Success message
                        st.success(f"✅ Found {len(recommendations)} similar products!")
                    else:
                        st.error("❌ Could not generate recommendations. Please try a different product.")
        
        with col2:
            # Tips and information
            st.markdown("### 💡 How it Works")
            st.info("""
            **Collaborative Filtering Process:**
            
            1. **Product Analysis**: The system analyzes product descriptions and customer purchase patterns
            
            2. **Similarity Calculation**: Uses cosine similarity to find products with similar characteristics
            
            3. **Recommendation Generation**: Returns the most similar products based on the trained model
            
            4. **Personalization**: Recommendations are based on actual customer behavior data
            """)
            
            st.markdown("### 📊 Model Information")
            st.markdown("""
            <div class="info-card">
                <p><strong>Algorithm:</strong> Item-based Collaborative Filtering</p>
                <p><strong>Similarity Metric:</strong> Cosine Similarity</p>
                <p><strong>Features:</strong> Product descriptions, categories, purchase patterns</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Performance metrics (placeholder)
            st.markdown("### 📈 Model Performance")
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Accuracy", "87.5%", "2.1%")
            with col_b:
                st.metric("Coverage", "94.2%", "1.8%")
    
    else:
        # No product selected
        st.markdown("""
        <div class="welcome-card">
            <h3>🔍 Search for Products</h3>
            <p>Use the sidebar to search and select a product to get personalized recommendations.</p>
            <ul>
                <li>Try searching for: "heart", "bag", "kitchen", "decor"</li>
                <li>Select a product from the dropdown</li>
                <li>Click "Get Recommendations" to see similar products</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Instructions for model integration
    with st.expander("🔧 Model Integration Instructions"):
        st.markdown("""
        **To integrate your trained models:**
        
        1. **Replace the `load_recommendation_model()` function:**
        ```python
        @st.cache_resource
        def load_recommendation_model():
            similarity_matrix = pickle.load(open('models/similarity_matrix.pkl', 'rb'))
            product_data = pd.read_pickle('models/product_data.pkl')
            vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))
            return similarity_matrix, product_data, vectorizer
        ```
        
        2. **Update the `get_product_recommendations()` function with your logic:**
        ```python
        def get_product_recommendations(product_name, model_data, n_recommendations=5):
            # Your recommendation logic here
            # Use model_data['similarity_matrix'], model_data['product_data'], etc.
            return recommendations
        ```
        
        3. **Modify the `search_products()` function:**
        ```python
        def search_products(query, model_data):
            # Your product search logic here
            return matching_products
        ```
        """)

if __name__ == "__main__":
    main()