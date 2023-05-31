from tkinter import *
import os
import easy_facial_recognition
import MySQLdb
from tkinter import messagebox


welcome_window = Tk()
welcome_window.title("Se connecter à LISA")
welcome_window.geometry("400x100")

nom = None
prenom = None

def open_connexion_mail():
    os.system("connexion_mail.py")


def open_reco_faciale():
    nom_reco = easy_facial_recognition.my_reco()
    print( f"J ai reconnu {nom_reco}\n")
    if nom_reco == "Unknown":
        messagebox.showerror("Error", "Visage pas reconnu. Veuillez vous inscrire à LISA ou vous identifier avec votre e-mail.")
        exit(1)
    print(type(nom_reco))
    conn = MySQLdb.connect("172.16.20.125", "dba", "ghjk", "lisa_db")
    cur = conn.cursor()
    cur.execute("select * from eleve where id_photo=%s", (nom_reco))
    row = cur.fetchone()

    if row is None:
        cur.execute("select * from intervenant where id_photo=%s", (nom_reco))
        row = cur.fetchone
        if row is None:
            messagebox.showerror("Error", "Visage pas reconnu. Veuillez vous inscrire à LISA ou vous identifier avec votre e-mail.")
        else:
            nom = row[3]
            prenom = row[4]
            messagebox.askquestion("Success", "Bienvenue, êtes-vous {} {} ?".format(prenom, nom))

            # Stocker les valeurs de nom et prenom dans le fichier texte
            with open("donnees.txt", "w") as file:
                file.write(nom + "\n")
                file.write(prenom + "\n")
    else:
        nom = row[3]
        prenom = row[4]
        messagebox.askquestion("Success", "Bienvenue, êtes-vous {} {} ?".format(prenom, nom))
        # Stocker les valeurs de nom et prenom dans le fichier texte
        with open("donnees.txt", "w") as file:
            file.write(nom + "\n")
            file.write(prenom + "\n")

    conn.close()


statut_label = Label(welcome_window, text="Comment voulez-vous vous connecter à LISA?")
statut_label.grid(row=2, column=0)

reco_button = Button(welcome_window, text="Reconnaissance faciale", command=open_reco_faciale)
reco_button.grid(row=3, column=0)
mail_button = Button(welcome_window, text="Manière classique", command=open_connexion_mail)
mail_button.grid(row=3, column=3)

welcome_window.mainloop()
