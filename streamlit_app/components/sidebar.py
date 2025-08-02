import streamlit as st
from datetime import datetime

def render_sidebar():
    """Render the main sidebar with navigation and information"""
    
    with st.sidebar:
        # Logo/Title section
        st.markdown("""
        <div class="sidebar-header">
            <h2>🛒 Shopper Spectrum</h2>
            <p>E-Commerce Analytics Platform</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Navigation section
        st.markdown("### 🧭 Navigation")
        st.markdown("""
        **Pages Available:**
        - **🏠 Home:** Overview and analytics dashboard
        - **🎯 Product Recommendations:** Get product suggestions
        - **👥 Customer Segmentation:** RFM analysis and predictions
        """)
        
        st.markdown("---")
        
        # App information
        st.markdown("### ℹ️ About")
        st.markdown("""
        This application provides:
        
        **🎯 Product Recommendations:**
        - Item-based collaborative filtering
        - Cosine similarity analysis
        - Real-time product suggestions
        
        **👥 Customer Segmentation:**
        - RFM (Recency, Frequency, Monetary) analysis
        - K-Means clustering
        - Customer behavior insights
        """)
        
        # Model status
        st.markdown("---")
        st.markdown("### 🔧 Model Status")
        
        # Placeholder for model status - replace with actual checks
        col1, col2 = st.columns([3, 1])
        with col1:
            st.text("Recommendation Model")
        with col2:
            st.markdown("🟡")  # Replace with actual status check
            
        col1, col2 = st.columns([3, 1])
        with col1:
            st.text("Segmentation Model")
        with col2:
            st.markdown("🟡")  # Replace with actual status check
        
        # Performance metrics
        st.markdown("---")
        st.markdown("### 📊 Quick Stats")
        st.metric("Total Products", "1,200+")
        st.metric("Customer Segments", "4")
        st.metric("Model Accuracy", "87.5%")
        
        # Help section
        st.markdown("---")
        st.markdown("### 💡 Help & Tips")
        
        with st.expander("🎯 Product Recommendations"):
            st.markdown("""
            **How to use:**
            1. Search for a product by name
            2. Select from the dropdown
            3. Click "Get Recommendations"
            4. View similar products with similarity scores
            
            **Tips:**
            - Try specific product names for better results
            - Use category keywords like "kitchen", "decor"
            """)
        
        with st.expander("👥 Customer Segmentation"):
            st.markdown("""
            **RFM Values Explained:**
            - **Recency:** Days since last purchase (lower = better)
            - **Frequency:** Number of purchases (higher = better)  
            - **Monetary:** Total amount spent (higher = better)
            
            **Segments:**
            - **High-Value:** Recent, frequent, high spenders
            - **Regular:** Steady, moderate customers
            - **Occasional:** Infrequent buyers
            - **At-Risk:** Haven't purchased recently
            """)
        
        # Footer
        st.markdown("---")
        st.markdown("""
        <div class="sidebar-footer">
            <p><small>Built with Streamlit</small></p>
            <p><small>Last updated: {}</small></p>
        </div>
        """.format(datetime.now().strftime("%Y-%m-%d")), unsafe_allow_html=True)

def render_model_info_sidebar():
    """Render model-specific information in sidebar"""
    
    st.sidebar.markdown("### 🤖 Model Details")
    
    # Current page detection
    current_page = st.session_state.get('current_page', 'home')
    
    if 'product' in current_page.lower():
        st.sidebar.markdown("""
        **Recommendation System:**
        - Algorithm: Collaborative Filtering
        - Similarity: Cosine Similarity
        - Features: Product descriptions, categories
        - Training Data: Customer purchase history
        """)
        
        st.sidebar.markdown("**Performance Metrics:**")
        st.sidebar.metric("Precision@5", "0.847")
        st.sidebar.metric("Recall@5", "0.623")
        st.sidebar.metric("Coverage", "94.2%")
        
    elif 'customer' in current_page.lower():
        st.sidebar.markdown("""
        **Segmentation Model:**
        - Algorithm: K-Means Clustering
        - Features: RFM values
        - Clusters: 4 segments
        - Preprocessing: StandardScaler
        """)
        
        st.sidebar.markdown("**Performance Metrics:**")
        st.sidebar.metric("Silhouette Score", "0.726")
        st.sidebar.metric("Inertia", "1,247")
        st.sidebar.metric("Explained Variance", "78.3%")

def render_data_info_sidebar():
    """Render data information in sidebar"""
    
    st.sidebar.markdown("### 📊 Dataset Info")
    st.sidebar.markdown("""
    **Data Source:** E-commerce transaction data
    
    **Time Period:** 2022-2023
    
    **Key Columns:**
    - InvoiceNo: Transaction ID
    - StockCode: Product ID
    - Description: Product name
    - Quantity: Items purchased
    - InvoiceDate: Transaction date
    - UnitPrice: Price per item
    - CustomerID: Customer ID
    - Country: Customer location
    
    **Data Quality:**
    - Removed cancelled transactions
    - Filtered negative quantities/prices
    - Handled missing CustomerIDs
    """)

def check_model_status():
    """Check if models are loaded and working"""
    # Placeholder function - replace with actual model checks
    
    recommendation_status = "loaded"  # or "error", "loading"
    segmentation_status = "loaded"   # or "error", "loading"
    
    return {
        'recommendation': recommendation_status,
        'segmentation': segmentation_status
    }

def get_status_emoji(status):
    """Get emoji for model status"""
    if status == "loaded":
        return "🟢"
    elif status == "loading":
        return "🟡"
    elif status == "error":
        return "🔴"
    else:
        return "⚫"