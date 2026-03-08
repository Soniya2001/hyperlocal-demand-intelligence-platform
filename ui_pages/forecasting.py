import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

from utils.data_loader import load_inventory_data


def render_forecasting():

    st.header("Demand Forecasting")

    df = load_inventory_data()

    df_encoded = pd.get_dummies(df, columns=["region", "category"])

    X = df_encoded.drop(columns=["monthly_sales", "product_name"])
    y = df_encoded["monthly_sales"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    st.subheader("Model Performance")
    st.write(f"Mean Absolute Error: {round(mae, 2)}")

    df["predicted_next_month_sales"] = model.predict(X)

    st.subheader("Forecasted Demand (Sample)")

    st.dataframe(
        df[
            [
                "product_name",
                "region",
                "monthly_sales",
                "predicted_next_month_sales"
            ]
        ].head(50)
    )