import pandas as pd
import logging

def aggregate_sales(sales_df, inventory_df):

    sales_df["transaction_date"] = pd.to_datetime(
        sales_df["transaction_date"],
        errors="coerce"
    )

    # Filter April 2024
    sales_df = sales_df[
        (sales_df["transaction_date"].dt.month == 4) &
        (sales_df["transaction_date"].dt.year == 2024)
    ]

    # Remove invalid dates
    sales_df = sales_df.dropna(subset=["transaction_date"])

    # Ignore negative quantities
    sales_df = sales_df[sales_df["quantity_sold"] >= 0]

    # Validate product_id exists in inventory
    valid_products = set(inventory_df["product_id"])
    invalid_products = sales_df[~sales_df["product_id"].isin(valid_products)]

    for _, row in invalid_products.iterrows():
        logging.warning(f"Invalid product ID in sales: {row['product_id']}")

    sales_df = sales_df[sales_df["product_id"].isin(valid_products)]

    # Aggregate
    aggregation = sales_df.groupby("product_id")["quantity_sold"].sum().to_dict()

    return aggregation, len(sales_df)