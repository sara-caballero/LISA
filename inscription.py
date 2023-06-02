from tkinter import *
from tkinter import messagebox
import os
import interface
from photo import id_photo
import re
import hashlib
from connexion_bdd import connect_to_database


welcome_window = Toplevel(interface.window)
welcome_window.title("S'inscrire à LISA")
welcome_window.geometry("500x480")

# Couleurs
primary_color = "#28536B"  # Couleur principale
secondary_color = "#FFFFFF"  # Couleur secondaire
accent_color = "#FF8A5B"  # Couleur d'accentuation

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

                conn = connect_to_database()

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
                        print("Prenom: ", prenom)
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
                            messagebox.showinfo(title="Succès", message="Félicitations ! Vous avez été inscrit avec succès. Vous pouvez maintenant vous connecter.")
                            welcome_window.destroy()

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
                            messagebox.showinfo(title="Succès", message="Felicitations ! Vous avez été inscrit avec succès. Vous pouvez maintenant vous connecter.")
                            welcome_window.destroy()


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
    photo_label['text'] = 'Photo enregistrée avec succès'


# Configurer les styles des widgets
welcome_window.configure(bg=secondary_color)

welcome_label = Label(welcome_window, text="Inscrivez-vous à LISA", font=("Arial", 16), bg=secondary_color)

first_name_label = Label(welcome_window, text="Prénom:", font=("Arial", 12), bg=secondary_color)
first_name_entry = Entry(welcome_window, font=("Arial", 12))

last_name_label = Label(welcome_window, text="Nom:", font=("Arial", 12), bg=secondary_color)
last_name_entry = Entry(welcome_window, font=("Arial", 12))

email_label = Label(welcome_window, text="Mail:", font=("Arial", 12), bg=secondary_color)
email_entry = Entry(welcome_window, font=("Arial", 12))

password_label = Label(welcome_window, text="Mot de passe:", font=("Arial", 12), bg=secondary_color)
password_entry = Entry(welcome_window, show="*", font=("Arial", 12))

password_c_label = Label(welcome_window, text="Confirmation de mot de passe:", font=("Arial", 12), bg=secondary_color)
password_c_entry = Entry(welcome_window, show="*", font=("Arial", 12))

statut_label = Label(welcome_window, text="Êtes-vous un(e) étudiant(e) ou un(e) intervenant(e) ?", font=("Arial", 12), bg=secondary_color)
etudiant_choice = Radiobutton(welcome_window, variable=choix, text="Etudiant(e)", value=1, font=("Arial", 12), bg=secondary_color)
intervenant_choice = Radiobutton(welcome_window, variable=choix, text="Intervenant(e)", value=2, font=("Arial", 12), bg=secondary_color)

photo_button = Button(welcome_window, text="Prendre photo", command=open_photo, font=("Arial", 12), bg=primary_color, fg=secondary_color)
photo_label = Label(welcome_window, text="Veuillez prendre une photo pour votre inscription.", font=("Arial", 12), bg=secondary_color, fg=primary_color)

submit_button = Button(welcome_window, text="S'inscrire", command=enter_data, state=DISABLED, font=("Arial", 14), bg=accent_color, fg=secondary_color)

# Positionner les widgets dans la grille
welcome_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
first_name_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)
first_name_entry.grid(row=1, column=1, padx=10, pady=5)
last_name_label.grid(row=2, column=0, sticky="e", padx=10, pady=5)
last_name_entry.grid(row=2, column=1, padx=10, pady=5)
email_label.grid(row=3, column=0, sticky="e", padx=10, pady=5)
email_entry.grid(row=3, column=1, padx=10, pady=5)
password_label.grid(row=4, column=0, sticky="e", padx=10, pady=5)
password_entry.grid(row=4, column=1, padx=10, pady=5)
password_c_label.grid(row=5, column=0, sticky="e", padx=10, pady=5)
password_c_entry.grid(row=5, column=1, padx=10, pady=5)
statut_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
etudiant_choice.grid(row=7, column=0, padx=10, pady=5)
intervenant_choice.grid(row=7, column=1, padx=10, pady=5)
photo_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5)
photo_label.grid(row=9, column=0, columnspan=2, padx=10, pady=5)
submit_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

# Configurer les couleurs de fond
welcome_window.configure(bg=secondary_color)
submit_button.configure(bg=accent_color)
photo_button.configure(bg=primary_color)
photo_label.configure(bg=secondary_color)

# LISA
subtitle_label = Label(welcome_window, text="Local IRUP/ISTP Assistant", font=("Arial", 10), bg="#F5F5F5", fg="#808080")
subtitle_label.grid(row=11, column=0, columnspan=2, pady=10)


welcome_window.mainloop()