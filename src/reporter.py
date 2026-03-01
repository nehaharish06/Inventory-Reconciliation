import json
import pandas as pd

def generate_reports(results, total_transactions):

    df = pd.DataFrame(results)
    df.to_csv("inventory_reconciliation.csv", index=False)

    summary = {
        "total_products": len(df),
        "total_transactions_processed": total_transactions,
        "total_sales_value": round(df["total_sales_value"].sum(), 2),
        "low_stock_products": len(df[df["stock_status"] == "LOW_STOCK"]),
        "out_of_stock_products": len(df[df["stock_status"] == "OUT_OF_STOCK"])
    }

    with open("sales_summary.json", "w") as f:
        json.dump(summary, f, indent=4)

    return summary