import unittest
import pandas as pd
from src.sales_aggregator import aggregate_sales

class TestSalesAggregator(unittest.TestCase):

    def test_multiple_sales_aggregation(self):
        inventory = pd.DataFrame({"product_id": [1]})
        sales = pd.DataFrame({
            "product_id": [1, 1],
            "transaction_date": ["2024-04-01", "2024-04-05"],
            "quantity_sold": [5, 3]
        })

        result, _ = aggregate_sales(sales, inventory)
        self.assertEqual(result[1], 8)

    def test_negative_quantity_ignored(self):
        inventory = pd.DataFrame({"product_id": [1]})
        sales = pd.DataFrame({
            "product_id": [1],
            "transaction_date": ["2024-04-01"],
            "quantity_sold": [-5]
        })

        result, _ = aggregate_sales(sales, inventory)
        self.assertEqual(result.get(1, 0), 0)