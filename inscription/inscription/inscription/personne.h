#ifndef PERSONNE_H
#define PERSONNE_H

#include <QMainWindow>
#include <QObject>
#include <QWidget>

class Personne{
public:
    Personne(QString nom, QString prenom, int code);   //Constructeur

    //Accesseurs
    QString getNom() {return nom;}
    QString getPrenom() {return prenom;}
    int getCode() {return code;}

    //Mutateurs
    void setNom(QString &value) {nom = value;};
    void setPrenom(QString &value) {prenom = value;};
    void setCode(int &value){code = value;};

protected:  //les attributs suivants seront accesibles uniquement depuis la classe elle-même et depuis les clases qui en héritent
    QString nom;
    QString prenom;
    int code;
};

#endif // PERSONNE_H
