import unittest
import pandas as pd
from src.inventory_engine import reconcile_inventory

class TestInventoryEngine(unittest.TestCase):

    def test_inventory_reduction(self):
        inventory = pd.DataFrame({
            "product_id": [1],
            "product_name": ["A"],
            "current_stock": [20],
            "unit_price": [100],
            "category": ["Electronics"]
        })

        sales_map = {1: 5}
        results = reconcile_inventory(inventory, sales_map)

        self.assertEqual(results[0]["final_stock"], 15)

    def test_inventory_not_negative(self):
        inventory = pd.DataFrame({
            "product_id": [1],
            "product_name": ["A"],
            "current_stock": [5],
            "unit_price": [100],
            "category": ["Electronics"]
        })

        sales_map = {1: 10}
        results = reconcile_inventory(inventory, sales_map)

        self.assertEqual(results[0]["final_stock"], 0)
        self.assertEqual(results[0]["stock_status"], "OUT_OF_STOCK")