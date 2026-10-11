import sqlite3

connection = sqlite3.connect("orders.db")

cursor = connection.execute("""
    SELECT customer_name, amount
    FROM orders
    WHERE amount > 500
    ORDER BY amount DESC
""")

for row in cursor.fetchall():
    print(row)

connection.close()