#ifndef INTERVENANT_H
#define INTERVENANT_H

#include <QMainWindow>
#include <QObject>
#include <QWidget>
#include "personne.h"

class Intervenant : public Personne   //Intervenant hérite de Personne
{
public:
    Intervenant(QString nom, QString prenom, int code, QString module); //Constructeur
    QString getModule() { return module; }; //Accesseur
    void setModule(QString  &value) { module = value; }; //Mutateur

private:
    QString module;
};

#endif // INTERVENANT_H
