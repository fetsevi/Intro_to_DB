import mysql.connector
from mysql.connector import Error

def create_database():
    # Connect to MySQL Server
    try:
        connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Fr@nc01$1er"
        )

        if connection.is_connected():
            cursor=connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        try:
            if cursor:
                cursor.close()
            if connection.is_connected():
                connection.close()
        except NameError:
            pass

if __name__=="__main__":
    create_database()