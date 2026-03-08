def calculate_business_metrics(df):

    df["sales_velocity"] = (
        df["monthly_sales"] /
        df["stock_quantity"]
    )

    slow_moving = df[
        df["sales_velocity"] < 0.2
    ]

    df["revenue_risk"] = df.apply(
        lambda row:
        (row["predicted_sales"] - row["stock_quantity"]) * 500
        if row["predicted_sales"] > row["stock_quantity"]
        else 0,
        axis=1
    )

    df["holding_cost"] = df.apply(
        lambda row:
        (row["stock_quantity"] - row["predicted_sales"]) * 50
        if row["stock_quantity"] > row["predicted_sales"]
        else 0,
        axis=1
    )

    lost_revenue = int(df["revenue_risk"].sum())
    holding_cost = int(df["holding_cost"].sum())

    return {
        "total_products": len(df),
        "total_stock": df["stock_quantity"].sum(),
        "slow_moving": slow_moving,
        "lost_revenue": lost_revenue,
        "holding_cost": holding_cost
    }