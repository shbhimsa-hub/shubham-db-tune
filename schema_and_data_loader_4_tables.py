import psycopg
import random
from datetime import datetime, timedelta

# Connect to PostgreSQL
conn = psycopg.connect(
    host="127.0.0.1",
    port=5433,
    dbname="db_tune_autovacuum",
    user="postgres",
    password="postgres",
    autocommit=True
)

with conn.cursor() as cur:
    # Drop and recreate tables
    cur.execute("DROP TABLE IF EXISTS order_items")
    cur.execute("DROP TABLE IF EXISTS orders")
    cur.execute("DROP TABLE IF EXISTS products")
    cur.execute("DROP TABLE IF EXISTS customers")

    cur.execute("""
        CREATE TABLE customers (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            signup_date TIMESTAMP NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE products (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            price NUMERIC(10,2) NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE orders (
            id SERIAL PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            order_date TIMESTAMP NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE order_items (
            id SERIAL PRIMARY KEY,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)

    print(" Tables created.")

    # Insert customers
    batch_size = 10000
    total_batches = 100  # 100 batches × 10,000 = 1 million rows
    for batch in range(total_batches):
        customers = [
            (
                f"User {i}",
                f"user{i}@example.com",
                datetime.now() - timedelta(days=random.randint(0, 365))
            ) for i in range(batch * batch_size, (batch + 1) * batch_size)
        ]
        cur.executemany(
            "INSERT INTO customers (name, email, signup_date) VALUES (%s, %s, %s)",
            customers
        )
        print(f"Inserted batch {batch + 1}/100 customers")

    # Insert products
    for batch in range(1):  # Only once — 10,000 products
        products = [
            (
                f"Product {i}",
                round(random.uniform(10, 500), 2)
            ) for i in range(1, 10001)
        ]
        cur.executemany(
            "INSERT INTO products (name, price) VALUES (%s, %s)",
            products
        )
        print("Inserted 10,000 products.")

    # Insert orders
    for batch in range(total_batches):
        orders = [
            (
                random.randint(1, 1000000),
                datetime.now() - timedelta(days=random.randint(0, 365))
            ) for _ in range(batch_size)
        ]
        cur.executemany(
            "INSERT INTO orders (customer_id, order_date) VALUES (%s, %s)",
            orders
        )
        print(f"Inserted batch {batch + 1}/100 orders")

    # Insert order_items
    for batch in range(total_batches):
        order_items = [
            (
                random.randint(1, 1000000),
                random.randint(1, 10000),
                random.randint(1, 5)
            ) for _ in range(batch_size)
        ]
        cur.executemany(
            "INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)",
            order_items
        )
        print(f"Inserted batch {batch + 1}/100 order_items")

print("Loaded 1 million rows into each table successfully.")
conn.close()
