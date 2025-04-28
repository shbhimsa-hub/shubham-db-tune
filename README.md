PostgreSQL Autovacuum Stress Testing Project

⸻

1. Environment Setup

Deployed and verified the following services using Docker Compose:
	•	PostgreSQL 15 database
	•	Prometheus for metrics collection
	•	Grafana for dashboard visualization
	•	PG Badger for PostgreSQL logs analysis

Docker Compose deployment and services running ✅
![Docker Running](dockercompose.png)
![Docker Running](docker-ps.png)

	•	Prometheus for metrics collection
![Prometheus Running](prometheus.png)
•	Grafana for dashboard visualization
![Grafana Running](grafana.png)
•	PG Badger for PostgreSQL logs analysis
![PGBadger Running](pg-badger.png)


Build an automated setup to simulate autovacuum overload in a PostgreSQL database by:
	•	Creating schema and indexes
	•	Loading mock real-world-like data
	•	Generating dead tuples aggressively
	•	Monitoring and proving autovacuum stress

Four autovacuum panels were added to grafana 
![Autovacuum panels](autovacuum-panel.png)

Tables are created and bulk dummy data was inserted using schema_and_data_loader_4_tables.py:

![Visualization during generating bulk data ](populating_data.png)

Stress the Autovacuum Process

Separate Python script (autovacuum_stress.py) runs:
	•	Full table UPDATEs (customers, orders, order_items, products)
	•	Random 15% DELETEs from orders and order_items each cycle
	•	Continuous workload without significant sleep delays

✅ This generates constant dead tuples faster than default autovacuum settings can clean.

✅ PostgreSQL autovacuum gets progressively overwhelmed.

![Autovacuum stressed](autovacuum-panel.png)












⸻
