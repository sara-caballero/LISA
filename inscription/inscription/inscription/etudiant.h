#ifndef ETUDIANT_H
#define ETUDIANT_H

#include <QMainWindow>
#include <QObject>
#include <QWidget>

#include "personne.h"

class Etudiant : public Personne { //Etudiants hérite de Personne (=Etudiants est une classe dérivée ou une classe enfant)
public:
    Etudiant(QString nom, QString prenom, int code, QString promotion);    //Constructeur
    QString getPromotion() { return promotion; } ; //Accesseur
    void setPromotion(QString &value) { promotion = value; }; //Mutateur

private:
    QString promotion;

};

#endif // ETUDIANT_H
