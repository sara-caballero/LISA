#include "fenetre_etudiant.h"
#include "ui_fenetre_etudiant.h"

#include "etudiant.h"


fenetre_etudiant::fenetre_etudiant(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::fenetre_etudiant)
{
    ui->setupUi(this);
}

fenetre_etudiant::~fenetre_etudiant()
{
    delete ui;
}


QString nom_etu, prenom_etu, promotion;
int code_int_etu;

void fenetre_etudiant::on_nom_textChanged(const QString &arg1)
{
    nom_etu=ui->nom->text(); //Implémentation du Line Edit nom
}


void fenetre_etudiant::on_prenom_textChanged(const QString &arg1)
{
     prenom_etu=ui->prenom->text(); //Implémentation du Line Edit prenom
}


void fenetre_etudiant::on_code_textChanged(const QString &arg1)
{
     QString code=ui->code->text(); //Implémentation du Line Edit code
     code_int_etu=code.toInt();
}


void fenetre_etudiant::on_promotion_currentTextChanged(const QString &arg1)
{
     promotion=ui->promotion->currentText(); //Implémentation de la Combo Box promotion
}

Etudiant* e1 = new Etudiant(nom_etu, prenom_etu, code_int_etu, promotion);   //Instanciation de la classe Etudiant

void fenetre_etudiant::on_bouton_clicked()
{
    ui->resultat->setText(nom_etu + " " + prenom_etu + " " + promotion); //tout ok
}

