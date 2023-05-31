from tkinter import *
from tkinter import messagebox
import MySQLdb
import os
from photo import id_photo
import re
import hashlib

welcome_window = Tk()
welcome_window.title("S'inscrire à LISA")
welcome_window.geometry("600x250")

radio = IntVar()
choix = IntVar()
choix.set(0)


def enter_data(): #Inserer les données de la persone dans la BDD
    prenom = first_name_entry.get()
    nom = last_name_entry.get()
    email = email_entry.get()
    mdp = password_entry.get()
    mdp = hashlib.md5(mdp.encode('utf-8')).hexdigest()
    mdp_c = password_c_entry.get()
    mdp_c = hashlib.md5(mdp_c.encode('utf-8')).hexdigest()
    email_regex = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")

    if prenom and nom and email and mdp and mdp_c:
        if mdp == mdp_c:
            if email_regex.match(email):
               # conn = MySQLdb.connect("172.16.20.129", "dba", "ghjk", "lisa_db")
                conn = MySQLdb.connect("127.0.0.1", "root", "", "lisa_db")
                cursor = conn.cursor()

                # Vérifier si l'email existe déjà dans la table "eleve"
                email_query = "SELECT COUNT(*) FROM eleve WHERE email = %s"
                cursor.execute(email_query, (email,))
                result = cursor.fetchone()

                if result[0] > 0:
                    messagebox.showwarning(title="Erreur", message="Cet utilisateur est déjà inscrit.")

                else:
                    if choix.get()!=0:

                        print("L'utilisateur avec les données suivants a été inscrit : ")
                        print("Prenom: ", prenom, "Nom: ", nom)
                        print("Nom: ", nom)
                        print("E-Mail: ", email)
                        print("Id_photo : ", id_photo)

                        if choix.get() == 1:
                            print("Eleve/Intervenant : Eleve")
                            data_insert_query = '''INSERT INTO eleve (id_promotion, prenom, nom, email, mdp, id_photo) VALUES 
                                (%s, %s, %s, %s, %s, %s)'''
                            data_insert_tuple = (1, prenom, nom, email,
                                                 mdp, id_photo)

                            cursor.execute(data_insert_query, data_insert_tuple)
                            conn.commit()
                            conn.close()

                        if choix.get() == 2:
                            print("Eleve/Intervenant : Intervenant")

                            data_insert_query = '''INSERT INTO intervenant ( prenom, nom, email, mdp, id_photo) VALUES 
                                                    (%s, %s, %s, %s, %s)'''
                            data_insert_tuple = (prenom, nom, email,
                                                 mdp, id_photo)
                            cursor = conn.cursor()
                            cursor.execute(data_insert_query, data_insert_tuple)
                            conn.commit()
                            conn.close()

                    else:
                        messagebox.showerror(title="Error", message="Êtes-vous un(e) étudiant(e) ou un(e) intervenant(e) ?")

            else:
                    messagebox.showerror(title="Error", message="Veuillez mettre un adresse e-mail valide.")

        else:
                messagebox.showerror(title="Error", message="Veuillez entrer le même mot de passe.")

    else:
        messagebox.showerror(title="Error", message="Veuillez remplir tous les champs.")


#Active le bouton submit_button après avoir pris la photo et met à jour le label pour indiquer que la photo a été prise
def open_photo():
    os.system("photo.py")
    submit_button['state'] = NORMAL
    photo_label['text'] = 'Photo OK'


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

email_label = Label(welcome_window, text="Mail")
email_label.grid(row=4, column=0)

email_entry = Entry(welcome_window)
email_entry.grid(row=4, column=1)

password_label = Label(welcome_window, text="Mot de passe")
password_label.grid(row=5, column=0)

password_entry = Entry(welcome_window, show = "*")
password_entry.grid(row=5, column=1)

password_c_label = Label(welcome_window, text="Confirmation de mot de passe")
password_c_label.grid(row=6, column=0)

password_c_entry = Entry(welcome_window, show = "*")
password_c_entry.grid(row=6, column=1)

statut_label = Label(welcome_window, text="Êtes-vous un(e) étudiant(e) ou un(e) intervenant(e) ?")
statut_label.grid(row=7, column=0)

etudiant_choice = Radiobutton(welcome_window, variable=choix, text="Etudiant(e)", value=1)
etudiant_choice.grid(row=7, column=1)

intervenant_choice = Radiobutton(welcome_window, variable=radio, text="Intervenant(e)", value=2)
intervenant_choice.grid(row=7, column=2)

photo_button = Button(welcome_window, text="Prendre photo", command=open_photo)
photo_button.grid(row=8, column=0)

photo_label = Label(welcome_window, text="Veuillez prendre une photo ! ")
photo_label.grid(row=8, column=1)

submit_button = Button(welcome_window, text="OK", command=enter_data, state=DISABLED)
submit_button.grid(row=9, column=0)


welcome_window.mainloop()
