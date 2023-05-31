from tkinter import *
from tkinter import messagebox
import MySQLdb
import hashlib

welcome_window = Tk()
welcome_window.title("Se connecter à LISA")
welcome_window.geometry("300x100")

def login():
    global nom, prenom

    email = email_entry.get()
    mdp = hashlib.md5(password_entry.get().encode('utf-8')).hexdigest()

    conn = MySQLdb.connect("172.16.20.125", "dba", "ghjk", "lisa_db")
    cur = conn.cursor()
    cur.execute("select * from eleve where email=%s and mdp=%s", (email, mdp))
<<<<<<< HEAD
=======

>>>>>>> origin/Authentification
    row = cur.fetchone()

    if row is None:
        messagebox.showerror("Error", "Mot de passe et/ou mail invalides")
    else:
        messagebox.showinfo("Success", "Bienvenue")
        nom = row[3]
        prenom = row[4]
        print(nom)
        print(prenom)

        # Stocker les valeurs de nom et prenom dans le fichier texte
        with open("donnees.txt", "w") as file:
            file.write(nom + "\n")
            file.write(prenom + "\n")

    conn.close()

welcome_label = Label(welcome_window, text="Connectez-vous à LISA")
welcome_label.grid(row=0, column=0, rowspan=2)

email_label = Label(welcome_window, text="Mail")
email_label.grid(row=4, column=0)

email_entry = Entry(welcome_window)
email_entry.grid(row=4, column=1)

password_label = Label(welcome_window, text="Mot de passe")
password_label.grid(row=5, column=0)

password_entry = Entry(welcome_window, show="*")
password_entry.grid(row=5, column=1)

submit_button = Button(welcome_window, text="OK", command=login)
submit_button.grid(row=8, column=0)

welcome_window.mainloop()
