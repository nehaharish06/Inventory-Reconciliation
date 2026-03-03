
import json
import matplotlib.pyplot as plt

def generate_summary(df, transactions_processed):

    summary = {
        "total_products": len(df),
        "total_transactions_processed": transactions_processed,
        "total_sales_value": float(df["total_sales_value"].sum()),
        "low_stock_products": int((df["stock_status"] == "LOW_STOCK").sum()),
        "out_of_stock_products": int((df["stock_status"] == "OUT_OF_STOCK").sum())
    }

    with open("sales_summary.json", "w") as f:
        json.dump(summary, f, indent=4)

    return summary


def generate_sales_graph(df):

    top_products = df.sort_values(
        by="total_sales_value", ascending=False
    ).head(5)

    plt.figure()
    plt.bar(top_products["product_name"], top_products["total_sales_value"])
    plt.xticks(rotation=45)
    plt.title("Top 5 Products by Sales Value - April 2024")
    plt.xlabel("Product")
    plt.ylabel("Sales Value")
    plt.tight_layout()
    plt.show()

def generate_category_sales_graph(df):

    category_sales = df.groupby("category")["total_sales_value"].sum()

    plt.figure()
    plt.bar(category_sales.index, category_sales.values)
    plt.xticks(rotation=45)
    plt.title("Sales Value by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales Value")
    plt.tight_layout()
    plt.show()

def generate_sales_vs_stock_graph(df):

    top_products = df.sort_values(
        by="total_sold_quantity", ascending=False
    ).head(5)

    plt.figure()
    plt.bar(top_products["product_name"], top_products["total_sold_quantity"])
    plt.title("Top 5 Products - Quantity Sold")
    plt.xlabel("Product")
    plt.ylabel("Quantity Sold")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()