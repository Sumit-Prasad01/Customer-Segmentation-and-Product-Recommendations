import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from components.styling import apply_custom_css

# Page configuration
st.set_page_config(
    page_title="👥 Customer Segmentation",
    page_icon="👥",
    layout="wide"
)

apply_custom_css()

# Model loading functions - Replace these with your actual model loading
@st.cache_resource
def load_segmentation_model():
    """
    Load your trained customer segmentation model
    Replace this with your actual model loading logic
    """
    try:
        # Example: Load your trained models
        # clustering_model = pickle.load(open('models/kmeans_model.pkl', 'rb'))
        # scaler = pickle.load(open('models/rfm_scaler.pkl', 'rb'))
        # cluster_labels = pickle.load(open('models/cluster_labels.pkl', 'rb'))
        
        # For now, return None - you'll replace this with actual model loading
        return None, None, None
    except Exception as e:
        st.error(f"Error loading segmentation model: {str(e)}")
        return None, None, None

def predict_customer_segment(recency, frequency, monetary, model_data):
    """
    Predict customer segment using your trained model
    Replace this function with your actual prediction logic
    
    Args:
        recency (int): Days since last purchase
        frequency (int): Number of purchases
        monetary (float): Total amount spent
        model_data: Your loaded model data
    
    Returns:
        dict: Prediction results with segment label and probabilities
    """
    
    # PLACEHOLDER - Replace with your actual prediction logic
    # Example logic for demonstration
    if recency <= 30 and frequency >= 10 and monetary >= 500:
        segment = "High-Value"
        confidence = 0.95
        description = "Frequent, recent, and high-spending customers. Your most valuable segment!"
        color = "#FF6B6B"
        recommendations = [
            "Offer premium products and exclusive deals",
            "Provide VIP customer service",
            "Send personalized product recommendations",
            "Create loyalty rewards program"
        ]
    elif recency <= 60 and frequency >= 5 and monetary >= 200:
        segment = "Regular"
        confidence = 0.88
        description = "Steady customers with moderate purchase behavior."
        color = "#4ECDC4"
        recommendations = [
            "Send regular promotional offers",
            "Encourage increased purchase frequency",
            "Cross-sell complementary products",
            "Maintain engagement through newsletters"
        ]
    elif recency <= 180 and frequency >= 2 and monetary >= 50:
        segment = "Occasional"
        confidence = 0.82
        description = "Infrequent buyers who make occasional purchases."
        color = "#45B7D1"
        recommendations = [
            "Send targeted reactivation campaigns",
            "Offer seasonal promotions",
            "Provide product education content",
            "Use reminder marketing strategies"
        ]
    else:
        segment = "At-Risk"
        confidence = 0.79
        description = "Customers who haven't purchased recently and may churn."
        color = "#96CEB4"
        recommendations = [
            "Launch win-back campaigns",
            "Offer significant discounts",
            "Survey for feedback and issues",
            "Provide customer support outreach"
        ]
    
    return {
        'segment': segment,
        'confidence': confidence,
        'description': description,
        'color': color,
        'recommendations': recommendations,
        'rfm_scores': {
            'recency': recency,
            'frequency': frequency,
            'monetary': monetary
        }
    }

def get_segment_insights():
    """
    Get insights about different customer segments
    Replace with your actual segment analysis
    """
    return {
        'High-Value': {
            'percentage': 15,
            'avg_monetary': 750,
            'avg_frequency': 12,
            'avg_recency': 20,
            'color': '#FF6B6B'
        },
        'Regular': {
            'percentage': 35,
            'avg_monetary': 300,
            'avg_frequency': 7,
            'avg_recency': 45,
            'color': '#4ECDC4'
        },
        'Occasional': {
            'percentage': 30,
            'avg_monetary': 120,
            'avg_frequency': 3,
            'avg_recency': 90,
            'color': '#45B7D1'
        },
        'At-Risk': {
            'percentage': 20,
            'avg_monetary': 80,
            'avg_frequency': 2,
            'avg_recency': 200,
            'color': '#96CEB4'
        }
    }

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>👥 Customer Segmentation</h1>
        <p>Analyze customer behavior using RFM (Recency, Frequency, Monetary) analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load models
    with st.spinner("Loading segmentation models..."):
        clustering_model, scaler, cluster_labels = load_segmentation_model()
    
    model_data = {
        'clustering_model': clustering_model,
        'scaler': scaler,
        'cluster_labels': cluster_labels
    }
    
    # Two-column layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📊 Customer Analysis Input")
        
        # RFM Input Form
        with st.form("rfm_form"):
            st.markdown("#### Enter Customer RFM Values:")
            
            # Recency input
            recency = st.number_input(
                "🕒 Recency (Days since last purchase)",
                min_value=0,
                max_value=365,
                value=30,
                help="Number of days since the customer's last purchase"
            )
            
            # Frequency input
            frequency = st.number_input(
                "🔄 Frequency (Number of purchases)",
                min_value=1,
                max_value=100,
                value=5,
                help="Total number of purchases made by the customer"
            )
            
            # Monetary input
            monetary = st.number_input(
                "💰 Monetary (Total amount spent)",
                min_value=0.0,
                value=250.0,
                step=10.0,
                format="%.2f",
                help="Total amount spent by the customer"
            )
            
            # Submit button
            submitted = st.form_submit_button("🎯 Predict Customer Segment", type="primary")
        
        # Quick preset buttons
        st.markdown("#### 🚀 Quick Presets:")
        preset_col1, preset_col2 = st.columns(2)
        
        with preset_col1:
            if st.button("High-Value Customer", key="high_value"):
                st.session_state.recency_preset = 15
                st.session_state.frequency_preset = 15
                st.session_state.monetary_preset = 800
                
            if st.button("Regular Customer", key="regular"):
                st.session_state.recency_preset = 45
                st.session_state.frequency_preset = 8
                st.session_state.monetary_preset = 350
        
        with preset_col2:
            if st.button("Occasional Customer", key="occasional"):
                st.session_state.recency_preset = 120
                st.session_state.frequency_preset = 3
                st.session_state.monetary_preset = 150
                
            if st.button("At-Risk Customer", key="at_risk"):
                st.session_state.recency_preset = 250
                st.session_state.frequency_preset = 2
                st.session_state.monetary_preset = 80
    
    with col2:
        # Results display
        if submitted:
            with st.spinner("Analyzing customer segment..."):
                prediction = predict_customer_segment(recency, frequency, monetary, model_data)
                
                # Display prediction result
                st.markdown("### 🎯 Prediction Result")
                
                st.markdown(f"""
                <div class="segment-result" style="border-left: 5px solid {prediction['color']};">
                    <h3 style="color: {prediction['color']};">{prediction['segment']} Customer</h3>
                    <p><strong>Confidence:</strong> {prediction['confidence']:.1%}</p>
                    <p>{prediction['description']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # RFM Visualization
                st.markdown("#### 📊 RFM Profile")
                
                # Create radar chart
                categories = ['Recency Score', 'Frequency Score', 'Monetary Score']
                
                # Normalize scores for visualization (this is a placeholder - use your actual scoring logic)
                recency_score = max(0, 100 - (recency / 365 * 100))
                frequency_score = min(100, frequency * 10)
                monetary_score = min(100, monetary / 10)
                
                fig = go.Figure()
                
                fig.add_trace(go.Scatterpolar(
                    r=[recency_score, frequency_score, monetary_score],
                    theta=categories,
                    fill='toself',
                    name='Customer Profile',
                    line_color=prediction['color']
                ))
                
                fig.update_layout(
                    polar=dict(
                        radialaxis=dict(
                            visible=True,
                            range=[0, 100]
                        )),
                    showlegend=False,
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Recommendations
                st.markdown("#### 💡 Marketing Recommendations")
                for i, rec in enumerate(prediction['recommendations'], 1):
                    st.markdown(f"{i}. {rec}")
        
        else:
            # Default display
            st.markdown("### 🎯 Customer Segment Prediction")
            st.info("Enter customer RFM values and click 'Predict Customer Segment' to analyze the customer profile.")
            
            # Display segment insights
            st.markdown("### 📈 Segment Overview")
            insights = get_segment_insights()
            
            for segment, data in insights.items():
                st.markdown(f"""
                <div class="segment-card" style="border-left: 4px solid {data['color']};">
                    <h4 style="color: {data['color']};">{segment}</h4>
                    <p><strong>{data['percentage']}%</strong> of customers</p>
                    <p>Avg Spend: £{data['avg_monetary']} | Avg Frequency: {data['avg_frequency']} | Avg Recency: {data['avg_recency']} days</p>
                </div>
                """, unsafe_allow_html=True)
    
    # Bottom section - Analytics Dashboard
    st.markdown("---")
    st.markdown("## 📊 Segmentation Analytics Dashboard")
    
    # Segment distribution chart
    insights = get_segment_insights()
    segments = list(insights.keys())
    percentages = [insights[seg]['percentage'] for seg in segments]
    colors = [insights[seg]['color'] for seg in segments]
    
    col_chart1, col_chart2, col_chart3 = st.columns(3)
    
    with col_chart1:
        # Pie chart
        fig_pie = px.pie(
            values=percentages,
            names=segments,
            title="Customer Distribution by Segment",
            color_discrete_sequence=colors
        )
        fig_pie.update_layout(height=350)
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col_chart2:
        # Average monetary value by segment
        monetary_values = [insights[seg]['avg_monetary'] for seg in segments]
        fig_bar = px.bar(
            x=segments,
            y=monetary_values,
            title="Average Monetary Value by Segment",
            color=segments,
            color_discrete_sequence=colors
        )
        fig_bar.update_layout(height=350, showlegend=False)
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col_chart3:
        # Frequency vs Recency scatter
        frequency_values = [insights[seg]['avg_frequency'] for seg in segments]
        recency_values = [insights[seg]['avg_recency'] for seg in segments]
        
        fig_scatter = px.scatter(
            x=recency_values,
            y=frequency_values,
            color=segments,
            size=monetary_values,
            title="Frequency vs Recency by Segment",
            labels={'x': 'Avg Recency (days)', 'y': 'Avg Frequency'},
            color_discrete_sequence=colors
        )
        fig_scatter.update_layout(height=350)
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Instructions for model integration
    with st.expander("🔧 Model Integration Instructions"):
        st.markdown("""
        **To integrate your trained segmentation model:**
        
        1. **Replace the `load_segmentation_model()` function:**
        ```python
        @st.cache_resource
        def load_segmentation_model():
            clustering_model = pickle.load(open('models/kmeans_model.pkl', 'rb'))
            scaler = pickle.load(open('models/rfm_scaler.pkl', 'rb'))
            cluster_labels = pickle.load(open('models/cluster_labels.pkl', 'rb'))
            return clustering_model, scaler, cluster_labels
        ```
        
        2. **Update the `predict_customer_segment()` function:**
        ```python
        def predict_customer_segment(recency, frequency, monetary, model_data):
            # Prepare input data
            rfm_data = np.array([[recency, frequency, monetary]])
            
            # Scale the data
            rfm_scaled = model_data['scaler'].transform(rfm_data)
            
            # Predict cluster
            cluster = model_data['clustering_model'].predict(rfm_scaled)[0]
            
            # Map cluster to segment label
            segment = model_data['cluster_labels'][cluster]
            
            return segment_details
        ```
        
        3. **Replace segment insights with your actual data:**
        ```python
        def get_segment_insights():
            # Load your actual segment statistics
            return your_segment_data
        ```
        """)

if __name__ == "__main__":
    main()