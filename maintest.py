from connexion_bdd import connect_to_database
from pprint import pprint

# Initialisation des variables contenants les valeurs extraites de la bdd
titre = None
description = None
date_debut = None
date_fin = None
heure_debut = None
heure_fin = None
salle = None
lieu = None

# Extraction de l'évènement à venir si existant
conn = connect_to_database()
cursor = conn.cursor()
cursor.execute("SELECT * FROM evenement WHERE date_debut >= CURDATE() ORDER BY date_debut ASC LIMIT 1")
result = cursor.fetchall()
if cursor.rowcount == 1:
    for row in result:
        titre = row[0]
        description = row[1]
        date_debut = str(row[2])
        date_fin = str(row[3])
        heure_debut = str(row[4])
        heure_fin = str(row[5])
        salle = row[6]
        lieu = row[7]

pprint(globals())

