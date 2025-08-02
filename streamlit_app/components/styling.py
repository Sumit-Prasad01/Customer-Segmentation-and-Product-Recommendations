import streamlit as st

def apply_custom_css():
    """Apply custom CSS styling to the Streamlit app"""
    
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Main app styling */
    .main {
        padding-top: 2rem;
    }
    
    /* Typography */
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        font-size: 1.1rem;
        font-weight: 300;
        opacity: 0.9;
        margin: 0;
    }
    
    /* Sidebar styling */
    .sidebar-header {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .sidebar-header h2 {
        margin: 0;
        font-weight: 600;
    }
    
    .sidebar-header p {
        margin: 0.5rem 0 0 0;
        font-size: 0.9rem;
        opacity: 0.9;
    }
    
    .sidebar-footer {
        text-align: center;
        color: #666;
        font-size: 0.8rem;
    }
    
    /* Card styling */
    .welcome-card, .feature-card, .info-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
        border-left: 5px solid #667eea;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .welcome-card:hover, .feature-card:hover, .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }
    
    .feature-card {
        border-left-color: #4ECDC4;
    }
    
    .info-card {
        border-left-color: #45B7D1;
    }
    
    /* Product cards */
    .product-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 3px 15px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-left: 4px solid #4ECDC4;
        transition: all 0.3s ease;
    }
    
    .product-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 25px rgba(0,0,0,0.15);
    }
    
    .product-card.selected {
        border-left-color: #FF6B6B;
        background: linear-gradient(135deg, #fff5f5 0%, #ffffff 100%);
    }
    
    .product-card h4 {
        color: #333;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }
    
    /* Recommendation cards */
    .recommendation-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e9ecef;
        margin-bottom: 1rem;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .recommendation-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: linear-gradient(135deg, #4ECDC4 0%, #44A08D 100%);
    }
    
    .recommendation-card:hover {
        transform: translateX(5px);
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    }
    
    .rec-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }
    
    .rec-header h4 {
        margin: 0;
        color: #333;
        font-weight: 600;
    }
    
    .similarity-badge {
        background: linear-gradient(135deg, #4ECDC4 0%, #44A08D 100%);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
    }
    
    /* Segment cards */
    .segment-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 3px 15px rgba(0,0,0,0.08);
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }
    
    .segment-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 25px rgba(0,0,0,0.12);
    }
    
    .segment-result {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 1.5rem;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    }
    
    .segment-result h3 {
        margin-top: 0;
        font-weight: 700;
        font-size: 1.5rem;
    }
    
    /* Metrics styling */
    .metric-container {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 3px 15px rgba(0,0,0,0.08);
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .metric-container:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 25px rgba(0,0,0,0.12);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 3px 10px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Form styling */
    .stNumberInput > div > div > input {
        border-radius: 8px;
        border: 2px solid #e9ecef;
        transition: border-color 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    .stSelectbox > div > div > select {
        border-radius: 8px;
        border: 2px solid #e9ecef;
        transition: border-color 0.3s ease;
    }
    
    .stTextInput > div > div > input {
        border-radius: 8px;
        border: 2px solid #e9ecef;
        transition: border-color 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Charts and plots */
    .plotly-graph-div {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 3px 15px rgba(0,0,0,0.08);
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        border-radius: 12px;
        margin-top: 2rem;
        color: #666;
    }
    
    /* Alert and info boxes */
    .stAlert {
        border-radius: 10px;
        border: none;
        box-shadow: 0 3px 15px rgba(0,0,0,0.08);
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        border-radius: 8px;
        border: 1px solid #e9ecef;
    }
    
    /* Progress bar */
    .stProgress > div > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    /* Success/Error messages */
    .success-message {
        background: linear-gradient(135deg, #d4edda 0%, #ffffff 100%);
        color: #155724;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
    }
    
    .error-message {
        background: linear-gradient(135deg, #f8d7da 0%, #ffffff 100%);
        color: #721c24;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #dc3545;
        margin: 1rem 0;
    }
    
    /* Loading spinner customization */
    .stSpinner > div {
        border-top-color: #667eea !important;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 2rem;
        }
        
        .main-header p {
            font-size: 1rem;
        }
        
        .product-card, .recommendation-card, .segment-card {
            padding: 1rem;
        }
        
        .welcome-card, .feature-card, .info-card {
            padding: 1.5rem;
        }
    }
    
    /* Animation classes */
    .fade-in {
        animation: fadeIn 0.5s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .slide-in {
        animation: slideIn 0.3s ease-out;
    }
    
    @keyframes slideIn {
        from { transform: translateX(-20px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    </style>
    """, unsafe_allow_html=True)

def apply_page_specific_css(page_type):
    """Apply page-specific CSS styling"""
    
    if page_type == "product_recommendations":
        st.markdown("""
        <style>
        .recommendation-section {
            background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
        }
        
        .product-search-container {
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 3px 15px rgba(0,0,0,0.08);
        }
        </style>
        """, unsafe_allow_html=True)
        
    elif page_type == "customer_segmentation":
        st.markdown("""
        <style>
        .rfm-input-section {
            background: linear-gradient(135deg, #fff5f5 0%, #ffffff 100%);
            padding: 2rem;
            border-radius: 15px;
            border-left: 5px solid #FF6B6B;
        }
        
        .segment-analysis {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }
        </style>
        """, unsafe_allow_html=True)