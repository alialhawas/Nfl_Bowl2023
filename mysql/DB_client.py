import mysql.connector
import os  

def crate_connect():
    return mysql.connector.connect(user='root', password= 1,
                              host='localhost',
                              database= 'nflbowl')

def create_cursor(connection):
    return connection.cursor()

def execute_quaer(cursor, query):
    return cursor.execute(query)

def close_connection(cursor, connection):
    cursor.close()
    connection.close()

    















# import MySQLdb
# def cratedb ():
#     return MySQLdb.connect(host="localhost",    # your host, usually localhost
#                         user="root",         # your username
#                         passwd="1",  # your password
#                         db="nfl")        # name of the data base               

# # you must create a Cursor object. It will let
# #  you execute all the queries you need
# def get_cursor(connection):
#     return connection.cursor()

# # Use all the SQL you like
# def execute(Q, cursor):
#     return cursor.execute(Q)


# db.close()