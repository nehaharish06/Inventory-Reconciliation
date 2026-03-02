import pandas as pd
import logging

def aggregate_sales(sales_df, inventory_df):

    # Convert date
    sales_df["transaction_date"] = pd.to_datetime(
        sales_df["transaction_date"], errors="coerce"
    )

    # Filter April 2024
    sales_df = sales_df[
        (sales_df["transaction_date"].dt.month == 4) &
        (sales_df["transaction_date"].dt.year == 2024)
    ]

    # Remove invalid dates
    sales_df = sales_df.dropna(subset=["transaction_date"])

    # Remove negative quantities
    sales_df = sales_df[sales_df["quantity_sold"] >= 0]

    # Remove unknown product_ids
    valid_products = inventory_df["product_id"].tolist()
    invalid_products = sales_df[~sales_df["product_id"].isin(valid_products)]
    
    if not invalid_products.empty:
        logging.warning("Unknown product IDs detected")

    sales_df = sales_df[sales_df["product_id"].isin(valid_products)]

    # Aggregate
    aggregated = sales_df.groupby("product_id")["quantity_sold"].sum().reset_index()
    aggregated.rename(columns={"quantity_sold": "total_sold_quantity"}, inplace=True)

    return aggregated, len(sales_df)