import streamlit as st
import pandas as pd

from utils.data_loader import load_inventory_data
from services.forecasting_service import train_forecast_model


def render_matching():

    st.header("Matching & Recommendations")

    df = load_inventory_data()

    df, region_summary = train_forecast_model(df)

    st.subheader("Forecast-Based Region Demand Analysis")

    st.dataframe(region_summary)