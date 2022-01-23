from flask import Blueprint, Flask, render_template, request, redirect, url_for, session
from mysql.connector import MySQLConnection, Error

from Logic.MySql import *

def LoggedIn():
    if 'loggedin' in session:
        return True
    return False

def Authenticate(passHash):
    connectionDetails = Import_Connection_Details()
    conn = None
    cursor = None
    try:
        conn = MySQLConnection(**connectionDetails)

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM USERS WHERE PASSWORD_HASH = '{hashedPassword}'".format(hashedPassword=passHash))
            row = cursor.fetchone()

            while row is not None:
                return {
                    'id' : row[0],
                    'forenames' : row[1],
                    'surname' : row[2],
                    'permissions' : row[4]
                }
                row = cursor.fetchone()
        else:
            return("connection failed")
    
    except Error as error:
        return(error)
    
    finally:
            if conn is not None and conn.is_connected():
                cursor.close()
                conn.close()