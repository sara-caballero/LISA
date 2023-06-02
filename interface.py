import subprocess
from tkinter import *
from speech_recognition import Recognizer, Microphone
import playsound as ps
import random as rand
from connexion_bdd import connect_to_database
import threading


# Initialisation de la variable globale "text": la reco vocale enregistre en permanence, et tant que le
# mot "Lisa" n'est pas prononcé, il garde la valeur 'Continue'
text = 'Continue'

# Initialisation de la fenêtre
window = Tk()
window.geometry('1280x700')
window.title('LISA')
window['bg'] = '#D2DBFF'
window.attributes("-fullscreen", True)


def open_auth():
    subprocess.call(['python', 'inscription.py'])


def open_conn():
    subprocess.call(['python', 'connexion_reco.py'])



# Fonction qui permet de changer de frame
def switch_canvas(n):
    can.itemconfig(1, state='hidden')
    can.itemconfig(n, state='normal')


# Fonction qui permet de revenir à la frame de base
def default_canvas(n):
    can.itemconfig(n, state='hidden')
    can.itemconfig(1, state='normal')


# Intégration des frames dans la fenêtre
can = Canvas(window, width=1280, height=700, bg="#D2DBFF", highlightthickness=0, relief='ridge')
default_img = PhotoImage(file='img/lisa1.png')
can.create_image(430, 315, image=default_img, state='normal')
can.place(x='10', y='100')

img1 = PhotoImage(file='img/lisa2.png')
can.create_image(430, 315, image=img1, state='hidden')
can.place(x='210', y='200')

img2 = PhotoImage(file='img/lisa3.png')
can.create_image(430, 315, image=img2, state='hidden')
can.place(x='210', y='200')

img3 = PhotoImage(file='img/lisa4.png')
can.create_image(430, 315, image=img3, state='hidden')
can.place(x='210', y='200')

img4 = PhotoImage(file='img/lisa5.png')
can.create_image(430, 315, image=img4, state='hidden')
can.place(x='300', y='300')

img5 = PhotoImage(file='img/lisa6.png')
can.create_image(430, 315, image=img5, state='hidden')
can.place(x='210', y='200')

img6 = PhotoImage(file='img/lisa7.png')
can.create_image(430, 315, image=img6, state='hidden')
can.place(x='210', y='210')

# Création d'un canvas pour la bubble speech
can2 = Canvas(window, width=320, height=260, bg="#D2DBFF", highlightthickness=0, relief='ridge')
bubble_speech = PhotoImage(file='img/bubble.png')
can2.create_image(158, 145, image=bubble_speech, state='normal')
can2.place(x='900', y='400')

txtLisa = Label(window, text="Si vous avez\n besoin de moi,\n dites simplement\n 'Lisa' !", bg="#D2DBFF",
                font=("Arial", 18), width=16)
txtLisa.place(x="940", y="468")

auth_button = Button(window, text="S'authentifier", font=("Arial", 14), height=2, width=12,
                     command=open_conn)
auth_button.place(x="80", y="600")

regis_button = Button(window, text="S'inscrire", font=("Arial", 14), height=2, width=12,
                      command=open_auth)
regis_button.place(x="280", y="600")

# Initialisation des variables contenants les valeurs extraites de la bdd
description = ''
date_debut = ''
date_fin = ''
heure_debut = ''
heure_fin = ''
salle = ''
lieu = ''

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

    if date_fin != '' and salle == '':
        evenement = 'Evènement : ' + description + "\n le " + date_debut + " à " \
                    + heure_debut + " à " + lieu + " jusqu'au " + date_fin + " à " + heure_fin
    elif salle != '' and date_fin == '':
        evenement = 'Evènement : ' + description + "\n en salle " + salle + " le " + date_debut + " à " \
                    + heure_debut + " à " + lieu
    elif salle == '' and date_fin == '':
        evenement = 'Evènement : ' + description + "\n le " + date_debut + " à " \
                    + heure_debut + " à " + lieu
    else:
        evenement = 'Evènement : ' + description + "\n en salle " + salle + " le " + date_debut + " à " \
                    + heure_debut + " à " + lieu + " jusqu'au " + date_fin + " à " + heure_fin

    evLabel = Label(window, text=evenement, bg="#D2DBFF", font=("Arial", 18), width=90)
    evLabel.place(x='0', y='100')

# Initialisation de la boucle infinie
loop = True


# Fonction principale
def lisa_loop():
    global text
    if loop:

        while text == 'Continue':

            recognizer = Recognizer()

            with Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                recognizer.energy_threshold = 1000
                recorded_audio = recognizer.listen(source, timeout=2 ** 63 / 1e9 - 0.1)

            try:
                text = recognizer.recognize_google(
                    recorded_audio,
                    language="fr-FR"
                )

            except:
                text = 'Continue'

            if 'Lisa' not in text:
                text = 'Continue'

            elif 'Lisa' in text:
                text = ''

                num = rand.randint(2, 6)
                switch_canvas(num)
                ask = rand.choice(['1', '2', '3', '4', '5'])
                ask_str = f'C:\\projets_dev\\lisa-all\\lisaspeech\\lisa_ask{ask}.mp3'
                ps.playsound(ask_str)
                default_canvas(num)

                while True:

                    with Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source)
                        recognizer.energy_threshold = 1000
                        recorded_audio = recognizer.listen(source)

                    try:
                        text = recognizer.recognize_google(
                            recorded_audio,
                            language="fr-FR"
                        )

                    except:
                        text = 'error'
                        timeout = rand.choice(['1', '2', '3', '4'])
                        timeout_str = f'C:\\projets_dev\\lisa-all\\lisaspeech\\lisa_timeout{timeout}.mp3'
                        ps.playsound(timeout_str)
                        text = 'continue'
                        break

                    if text != 'error':
                        if "retard" in text:
                            num = rand.randint(2, 6)
                            switch_canvas(num)
                            retard = rand.choice(['1', '2', '3'])
                            retard_str = f'C:\\projets_dev\\lisa-all\\lisaspeech\\lisa_retard{retard}.mp3'
                            ps.playsound(retard_str)
                            text = 'continue'
                            default_canvas(num)
                            break
                        elif "inscrire" in text:
                            num = rand.randint(2, 6)
                            switch_canvas(num)

                            # inviter à entrer les informations d'insrcription
                            ps.playsound('C:\\projets_dev\\lisa-all\\lisaspeech\\lisa_signin.mp3')

                            # expliquer que l'on va prendre une photo
                            ps.playsound('C:\\projets_dev\\lisa-all\\lisaspeech\\lisa_photo.mp3')

                            # photo prise
                            ps.playsound('C:\\projets_dev\\lisa-all\\lisaspeech\\lisa_clic1.mp3')
                            ps.playsound('C:\\projets_dev\\lisa-all\\lisaspeech\\lisa_clic2.mp3')

                            text = 'continue'
                            default_canvas(num)
                            break
                        elif "bonjour" in text:
                            switch_canvas(2)
                            greet = rand.choice(['1', '2', '3', '4'])
                            greet_str = f'C:\\projets_dev\\lisa-all\\lisaspeech\\lisa_greetings{greet}.mp3'
                            ps.playsound(greet_str)
                            default_canvas(2)
                        elif "salut" in text:
                            switch_canvas(2)
                            greet = rand.choice(['1', '2', '3', '4'])
                            greet_str = f'C:\\projets_dev\\lisa-all\\lisaspeech\\lisa_greetings{greet}.mp3'
                            ps.playsound(greet_str)
                            default_canvas(2)
                        else:
                            switch_canvas(7)
                            error = rand.choice(['1', '2', '3'])
                            error_str = f'C:\\projets_dev\\lisa-all\\lisaspeech\\lisa_error{error}.mp3'
                            ps.playsound(error_str)
                            default_canvas(7)
