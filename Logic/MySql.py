from configparser import ConfigParser
from mysql.connector import MySQLConnection, Error

def Import_Connection_Details():
    parser = ConfigParser()
    parser.read("MysqlConnection.ini")

    db = {}
    if parser.has_section('mysql'):
        items = parser.items('mysql')
        for item in items:
            db[item[0]] = item[1]
        return db
    else:
        raise Exception('{0} not found in the {1} file'.format('mysql', filename))

def Execute_No_Response_Query(query, args):
    connectionDetails = Import_Connection_Details()
    conn = None
    cursor = None
    try:
        conn = MySQLConnection(**connectionDetails)

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()
        else:
            print("connection failed")
    
    except Error as error:
        print(error)
    
    finally:
            if conn is not None and conn.is_connected():
                cursor.close()
                conn.close()