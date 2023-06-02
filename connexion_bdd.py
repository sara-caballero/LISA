import mysql.connector


def connect_to_database():
    conn = mysql.connector.connect(
        host="172.16.20.129",
        user="dba",
        password="ghjk",
        database="lisa_db"
    )
    return conn
