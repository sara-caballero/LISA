import mysql.connector
import hashlib


pdo = mysql.connector.connect(host="172.16.5.106", user="dba", passwd="ghjk", database="lisa_db")

if pdo:
    print("Connected")
else:
    print("Not connected")

mycursor = pdo.cursor()
mdp = "Tplombgrosbg"
result = hashlib.md5(mdp.encode())

sql = "INSERT INTO eleve (id_groupe, nom, prenom, mail, mdp) VALUES (%s, %s, %s, %s, %s)"
val = (1, "Plomb", "Titouan", "btss21tplomb@eleve-irup.com", mdp)
mycursor.execute(sql, val)

pdo.commit()

print(mycursor.rowcount, "record inserted.")