import os
import logging
from loader import load_inventory, load_sales
from sales_aggregator import aggregate_sales
from inventory_engine import reconcile_inventory
from reporter import generate_summary, generate_sales_graph

# Ensure logs directory exists
os.makedirs("../logs", exist_ok=True)

logging.basicConfig(
    filename="../logs/inventory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    inventory = load_inventory("./data/inventory.csv")python -m unittest discover tests
    sales = load_sales("./data/sales_transactions.csv")

    aggregated_sales, transactions_processed = aggregate_sales(sales, inventory)

    reconciled_df = reconcile_inventory(inventory, aggregated_sales)

    reconciled_df.to_csv("inventory_reconciliation.csv", index=False)

    generate_summary(reconciled_df, transactions_processed)

    generate_sales_graph(reconciled_df)

if __name__ == "__main__":
    main()