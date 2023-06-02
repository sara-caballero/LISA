import mysql.connector

def connect_to_database():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="lisa_db"
    )
    return conn

#"172.16.20.129", "dba", "ghjk", "lisa_db"
#host = "127.0.0.1",
#user = "root",
#password = "",
#database = "lisa_db"