import logging
from src.loader import load_csv
from src.sales_aggregator import aggregate_sales
from src.inventory_engine import reconcile_inventory
from src.reporter import generate_reports

logging.basicConfig(
    filename="logs/inventory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():

    inventory = load_csv("data/inventory.csv")
    sales = load_csv("data/sales_transactions.csv")

    sales_map, total_transactions = aggregate_sales(sales, inventory)

    results = reconcile_inventory(inventory, sales_map)

    summary = generate_reports(results, total_transactions)

    print("Inventory Reconciliation Completed")
    print(summary)

if __name__ == "__main__":
    main()