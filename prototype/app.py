import streamlit as st
import pandas as pd

st.set_page_config(page_title="OneMindAI", layout="wide")

st.title("OneMindAI – Hyperlocal Demand Intelligence Platform")
st.sidebar.title("Seller Panel")
st.sidebar.write("Seller: Madurai Retail Store")
# Sidebar Navigation
page = st.sidebar.selectbox(
    "Select Page",
    ["Dashboard",
     "Inventory Analysis",
     "Demand Forecasting",
     "Matching & Recommendations"]
)

# Page Routing Logic
if page == "Dashboard":

    df = pd.read_csv("hyperlocal_inventory_data.csv")

    st.header("Dashboard Overview")

    # Basic metrics
    total_products = len(df)
    total_stock = df["stock_quantity"].sum()

    df["sales_velocity"] = df["monthly_sales"] / df["stock_quantity"]
    slow_moving = df[df["sales_velocity"] < 0.2]

    # ---- ML MODEL ----
    df_encoded = pd.get_dummies(df, columns=["region", "category"])

    X = df_encoded.drop(columns=["monthly_sales", "product_name"])
    y = df_encoded["monthly_sales"]

    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X, y)

    df["predicted_sales"] = model.predict(X)
        # ---- REGION SUMMARY ----
    region_summary = df.groupby("region").agg({
        "stock_quantity": "sum",
        "predicted_sales": "sum"
    }).reset_index()

    region_summary["demand_ratio"] = (
        region_summary["predicted_sales"] /
        region_summary["stock_quantity"]
    )

    high_demand_regions = region_summary[
        region_summary["demand_ratio"] > 0.6
    ]

    surplus_regions = region_summary[
        region_summary["demand_ratio"] < 0.25
    ]

    # ---- KPI CARDS ----
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Products", total_products)
    col2.metric("Total Stock Units", total_stock)
    col3.metric("Slow Moving Items", len(slow_moving))
    col4.metric("High Demand Regions", len(high_demand_regions))

    st.divider()

    st.subheader("💰 Business Impact Metrics")

    # Estimated lost revenue (if demand > stock)
    df["revenue_risk"] = df.apply(
        lambda row:
        (row["predicted_sales"] - row["stock_quantity"]) * 500
        if row["predicted_sales"] > row["stock_quantity"]
        else 0,
        axis=1
        )

    # Estimated holding cost (if surplus stock)
    df["holding_cost"] = df.apply(
        lambda row:
        (row["stock_quantity"] - row["predicted_sales"]) * 50
        if row["stock_quantity"] > row["predicted_sales"]
        else 0,
        axis=1
        )

    lost_revenue = int(df["revenue_risk"].sum())
    holding_cost = int(df["holding_cost"].sum())

    colA, colB = st.columns(2)

    colA.metric("Potential Lost Revenue (₹)", f"{lost_revenue:,}")
    colB.metric("Estimated Holding Cost (₹)", f"{holding_cost:,}")


    st.subheader("🔄 Intelligent Redistribution Plan")

    high_regions = region_summary[
        region_summary["demand_ratio"] > 0.6
    ].copy()

    surplus_regions = region_summary[
        region_summary["demand_ratio"] < 0.25
    ].copy()

    # Calculate demand gap and surplus excess
    high_regions["demand_gap"] = (
        high_regions["predicted_sales"] -
        high_regions["stock_quantity"]
    )

    surplus_regions["excess_stock"] = (
        surplus_regions["stock_quantity"] -
        surplus_regions["predicted_sales"]
    )

    high_regions = high_regions.sort_values(
        by="demand_gap", ascending=False
    )

    surplus_regions = surplus_regions.sort_values(
        by="excess_stock", ascending=False
    )

    redistribution_plan = []

    for _, high in high_regions.iterrows():

        remaining_gap = high["demand_gap"]

        for idx, surplus in surplus_regions.iterrows():

            if remaining_gap <= 0:
                break

            available = surplus["excess_stock"]

            if available > 0 and remaining_gap > 0:

                transfer = int(min(remaining_gap, available))

                if transfer > 0:
                    redistribution_plan.append({
                        "From Region": surplus["region"],
                        "To Region": high["region"],
                        "Units to Transfer": transfer
                    })

                surplus_regions.at[idx, "excess_stock"] -= transfer
                remaining_gap -= transfer

    if redistribution_plan:
        st.dataframe(pd.DataFrame(redistribution_plan))
    else:
        st.success("Stock levels are balanced. No redistribution required.")

    # ---- CHART ----
    st.subheader("Region Demand Forecast")
    st.bar_chart(region_summary.set_index("region")["demand_ratio"])

    # ---- TABLE ----
    st.subheader("Top 5 Slow Moving Products")
    st.dataframe(
        slow_moving[[
            "product_name",
            "region",
            "stock_quantity",
            "monthly_sales"
        ]].head(5)
    )

elif page == "Inventory Analysis":
    st.header("Inventory Analysis")

    uploaded_file = st.file_uploader("Upload Inventory CSV", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        st.info("Using generated dataset")
        df = pd.read_csv("hyperlocal_inventory_data.csv")

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

    st.dataframe(df[["product_name", "region", "stock_quantity", "monthly_sales", "sales_velocity", "status"]].head(50))
    st.subheader("Region Summary")

    region_summary = df.groupby("region").agg({
        "stock_quantity": "sum",
        "monthly_sales": "sum"
    }).reset_index()

    region_summary["demand_ratio"] = region_summary["monthly_sales"] / region_summary["stock_quantity"]

    st.dataframe(region_summary)

    st.bar_chart(region_summary.set_index("region")["demand_ratio"])

elif page == "Demand Forecasting":
    st.header("Demand Forecasting")

    df = pd.read_csv("hyperlocal_inventory_data.csv")

    # Encode region
    df_encoded = pd.get_dummies(df, columns=["region", "category"])

    X = df_encoded.drop(columns=["monthly_sales", "product_name"])
    y = df_encoded["monthly_sales"]

    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_absolute_error

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    st.subheader("Model Performance")
    st.write(f"Mean Absolute Error: {round(mae, 2)}")

    # Add predictions back
    df["predicted_next_month_sales"] = model.predict(X)

    st.subheader("Forecasted Demand (Sample)")
    st.dataframe(
        df[[
            "product_name",
            "region",
            "monthly_sales",
            "predicted_next_month_sales"
        ]].head(50)
    )

elif page == "Matching & Recommendations":
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split

    df = pd.read_csv("hyperlocal_inventory_data.csv")

    # Encode region & category
    df_encoded = pd.get_dummies(df, columns=["region", "category"])

    X = df_encoded.drop(columns=["monthly_sales", "product_name"])
    y = df_encoded["monthly_sales"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    df["predicted_sales"] = model.predict(X)

    # Use predicted sales instead of actual
    region_summary = df.groupby("region").agg({
        "stock_quantity": "sum",
        "predicted_sales": "sum"
    }).reset_index()

    region_summary["demand_ratio"] = (
        region_summary["predicted_sales"] / region_summary["stock_quantity"]
    )

    st.subheader("Forecast-Based Region Demand Analysis")
    st.dataframe(region_summary)







































  