from Logic.MySql import *
from mysql.connector import MySQLConnection, Error

def GetPrintQueue():
    connectionDetails = Import_Connection_Details()
    conn = None
    cursor = None
    try:
        conn = MySQLConnection(**connectionDetails)

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM PRINT")
            row = cursor.fetchone()
            data = []

            while row is not None:
                val = {
                    'print_id' : row[0],
                    'function_id' : row[1],
                    'data' : row[2],
                    'sender' : row[3],
                    'attributes' : row[4]
                }
                data.append(val)
                row = cursor.fetchone()
            
            return data
        else:
            print("connection failed")
    
    except Error as error:
        print(error)
    
    finally:
            if conn is not None and conn.is_connected():
                cursor.close()
                conn.close()

def InsertPrintItem(function_id, data, sender, attributes):
    query = "INSERT INTO PRINT(FUNCTION_ID, DATA, SENDER, ATTRIBUTES) VALUES (%s,%s,%s,%s)"
    args = (function_id, data, sender, attributes)
    Execute_No_Response_Query(query, args)

def DeletePrintItem(print_id):
    query = "DELETE FROM PRINT WHERE PRINT_ID = %s"
    args = (print_id, )
    Execute_No_Response_Query(query, args)

        