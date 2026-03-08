def generate_redistribution_plan(region_summary):

    high_regions = region_summary[
        region_summary["demand_ratio"] > 0.6
    ].copy()

    surplus_regions = region_summary[
        region_summary["demand_ratio"] < 0.25
    ].copy()

    high_regions["demand_gap"] = (
        high_regions["predicted_sales"] -
        high_regions["stock_quantity"]
    )

    surplus_regions["excess_stock"] = (
        surplus_regions["stock_quantity"] -
        surplus_regions["predicted_sales"]
    )

    high_regions = high_regions.sort_values(
        by="demand_gap",
        ascending=False
    )

    surplus_regions = surplus_regions.sort_values(
        by="excess_stock",
        ascending=False
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

    return redistribution_plan, high_regions, surplus_regions