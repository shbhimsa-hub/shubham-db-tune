-- Create a new user for Grafana
CREATE USER grafana_user WITH PASSWORD 'grafana_password';

-- Grant read-only access to the specific database
GRANT CONNECT ON DATABASE db_tune_autovacuum TO grafana_user;
GRANT USAGE ON SCHEMA public TO grafana_user;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO grafana_user;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO grafana_user;

-- Optionally, grant the user the ability to use functions (if necessary)
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO grafana_user;

-- If you want this user to have access to new tables created in the future:
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO grafana_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON SEQUENCES TO grafana_user;

-- Enable the pgcrypto extension for generating random UUIDs
CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE customers (

    id SERIAL PRIMARY KEY,

    name TEXT NOT NULL,

    email TEXT UNIQUE NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

 

 

 

 

CREATE TABLE products (

    id SERIAL PRIMARY KEY,

    name TEXT NOT NULL,

    price NUMERIC(10, 2) NOT NULL,

    stock INT NOT NULL,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

 

 

 

 

CREATE TABLE orders (

    id SERIAL PRIMARY KEY,

    customer_id INT NOT NULL,

    total_amount NUMERIC(10, 2),

    order_date DATE DEFAULT CURRENT_DATE

);

 

 

 

 

CREATE TABLE order_items (

    id SERIAL PRIMARY KEY,

    order_id INT NOT NULL,

    product_id INT NOT NULL,

    quantity INT NOT NULL,

    item_price NUMERIC(10, 2) NOT NULL

);



