#include "fenetre_intervenant.h"
#include "ui_fenetre_intervenant.h"

#include "intervenant.h"

fenetre_intervenant::fenetre_intervenant(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::fenetre_intervenant)
{
    ui->setupUi(this);
}

fenetre_intervenant::~fenetre_intervenant()
{
    delete ui;
}

QString nom_interv, prenom_interv, module;
int code_int_interv;

void fenetre_intervenant::on_nom_textChanged(const QString &arg1)
{
    nom_interv=ui->nom->text(); //Implémentation du Line Edit nom
}


void fenetre_intervenant::on_prenom_textChanged(const QString &arg1)
{
     prenom_interv=ui->prenom->text(); //Implémentation du Line Edit prenom
}


void fenetre_intervenant::on_code_textChanged(const QString &arg1)
{
     QString code=ui->code->text(); //Implémentation du Line Edit code
     code_int_interv=code.toInt();
}


void fenetre_intervenant::on_module_currentTextChanged(const QString &arg1)
{
     module=ui->module->currentText(); //Implémentation de la Combo Box promotion
}

Intervenant* i1 = new Intervenant(nom_interv, prenom_interv, code_int_interv, module);   //Instanciation de la classe Intervenant

void fenetre_intervenant::on_bouton_clicked()
{
    ui->resultat->setText(nom_interv + " " + prenom_interv + " " + module); //tout ok
}
