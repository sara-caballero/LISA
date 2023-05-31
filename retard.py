from fpdf import FPDF
from datetime import datetime
import subprocess
nom = None
prenom = None


def create_pdf():
    pdf = FPDF()
    pdf.add_page()

    # Logo à gauche
    pdf.image("img/logo-istp.png", x=10, y=10, w=30)

    # Logo à droite
    pdf.image("img/logo-irup.png", x=170, y=10, w=30)

    # Titre "Fiche de retard"
    pdf.set_font("Arial", "B", size=16)
    pdf.cell(0, 20, txt="Fiche de retard", ln=True, align="C")

    # Sous-titre "DOCUMENT A PRESENTER A L INTERVENANT..."
    pdf.set_font("Arial", "U", size=12)
    pdf.cell(0, 10, txt="DOCUMENT A PRESENTER A L'INTERVENANT", ln=True, align="C")
    pdf.cell(0, 10, txt="ET A REMETTRE EN FIN DE COURS AU SECRETARIAT", ln=True, align="C")

    pdf.ln(20)  # Grand espace

    # Informations de l'élève
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, txt="Nom: {}".format(nom), ln=True)
    pdf.cell(0, 10, txt="Prénom: {}".format(prenom), ln=True)
    pdf.cell(0, 10, txt="Filière/Promo: BTS SN", ln=True)

    # Date/Heure du retard
    now = datetime.now()
    date_heure_retard = now.strftime("%d/%m/%Y %H:%M:%S")
    pdf.cell(0, 10, txt="Date/Heure du retard: {}".format(date_heure_retard), ln=True)

    pdf.ln(20)  # Grand espace

    # Signatures
    pdf.set_font("Arial", "B", size=12)
    pdf.cell(0, 10, txt="Signature de l'élève", ln=True)
    pdf.cell(0, 10, txt="", ln=True)  # Grand carreau pour la signature de l'élève

    pdf.ln(20)  # Grand espace

    pdf.cell(0, 10, txt="Signature de l'intervenant", ln=True)
    pdf.cell(0, 10, txt="", ln=True)  # Grand carreau pour la signature de l'intervenant

    pdf.output(f"temp/fiche_retard_{str(nom)}_{str(prenom)}.pdf")
    return "Fichier PDF créé avec succès."

with open("temp/donnees.txt", "r") as file:
    data = file.read().splitlines()
    if len(data) == 2:
        nom = data[0]
        prenom = data[1]


resultat = create_pdf()
print(resultat)

# Chemin complet vers le fichier PDF à imprimer
pdf_file = "fichier.pdf"

# Commande d'impression spécifique à Adobe Acrobat Reader sur Windows
command = 'START /B /WAIT "" "C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe" /t "{}"'.format(pdf_file)

# Lancer la commande d'impression
#subprocess.run(command, shell=True)
