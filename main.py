import psycopg2

connection_string = "postgresql://neondb_owner:npg_ZkS7teI2QDgv@ep-curly-dust-am2ew268-pooler.c-5.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

conn = psycopg2.connect(connection_string)

cur = conn.cursor()

print("Connected!")

# Customers
cur.execute("SELECT * FROM customer LIMIT 5;")

customers = cur.fetchall()

print("\nCUSTOMERS")
for row in customers:
    print(row)

# Products
cur.execute("SELECT * FROM product LIMIT 5;")

products = cur.fetchall()

print("\nPRODUCTS")
for row in products:
    print(row)

# Invoices
cur.execute("SELECT * FROM invoice LIMIT 5;")

invoices = cur.fetchall()

print("\nINVOICES")
for row in invoices:
    print(row)

cur.close()
conn.close()