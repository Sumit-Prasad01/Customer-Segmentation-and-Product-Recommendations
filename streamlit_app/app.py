import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from components.styling import apply_custom_css
from config import APP_CONFIG

# Page configuration
st.set_page_config(
    page_title="🛒 Shopper Spectrum",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styling
apply_custom_css()

def main():
    """Main application entry point"""
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🛒 Shopper Spectrum</h1>
        <p>Customer Segmentation and Product Recommendations in E-Commerce</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Welcome section
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="welcome-card">
            <h3>🎯 Welcome to Shopper Spectrum!</h3>
            <p>This application provides powerful tools for e-commerce analytics:</p>
            <ul>
                <li><strong>🎯 Product Recommendations:</strong> Get personalized product suggestions using collaborative filtering</li>
                <li><strong>👥 Customer Segmentation:</strong> Analyze customer behavior using RFM analysis</li>
            </ul>
            <p>Navigate using the sidebar to explore different features!</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Key Features Section
    st.markdown("## 🚀 Key Features")
    
    feature_col1, feature_col2 = st.columns(2)
    
    with feature_col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🎯 Product Recommendations</h4>
            <p>Advanced collaborative filtering system that:</p>
            <ul>
                <li>Analyzes customer purchase patterns</li>
                <li>Computes product similarities using cosine similarity</li>
                <li>Provides top 5 product recommendations</li>
                <li>Helps increase cross-selling opportunities</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with feature_col2:
        st.markdown("""
        <div class="feature-card">
            <h4>👥 Customer Segmentation</h4>
            <p>RFM-based customer analysis that:</p>
            <ul>
                <li>Segments customers using Recency, Frequency, Monetary values</li>
                <li>Identifies High-Value, Regular, Occasional, and At-Risk customers</li>
                <li>Enables targeted marketing campaigns</li>
                <li>Supports customer retention strategies</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Business Impact Section
    st.markdown("## 📈 Business Impact")
    
    impact_metrics = st.columns(4)
    
    with impact_metrics[0]:
        st.metric(
            label="Customer Retention",
            value="25%",
            delta="12% increase"
        )
    
    with impact_metrics[1]:
        st.metric(
            label="Cross-sell Revenue",
            value="$2.3M",
            delta="18% increase"
        )
    
    with impact_metrics[2]:
        st.metric(
            label="Conversion Rate",
            value="8.7%",
            delta="3.2% increase"
        )
    
    with impact_metrics[3]:
        st.metric(
            label="Customer Satisfaction",
            value="4.6/5",
            delta="0.4 increase"
        )
    
    # Sample Analytics Dashboard
    st.markdown("## 📊 Sample Analytics Overview")
    
    # Generate sample data for demonstration
    np.random.seed(42)
    
    # Sample customer distribution
    segments = ['High-Value', 'Regular', 'Occasional', 'At-Risk']
    segment_sizes = [150, 300, 250, 100]
    
    # Sample monthly trends
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    revenue_trend = [2.1, 2.3, 2.8, 2.6, 3.1, 3.4]
    
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        # Customer Segmentation Pie Chart
        fig_pie = px.pie(
            values=segment_sizes,
            names=segments,
            title="Customer Segmentation Distribution",
            color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
        )
        fig_pie.update_layout(height=400)
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with chart_col2:
        # Revenue Trend
        fig_line = px.line(
            x=months,
            y=revenue_trend,
            title="Monthly Revenue Trend (in millions)",
            markers=True
        )
        fig_line.update_traces(line_color='#FF6B6B', line_width=3)
        fig_line.update_layout(height=400)
        st.plotly_chart(fig_line, use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div class="footer">
        <p>💡 <strong>Pro Tip:</strong> Use the sidebar navigation to explore Product Recommendations and Customer Segmentation features!</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()