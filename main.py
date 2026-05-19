import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(
    os.getenv("DATABASE_URL")
)

cursor = conn.cursor()

cursor.execute("""
SELECT product_name, category, unit_price
FROM product;
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()
# single table query