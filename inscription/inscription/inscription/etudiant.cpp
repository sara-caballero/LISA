#include "etudiant.h"

Etudiant::Etudiant(QString nom, QString prenom, int code, QString promotion):Personne(nom, prenom, code){     //constructeur
    this->promotion = promotion;
}


//test pour git