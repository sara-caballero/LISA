#include "mainwindow.h"
#include "./ui_mainwindow.h"

#include "fenetre_etudiant.h"
#include "fenetre_intervenant.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_bouton_clicked()  //Ouverture de la 2ème fenetre en fonction du statut de la personne (etudiant ou intervenant)
{
    if (ui->bouton_etudiant->isChecked()){
        this->close();
        fenetre_etudiant fenetre;
        fenetre.exec();
    }
    else if (ui->bouton_intervenant->isChecked()){
        this->close();
        fenetre_intervenant fenetre;
        fenetre.exec();
    }
}

