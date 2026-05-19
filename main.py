import psycopg2
from dotenv import load_dotenv
import os

# Load DATABASE_URL from .env
load_dotenv()

conn = psycopg2.connect(
    os.getenv("DATABASE_URL")
)

# Cursor runs SQL
cursor = conn.cursor()

# Query customers
cursor.execute("SELECT * FROM customer;")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()