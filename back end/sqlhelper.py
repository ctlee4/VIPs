import mysql.connector
from mysql.connector import Error

def create_connection(hostname, username, userpw, database):
    connection = None
    try: # Try to connect to the database. can fail if the credentials are wrong, or if the database is not running
        connection = mysql.connector.connect(
            host=hostname, 
            user=username,
            password=userpw,
            database=database
        )
        print("Connection successful")
    except Error as e:
        print(f"Error {e} occured") 
    return connection # Return the connection object, which can be used to interact with the database


def execute_query(connection, query):
    cursor = connection.cursor() #this is empty because we are not getting anything back
    try:
        cursor.execute(query)
        connection.commit() #commit the transaction to save changes to the database
        print("Query executed successfully")
    except Error as e:
        print(f"Error {e} occured")


def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall() #fetch all results from the query and return them as a list of dictionaries
        return result
    except Error as e:
        print(f"Error {e} occured")
        return None