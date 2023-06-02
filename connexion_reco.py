from tkinter import *
import os
import easy_facial_recognition
from connexion_bdd import connect_to_database
from tkinter import messagebox


welcome_window = Tk()
welcome_window.title("Se connecter à LISA")
welcome_window.geometry("600x220")
welcome_window.configure(bg="#F5F5F5")

nom = None
prenom = None

def open_connexion_mail(): # Fonction pour ouvrir la fenêtre de connexion par e-mail
    os.system("connexion_mail.py")
    welcome_window.destroy()


def open_reco_faciale(): # Fonction pour ouvrir la reconnaissance faciale
    global nom, prenom
    reponse = "no" # Initialisation avec une valeur par défaut
    nom_reco = easy_facial_recognition.my_reco()
    print( f"id_photo reconnu :  {nom_reco}\n")
    if nom_reco == "Unknown":
        messagebox.showerror("Erreur", "Visage non reconnu. Veuillez vous inscrire à LISA ou vous identifier avec votre e-mail.")
        exit(1)
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM eleve WHERE id_photo=%s", (nom_reco,))
    row = cur.fetchone()

    if row is None:
        cur.execute("SELECT * FROM intervenant WHERE id_photo=%s", (nom_reco,))
        row = cur.fetchone()
        if row is None:
            messagebox.showerror("Erreur", "Visage non reconnu. Veuillez vous inscrire à LISA ou vous identifier avec votre e-mail.")
        else:
            nom = row[1]
            prenom = row[2]
           # reponse = messagebox.askquestion("Succès", "Bienvenue, êtes-vous {} {} ?".format(prenom, nom))
    else:
        nom = row[1]
        prenom = row[2]

    if nom is not None and prenom is not None:
        reponse = messagebox.askquestion("Succès", "Bienvenue, êtes-vous {} {} ?".format(prenom, nom))
        # Stocker les valeurs de nom et prenom dans le fichier texte
        with open("donnees.txt", "w") as file:
            file.write(nom + "\n")
            file.write(prenom + "\n")

    if reponse == 'yes':
        messagebox.showinfo("Confirmation", "Super, bienvenue {} !".format(prenom))
        welcome_window.destroy()
    else:
        messagebox.showinfo("Confirmation", "Veuillez contacter l'administrateur de LISA pour résoudre ce problème. En attendant, veuillez vous connecter avec la méthode classique en utilisant votre email et votre mot de passe.")

    conn.close()


# Titre d'accueil
welcome_label = Label(welcome_window, text="Connectez-vous à LISA", font=("Arial", 16), bg="#F5F5F5")
welcome_label.pack(pady=10)

# Sous-titre expliquant les choix de connexion
subtitle_label = Label(welcome_window, text="Choisissez une méthode de connexion :", font=("Arial", 12), bg="#F5F5F5")
subtitle_label.pack()

# Bouton pour la connexion par méthode classique
login_button = Button(welcome_window, text="Méthode classique", font=("Arial", 12), bg="#4CAF50", fg="white", command=open_connexion_mail)
login_button.pack(pady=10)

# Bouton pour la connexion par reconnaissance faciale
facial_login_button = Button(welcome_window, text="Reconnaissance faciale", font=("Arial", 12), bg="#1976D2", fg="white", command=open_reco_faciale)
facial_login_button.pack(pady=5)

# LISA
subtitle_label = Label(welcome_window, text="Local IRUP/ISTP Assistant", font=("Arial", 10), bg="#F5F5F5", fg="#808080")
subtitle_label.pack(side=BOTTOM, pady=10)

welcome_window.mainloop()
