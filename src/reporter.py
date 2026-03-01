import json
import pandas as pd

def generate_reports(results, total_transactions):

    df = pd.DataFrame(results)
    df.to_csv("inventory_reconciliation.csv", index=False)

    summary = {
        "total_products": int(len(results)),
        "total_transactions_processed": int(total_transactions),
        "total_sales_value": float(sum(r["total_sales_value"] for r in results)),
        "low_stock_products": int(sum(1 for r in results if r["stock_status"] == "LOW_STOCK")),
        "out_of_stock_products": int(sum(1 for r in results if r["stock_status"] == "OUT_OF_STOCK"))
    }

    with open("sales_summary.json", "w") as f:
        json.dump(summary, f, indent=4)

    return summary