import pandas as pd
import logging

def load_inventory(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        logging.error(f"Error loading inventory file: {e}")
        raise

def load_sales(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        logging.error(f"Error loading sales file: {e}")
        raise