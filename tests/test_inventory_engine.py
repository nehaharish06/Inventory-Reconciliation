import unittest
import pandas as pd
from src.inventory_engine import reconcile_inventory

class TestInventoryEngine(unittest.TestCase):

    def test_inventory_reduction(self):
        inventory = pd.DataFrame({
            "product_id":[1],
            "current_stock":[20],
            "unit_price":[10],
            "product_name":["A"],
            "category":["X"]
        })

        sales = pd.DataFrame({
            "product_id":[1],
            "total_sold_quantity":[5]
        })

        result = reconcile_inventory(inventory, sales)
        self.assertEqual(result["final_stock"].iloc[0], 15)

    def test_inventory_not_negative(self):
        inventory = pd.DataFrame({
            "product_id":[1],
            "current_stock":[5],
            "unit_price":[10],
            "product_name":["A"],
            "category":["X"]
        })

        sales = pd.DataFrame({
            "product_id":[1],
            "total_sold_quantity":[10]
        })

        result = reconcile_inventory(inventory, sales)
        self.assertEqual(result["final_stock"].iloc[0], 0)

    def test_zero_stock_status(self):
        inventory = pd.DataFrame({
            "product_id":[1],
            "current_stock":[5],
            "unit_price":[10],
            "product_name":["A"],
            "category":["X"]
        })

        sales = pd.DataFrame({
            "product_id":[1],
            "total_sold_quantity":[5]
        })

        result = reconcile_inventory(inventory, sales)
        self.assertEqual(result["stock_status"].iloc[0], "OUT_OF_STOCK")

if __name__ == "__main__":
    unittest.main()