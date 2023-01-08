import mysql.connector


def create_connect():
    return mysql.connector.connect(user='root', password= 'Aum.p9wx',
                              host='localhost',
                              database= 'nflbowl',
                              auth_plugin='mysql_native_password')

def create_cursor(connection):
    return connection.cursor()

def execute_query(cursor, query):
    return cursor.execute(query)

def close_connection(cursor, connection):
    cursor.close()
    connection.close()

    
def mysql_ex(query):
    connect =  create_connect()
    cursor = create_cursor(connect)
    R = execute_query(cursor,query)
    print(R)
    print(f'type of R : {R}')
    return R
















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