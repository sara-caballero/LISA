from tkinter import *
from tkinter import messagebox
import hashlib
from connexion_bdd import connect_to_database

# Création de la fenêtre principale
welcome_window = Tk()
welcome_window.title("Se connecter à LISA")
welcome_window.geometry("500x300")
welcome_window.configure(bg="#F5F5F5")

def login():
    global nom, prenom

    email = email_entry.get()
    mdp = hashlib.md5(password_entry.get().encode('utf-8')).hexdigest()

    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM eleve WHERE email=%s AND mdp=%s", (email, mdp))

    row = cur.fetchone()

    if row is None:
        messagebox.showerror("Erreur", "Mot de passe et/ou e-mail invalides")
    else:
        messagebox.showinfo("Succès", "Bienvenue, vous êtes connecté avec succès !")
        welcome_window.destroy()
        nom = row[1]
        prenom = row[2]

        # Stocker les valeurs de nom et prenom dans le fichier texte
        with open("temp/donnees*.txt", "w") as file:
            file.write(nom + "\n")
            file.write(prenom + "\n")

    conn.close()

# Libellé d'accueil
welcome_label = Label(welcome_window, text="Connectez-vous à LISA", font=("Arial", 16), bg="#F5F5F5")
welcome_label.pack(pady=10)

# Champ d'e-mail
email_label = Label(welcome_window, text="E-mail", font=("Arial", 12), bg="#F5F5F5")
email_label.pack()
email_entry = Entry(welcome_window, font=("Arial", 12))
email_entry.pack()

# Champ de mot de passe
password_label = Label(welcome_window, text="Mot de passe", font=("Arial", 12), bg="#F5F5F5")
password_label.pack()
password_entry = Entry(welcome_window, show="*", font=("Arial", 12))
password_entry.pack()

# Bouton de soumission
submit_button = Button(welcome_window, text="Se connecter", font=("Arial", 12), bg="#FFD700", fg="black", highlightthickness=2, highlightcolor="black", command=login)
submit_button.pack(pady=10)

# LISA
subtitle_label = Label(welcome_window, text="Local IRUP/ISTP Assistant", font=("Arial", 10), bg="#F5F5F5", fg="#808080")
subtitle_label.pack(side=BOTTOM, pady=10)


welcome_window.mainloop()