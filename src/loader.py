import pandas as pd
import logging

def load_csv(path):
    try:
        return pd.read_csv(path)
    except Exception as e:
        logging.error(f"Error loading file {path}: {e}")
        return pd.DataFrame()