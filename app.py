import streamlit as st

# Import page functions
from ui_pages.dashboard import render_dashboard
from ui_pages.inventory import render_inventory
from ui_pages.forecasting import render_forecasting
from ui_pages.matching import render_matching

# App Config
st.set_page_config(
    page_title="OneMindAI",
    page_icon="🧠",
    layout="wide"
)

# App Title
st.title("OneMindAI – Hyperlocal Demand Intelligence Platform")
st.markdown("""
AI-powered platform that helps retailers **detect supply-demand imbalance**, 
**forecast regional demand**, and **optimize inventory distribution** using Machine Learning and Generative AI.

### 🚀 Key Capabilities
- 📈 **Demand Forecasting** using Machine Learning
- 📦 **Inventory Classification** to detect slow-moving products
- 🔄 **Hyperlocal Redistribution Engine** to balance regional supply
- 🤖 **GenAI Strategic Insights** powered by AWS Bedrock

---
""")
st.info(
"This prototype demonstrates how AI can identify supply-demand imbalance "
"across regions and recommend intelligent inventory redistribution to reduce "
"lost revenue and holding costs. The demo uses synthetic retail data for illustration."
)

# Sidebar
st.sidebar.title("Seller Panel")
st.sidebar.write("Seller: Madurai Retail Store")

# Navigation
page = st.sidebar.selectbox(
    "Select Page",
    [
        "Dashboard",
        "Inventory Analysis",
        "Demand Forecasting",
        "Matching & Recommendations"
    ]
)

# Page Routing
if page == "Dashboard":
    render_dashboard()

elif page == "Inventory Analysis":
    render_inventory()

elif page == "Demand Forecasting":
    render_forecasting()

elif page == "Matching & Recommendations":
    render_matching()