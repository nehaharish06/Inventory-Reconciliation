def reconcile_inventory(inventory_df, sales_map):

    results = []

    for _, row in inventory_df.iterrows():

        product_id = row["product_id"]
        current_stock = row["current_stock"]
        unit_price = row["unit_price"]

        total_sold = sales_map.get(product_id, 0)
        final_stock = current_stock - total_sold

        stock_error = False
        if final_stock < 0:
            final_stock = 0
            stock_error = True

        # Stock status
        if final_stock == 0:
            stock_status = "OUT_OF_STOCK"
        elif 1 <= final_stock <= 10:
            stock_status = "LOW_STOCK"
        else:
            stock_status = "AVAILABLE"

        total_sales_value = total_sold * unit_price

        results.append({
            "product_id": product_id,
            "product_name": row["product_name"],
            "category": row["category"],
            "current_stock": current_stock,
            "total_sold_quantity": total_sold,
            "final_stock": final_stock,
            "stock_status": stock_status,
            "total_sales_value": total_sales_value
        })

    return results