import pandas as pd
from sklearn.linear_model import LinearRegression


def train_forecast_model(df):
    """
    Train demand forecasting model and generate predicted sales.
    """

    # Encode categorical features
    df_encoded = pd.get_dummies(df, columns=["region", "category"])

    X = df_encoded.drop(columns=["monthly_sales", "product_name"])
    y = df_encoded["monthly_sales"]

    model = LinearRegression()
    model.fit(X, y)

    df["predicted_sales"] = model.predict(X)

    # Region summary
    region_summary = df.groupby("region").agg({
        "stock_quantity": "sum",
        "predicted_sales": "sum"
    }).reset_index()

    region_summary["demand_ratio"] = (
        region_summary["predicted_sales"] /
        region_summary["stock_quantity"]
    )

    return df, region_summary