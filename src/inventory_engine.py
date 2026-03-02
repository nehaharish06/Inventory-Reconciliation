import pandas as pd

def reconcile_inventory(inventory_df, aggregated_sales):

    df = inventory_df.merge(aggregated_sales, on="product_id", how="left")
    df["total_sold_quantity"] = df["total_sold_quantity"].fillna(0)

    df["final_stock"] = df["current_stock"] - df["total_sold_quantity"]

    # Prevent negative stock
    df.loc[df["final_stock"] < 0, "final_stock"] = 0

    # Stock Status
    def get_status(stock):
        if stock == 0:
            return "OUT_OF_STOCK"
        elif 1 <= stock <= 10:
            return "LOW_STOCK"
        else:
            return "AVAILABLE"

    df["stock_status"] = df["final_stock"].apply(get_status)

    df["total_sales_value"] = df["total_sold_quantity"] * df["unit_price"]

    return df