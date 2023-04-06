from tkinter import *
from tkinter import messagebox
import MySQLdb
import os
import photo
from photo import id_photo
import subprocess
import time

welcome_window = Tk()
welcome_window.title("S'inscrire à LISA")
welcome_window.geometry("600x250")

radio = IntVar()

print("id_photo = ", id_photo)




def enter_data(): #Inserer les données de la persone dans la BDD
    prenom = first_name_entry.get()
    nom = last_name_entry.get()
    mail = mail_entry.get()
    mdp = password_entry.get()
    mdp_c = password_c_entry.get()

    if prenom and nom and mail and mdp and mdp_c:

        print("Prenom: ", prenom, "Nom: ", nom)
        print("Mail: ", mail)
        print("Id_photo : ", id_photo)
      #  print(id_photo)

        conn = MySQLdb.connect("172.16.5.101", "dba", "ghjk", "lisa_db")

        # Insert Data
        data_insert_query = '''INSERT INTO eleve (id_groupe, prenom, nom, mail, mdp, id_photo) VALUES 
            (%s, %s, %s, %s, %s, %s)'''
        data_insert_tuple = (1, prenom, nom, mail,
                             mdp, id_photo)
        cursor = conn.cursor()
        cursor.execute(data_insert_query, data_insert_tuple)
        conn.commit()
        conn.close()

    else:
        messagebox.showwarning(title="Error", message="Veuillez remplir tous les champs")

def open_photo():
    os.system("photo.py")
    time.sleep(5)
    print(bool_photo())

def switchSubmitButtonState():
    if (submit_button['state'] == NORMAL):
        submit_button['state'] = DISABLED
    else:
        submit_button['state'] = NORMAL


def bool_photo():
    l = os.listdir('c:/lisa/rec_faciale/easy_facial_recognition-master/known_faces') # Retourne un tableau avec les noms de fichiers (String) du dossier known_faces au moment de l'execution sans l'extension
    liste = [x.split('.')[0] for x in l]
    test_label['text'] = liste
    bool = id_photo in liste
    if (bool == True):
        photo_label['text'] = 'ahah'


# declaration et positionnement des widgets

welcome_label = Label(welcome_window, text="Inscrivez-vous à LISA")
welcome_label.grid(row=0, column=0, rowspan=2)

first_name_label = Label(welcome_window, text="Prénom")
first_name_label.grid(row=2, column=0)

first_name_entry = Entry(welcome_window)
first_name_entry.grid(row=2, column=1)

last_name_label = Label(welcome_window, text="Nom")
last_name_label.grid(row=3, column=0)

last_name_entry = Entry(welcome_window)
last_name_entry.grid(row=3, column=1)

mail_label = Label(welcome_window, text="Mail")
mail_label.grid(row=4, column=0)

mail_entry = Entry(welcome_window)
mail_entry.grid(row=4, column=1)

password_label = Label(welcome_window, text="Mot de passe")
password_label.grid(row=5, column=0)

password_entry = Entry(welcome_window)
password_entry.grid(row=5, column=1)

password_c_label = Label(welcome_window, text="Confirmation de mot de passe")
password_c_label.grid(row=6, column=0)

password_c_entry = Entry(welcome_window)
password_c_entry.grid(row=6, column=1)

statut_label = Label(welcome_window, text="Êtes-vous un(e) étudiant(e) ou un(e) intervenant(e) ?")
statut_label.grid(row=7, column=0)

etudiant_choice = Radiobutton(welcome_window, variable=radio, text="Etudiant(e)", value=1)
etudiant_choice.grid(row=7, column=1)
intervenant_choice = Radiobutton(welcome_window, variable=radio, text="Intervenant(e)", value=2)
intervenant_choice.grid(row=7, column=2)

photo_button = Button(welcome_window, text="Prendre photo", command=lambda: [open_photo(), switchSubmitButtonState(), bool_photo()])
photo_button.grid(row=8, column=0)

photo_label = Label(welcome_window, text="Veuillez prendre une photo ! ")
photo_label.grid(row=8, column=1)

submit_button = Button(welcome_window, text="OK", command=enter_data, state=DISABLED)
submit_button.grid(row=9, column=0)

test_label = Label(welcome_window, text="Test")
test_label.grid(row=10, column=1)


welcome_window.mainloop()
