import mysql.connector
from mysql.connector import errorcode

try:
    # Connect to MySQL server (no database specified yet)
    conn = mysql.connector.connect(
        host="localhost",
        user="awonkevintwembi",
        password="Awonke@01"
    )
    cursor = conn.cursor()

    # Try to create the database
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Invalid username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Error: Database does not exist.")
    else:
        print(f"Error: {err}")
finally:
    # Close cursor and connection if they were opened
    try:
        cursor.close()
        conn.close()
    except:
        pass