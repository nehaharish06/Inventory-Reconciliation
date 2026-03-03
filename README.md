# Inventory Reconciliation & Sales Analysis Engine (Python)

## 📌 Project Overview

This project is a Python-based Inventory Reconciliation & Sales Analysis Engine built for an e-commerce company.

The system processes inventory and sales transaction data, applies business rules, reconciles stock levels, detects stock issues, and generates structured output reports along with visual analytics.

The application is modular, testable, and includes logging and unit test coverage.

---

## 🎯 Business Objective

The goal of this system is to:

- Reconcile inventory based on sales transactions  
- Identify low-stock and out-of-stock products  
- Detect invalid and inconsistent data  
- Generate sales summary reports  
- Provide visual insights through graphs  

---

## 📂 Input Data Files

### inventory.csv

| Column Name     | Description |
|---------------|------------|
| product_id     | Unique product identifier |
| product_name   | Name of the product |
| current_stock  | Current available stock |
| unit_price     | Price per unit |
| category       | Product category |

### sales_transactions.csv

| Column Name       | Description |
|------------------|------------|
| transaction_id    | Unique transaction ID |
| product_id        | Product identifier |
| transaction_date  | Date of sale |
| quantity_sold     | Units sold |

---

## ⚙️ Business Rules Implemented

### Sales Filtering

- Only transactions from April 2024 are considered.
- Invalid dates are ignored and logged.
- Negative quantities are ignored.

### Sales Aggregation

- Sales are aggregated per product.
- Unknown product IDs are logged individually.
- Invalid transactions are skipped safely.

### Inventory Reconciliation

final_stock = current_stock - total_sold_quantity

- If final_stock < 0 → set to 0.
- Stock status assigned based on final_stock.

### Stock Status Rules

| Condition | Status |
|----------|--------|
| final_stock = 0 | OUT_OF_STOCK |
| 1 ≤ final_stock ≤ 10 | LOW_STOCK |
| final_stock > 10 | AVAILABLE |

### Transformations Added

New fields generated:
- total_sold_quantity
- final_stock
- stock_status
- total_sales_value

---

## 📊 Graphs & Visualizations

The system generates the following analytics:

1. Top 5 Products by Sales Value  
   Shows the highest revenue-generating products.

2. Sales vs Remaining Stock Comparison  
   Helps identify potential stock risk and overstocking.

3. Category-wise Sales Value  
   Displays total revenue per product category.

These graphs support operational and strategic decision-making.

---

## 📤 Output Files

### inventory_reconciliation.csv

Contains:

- product_id  
- product_name  
- category  
- current_stock  
- total_sold_quantity  
- final_stock  
- stock_status  
- total_sales_value  

### sales_summary.json

Contains:

- total_products  
- total_transactions_processed  
- total_sales_value  
- low_stock_products  
- out_of_stock_products  

---

## 📝 Logging

Logging is implemented using Python's logging module.

Errors logged include:
- Invalid product IDs (logged individually)
- Invalid dates
- Data inconsistencies

Logs are stored in:

logs/inventory.log

---

## 🧪 Unit Testing

Framework Used:
- unittest

Test coverage includes:
- Sales aggregation logic
- Inventory reconciliation
- Stock status determination

Example Test Cases:

Sales Aggregation Tests:
- test_multiple_sales_aggregation
- test_invalid_transaction_date
- test_negative_quantity_ignored

Inventory Calculation Tests:
- test_inventory_reduction
- test_inventory_not_negative
- test_zero_stock_status

Stock Status Tests:
- test_available_status
- test_low_stock_status
- test_out_of_stock_status

---

## 🏗️ Project Structure

Inventory-Reconcilation/
│── data/
│── src/
│── tests/
│── logs/
│── sales_summary.json
│── README.md
|── inventory_reconciliation.csv

---

## ▶️ How to Run

1. Install Dependencies

pip install pandas matplotlib

2. Run Application

python src/main.py

3. Run Unit Tests

python -m unittest discover tests

---

## 🔒 Error Handling & Edge Cases

Handled cases:

- Invalid transaction dates
- Negative sales quantities
- Unknown product IDs
- Stock going below zero
- Empty sales records
- Safe handling of bad data (no application crash)

---

## 📌 Assumptions

- Inventory file contains unique product IDs.
- Sales file may contain invalid or inconsistent data.
- Only April 2024 transactions are relevant.
- Unit price remains constant during the period.

---

## 💼 Technologies Used

- Python 3.x
- Pandas
- Matplotlib
- JSON
- Logging
- unittest

---


## ✅ Project Status

- End-to-end processing  
- Business rules applied  
- Logging implemented  
- Unit tests written  
- Graphical analytics added  