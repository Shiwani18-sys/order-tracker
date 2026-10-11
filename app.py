
import sqlite3


DB_NAME = "orders.db"


def create_table():
    with sqlite3.connect(DB_NAME) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                amount REAL NOT NULL
            )
        """)


def add_order(customer_name, amount):
    if not customer_name.strip():
        raise ValueError("Customer name cannot be empty")

    if amount <= 0:
        raise ValueError("Amount must be positive")

    with sqlite3.connect(DB_NAME) as connection:
        connection.execute(
            "INSERT INTO orders (customer_name, amount) VALUES (?, ?)",
            (customer_name, amount)
        )


def get_orders():
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.execute(
            "SELECT order_id, customer_name, amount FROM orders"
        )
        return cursor.fetchall()


if __name__ == "__main__":
    create_table()
    
    if not get_orders():
        add_order("Anuska", 500)
        add_order("Rahul", 750)

    for order in get_orders():
        print(order)
