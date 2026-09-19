import sqlite3
import pandas as pd
from pathlib import Path

DATA_FOLDER = Path("data/raw")
DATABASE_PATH = Path("data/olist.db")

def load_table(table_name, csv_file):
    csv_path = DATA_FOLDER / csv_file

    df = pd.read_csv(csv_path)

    connection = sqlite3.connect(DATABASE_PATH)

    df.to_sql(table_name, connection, if_exists="append", index=False)

    connection.close()

    print(f"{table_name} loaded: {len(df)} rows")

load_table("customers", "olist_customers_dataset.csv")
load_table("products", "olist_products_dataset.csv")
load_table("sellers", "olist_sellers_dataset.csv")
load_table("categories", "product_category_name_translation.csv")

load_table("orders", "olist_orders_dataset.csv")
load_table("order_items", "olist_order_items_dataset.csv")
load_table("payments", "olist_order_payments_dataset.csv")
load_table("reviews", "olist_order_reviews_dataset.csv")

