import unittest
import pandas as pd
from src.sales_aggregator import aggregate_sales

class TestSalesAggregation(unittest.TestCase):

    def test_multiple_sales_aggregation(self):
        inventory = pd.DataFrame({
            "product_id": [1]
        })

        sales = pd.DataFrame({
            "transaction_id": [1,2],
            "product_id": [1,1],
            "transaction_date": ["2024-04-01","2024-04-02"],
            "quantity_sold": [5,5]
        })

        agg, _ = aggregate_sales(sales, inventory)
        self.assertEqual(agg["total_sold_quantity"].iloc[0], 10)

    def test_negative_quantity_ignored(self):
        inventory = pd.DataFrame({"product_id": [1]})
        sales = pd.DataFrame({
            "transaction_id":[1],
            "product_id":[1],
            "transaction_date":["2024-04-01"],
            "quantity_sold":[-5]
        })

        agg, _ = aggregate_sales(sales, inventory)
        self.assertTrue(agg.empty)

    def test_invalid_transaction_date(self):
        inventory = pd.DataFrame({"product_id":[1]})
        sales = pd.DataFrame({
            "transaction_id":[1],
            "product_id":[1],
            "transaction_date":["invalid"],
            "quantity_sold":[5]
        })

        agg, _ = aggregate_sales(sales, inventory)
        self.assertTrue(agg.empty)

if __name__ == "__main__":
    unittest.main()