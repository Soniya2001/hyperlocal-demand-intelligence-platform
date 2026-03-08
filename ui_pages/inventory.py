import streamlit as st
import pandas as pd
from utils.data_loader import load_inventory_data


def render_inventory():

    st.header("Inventory Analysis")

    uploaded_file = st.file_uploader("Upload Inventory CSV", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        st.info("Using generated dataset")
        df = load_inventory_data()

    st.subheader("Inventory Data")

    st.dataframe(df.head(50))

    st.subheader("Inventory Classification")

    df["sales_velocity"] = df["monthly_sales"] / df["stock_quantity"]

    df["status"] = df.apply(
        lambda row: "Slow-Moving"
        if row["sales_velocity"] < 0.2
        else "Normal",
        axis=1
    )

    st.dataframe(
        df[
            [
                "product_name",
                "region",
                "stock_quantity",
                "monthly_sales",
                "sales_velocity",
                "status"
            ]
        ].head(50)
    )

    st.subheader("Region Summary")

    region_summary = df.groupby("region").agg({
        "stock_quantity": "sum",
        "monthly_sales": "sum"
    }).reset_index()

    region_summary["demand_ratio"] = (
        region_summary["monthly_sales"] /
        region_summary["stock_quantity"]
    )

    st.dataframe(region_summary)

    st.bar_chart(region_summary.set_index("region")["demand_ratio"])