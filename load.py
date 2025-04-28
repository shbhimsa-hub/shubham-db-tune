import psycopg
import time

conn = psycopg.connect(
    host="172.30.0.2",
    port=5433,
    user="postgres",
    password="postgres",
    dbname="db_tune_autovacuum"
)
conn.autocommit = True
cur = conn.cursor()

print("Starting workload to generate dead tuples...")

while True:
    cur.execute("UPDATE client SET price = price + 1 WHERE id % 5 = 0")
    cur.execute("DELETE FROM client WHERE id % 7 = 0")
    cur.execute("""
        INSERT INTO client (customer_id, product, quantity, price)
        SELECT
            (random() * 1000)::INT + 1,
            'Product ' || (random() * 100)::INT,
            (random() * 10)::INT + 1,
            round(random() * 100, 2)
        FROM generate_series(1, 5000)
    """)
    print("Workload iteration completed.")
    time.sleep(2)
