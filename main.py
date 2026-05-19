import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(os.getenv("DATABASE_URL"))

cursor = conn.cursor()

cursor.execute("""
SELECT c.company_name,
SUM(i.total_amount) AS total_billed
FROM invoice i
JOIN customer c
ON i.customer_id = c.customer_id
GROUP BY c.company_name
ORDER BY total_billed DESC;
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()