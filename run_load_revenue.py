import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('product_sales.db')
cursor = conn.cursor()

# Define the insert query
insert_query = """
INSERT INTO REVENUE (sku_id, date_id, price, sales, revenue)
SELECT 
    p.sku_id,
    s.orderdate_utc AS date_id,
    p.price,
    s.sales,
    p.price * s.sales AS revenue
FROM 
    product p
JOIN 
    sales s ON p.sku_id = s.sku_id;
"""

try:
    # Execute the insert statement
    cursor.execute(insert_query)
    # Commit the transaction
    conn.commit()
    print("Data inserted successfully.")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
finally:
    # Close the connection
    conn.close()
