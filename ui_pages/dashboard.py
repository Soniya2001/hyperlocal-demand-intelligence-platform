import streamlit as st
import pandas as pd

from utils.data_loader import load_inventory_data
from services.forecasting_service import train_forecast_model
from services.redistribution_service import generate_redistribution_plan
from services.bedrock_client import generate_ai_summary
from utils.metrics import calculate_business_metrics


def render_dashboard():

    st.header("Dashboard Overview")

    df = load_inventory_data()

    # Train ML model
    df, region_summary = train_forecast_model(df)

    # Business metrics
    metrics = calculate_business_metrics(df)

    total_products = metrics["total_products"]
    total_stock = metrics["total_stock"]
    slow_moving = metrics["slow_moving"]
    lost_revenue = metrics["lost_revenue"]
    holding_cost = metrics["holding_cost"]

    high_demand_regions = region_summary[
        region_summary["demand_ratio"] > 0.6
    ]

    # KPI CARDS
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Products", total_products)
    col2.metric("Total Stock Units", total_stock)
    col3.metric("Slow Moving Items", len(slow_moving))
    col4.metric("High Demand Regions", len(high_demand_regions))

    st.divider()

    # Business Impact
    st.subheader("💰 Business Impact Metrics")

    colA, colB = st.columns(2)

    colA.metric("Potential Lost Revenue (₹)", f"{lost_revenue:,}")
    colB.metric("Estimated Holding Cost (₹)", f"{holding_cost:,}")

    # Risk Indicator
    st.subheader("⚠️ Operational Risk Level")

    if lost_revenue > holding_cost * 1.2:
        st.error("🔴 High Risk: Revenue loss exposure is significantly higher than holding cost.")
    elif lost_revenue > holding_cost * 0.7:
        st.warning("🟡 Moderate Risk: Supply-demand imbalance requires attention.")
    else:
        st.success("🟢 Stable: Inventory levels are relatively balanced.")

    # Redistribution Plan
    st.subheader("🔄 Intelligent Redistribution Plan")

    redistribution_plan, high_regions, surplus_regions = generate_redistribution_plan(region_summary)

    if redistribution_plan:
        st.dataframe(pd.DataFrame(redistribution_plan))
    else:
        st.success("Stock levels are balanced. No redistribution required.")

    # AI Summary
    st.subheader("🧠 GenAI Strategic Summary")

    summary = generate_ai_summary(
        high_regions,
        surplus_regions,
        lost_revenue,
        holding_cost,
        redistribution_plan
    )

    st.markdown(summary)

    # Chart
    st.subheader("Region Demand Forecast")
    st.bar_chart(region_summary.set_index("region")["demand_ratio"])

    # Slow moving table
    st.subheader("Top 5 Slow Moving Products")

    st.dataframe(
        slow_moving[
            [
                "product_name",
                "region",
                "stock_quantity",
                "monthly_sales"
            ]
        ].head(5)
    )