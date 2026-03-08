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