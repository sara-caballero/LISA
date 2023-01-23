#include "intervenant.h"

Intervenant::Intervenant(QString nom, QString prenom, int code, QString module):Personne(nom, prenom, code){     //constructeur
    this->module = module;
}
