import psycopg
import time

conn = psycopg.connect(
    host="127.0.0.1",
    port=5433,
    dbname="db_tune_autovacuum",
    user="postgres",
    password="postgres",
    autocommit=True
)

with conn.cursor() as cur:
    while True:
        print("Mass updating customers...")
        cur.execute("""
            UPDATE customers
            SET name = name || '_dead'
        """)

        print("Mass updating products...")
        cur.execute("""
            UPDATE products
            SET price = price + 1
        """)

        print("Mass updating orders...")
        cur.execute("""
            UPDATE orders
            SET order_date = order_date + INTERVAL '1 day'
        """)

        print("Mass updating order_items...")
        cur.execute("""
            UPDATE order_items
            SET quantity = quantity + 1
        """)

        print("Mass deleting 15% of orders randomly...")
        cur.execute("""
            DELETE FROM orders
            WHERE id IN (
                SELECT id FROM orders
                ORDER BY random()
                LIMIT (SELECT count(*) * 0.15 FROM orders)
            )
        """)

        print("Mass deleting 15% of order_items randomly...")
        cur.execute("""
            DELETE FROM order_items
            WHERE id IN (
                SELECT id FROM order_items
                ORDER BY random()
                LIMIT (SELECT count(*) * 0.15 FROM order_items)
            )
        """)

        time.sleep(1)
