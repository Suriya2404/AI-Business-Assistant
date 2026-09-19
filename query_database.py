import sqlite3

DATABASE_PATH = "data/olist.db"


def run_query(query):
    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute(query)

    results = cursor.fetchall()

    connection.close()

    return results

query = """
SELECT
    c.customer_state,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_state
ORDER BY total_orders DESC;
"""

results = run_query(query)

print(results)