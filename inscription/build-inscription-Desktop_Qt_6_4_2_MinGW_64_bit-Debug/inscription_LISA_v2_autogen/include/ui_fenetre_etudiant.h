/********************************************************************************
** Form generated from reading UI file 'fenetre_etudiant.ui'
**
** Created by: Qt User Interface Compiler version 6.4.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FENETRE_ETUDIANT_H
#define UI_FENETRE_ETUDIANT_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_fenetre_etudiant
{
public:
    QLineEdit *nom;
    QLabel *label_1;
    QLineEdit *prenom;
    QPushButton *bouton;
    QLabel *label_4;
    QLineEdit *code;
    QLabel *label_6;
    QLabel *label_2;
    QLabel *label_3;
    QComboBox *promotion;
    QLabel *resultat;
    QLabel *label_5;
    QLineEdit *code_2;
    QPushButton *bouton_photo;

    void setupUi(QDialog *fenetre_etudiant)
    {
        if (fenetre_etudiant->objectName().isEmpty())
            fenetre_etudiant->setObjectName("fenetre_etudiant");
        fenetre_etudiant->resize(646, 498);
        nom = new QLineEdit(fenetre_etudiant);
        nom->setObjectName("nom");
        nom->setGeometry(QRect(80, 130, 141, 41));
        QFont font;
        font.setPointSize(12);
        nom->setFont(font);
        label_1 = new QLabel(fenetre_etudiant);
        label_1->setObjectName("label_1");
        label_1->setGeometry(QRect(80, 100, 63, 20));
        QFont font1;
        font1.setPointSize(11);
        label_1->setFont(font1);
        prenom = new QLineEdit(fenetre_etudiant);
        prenom->setObjectName("prenom");
        prenom->setGeometry(QRect(350, 130, 141, 41));
        prenom->setFont(font);
        bouton = new QPushButton(fenetre_etudiant);
        bouton->setObjectName("bouton");
        bouton->setGeometry(QRect(460, 420, 131, 41));
        bouton->setFont(font1);
        label_4 = new QLabel(fenetre_etudiant);
        label_4->setObjectName("label_4");
        label_4->setGeometry(QRect(80, 210, 91, 21));
        label_4->setFont(font1);
        code = new QLineEdit(fenetre_etudiant);
        code->setObjectName("code");
        code->setGeometry(QRect(350, 240, 141, 41));
        code->setFont(font);
        label_6 = new QLabel(fenetre_etudiant);
        label_6->setObjectName("label_6");
        label_6->setGeometry(QRect(350, 210, 271, 21));
        label_6->setFont(font1);
        label_2 = new QLabel(fenetre_etudiant);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(350, 100, 63, 20));
        label_2->setFont(font1);
        label_3 = new QLabel(fenetre_etudiant);
        label_3->setObjectName("label_3");
        label_3->setGeometry(QRect(20, 10, 571, 71));
        QFont font2;
        font2.setPointSize(12);
        font2.setBold(true);
        label_3->setFont(font2);
        promotion = new QComboBox(fenetre_etudiant);
        promotion->addItem(QString());
        promotion->addItem(QString());
        promotion->setObjectName("promotion");
        promotion->setGeometry(QRect(80, 240, 141, 41));
        promotion->setFont(font1);
        resultat = new QLabel(fenetre_etudiant);
        resultat->setObjectName("resultat");
        resultat->setGeometry(QRect(350, 360, 201, 51));
        label_5 = new QLabel(fenetre_etudiant);
        label_5->setObjectName("label_5");
        label_5->setGeometry(QRect(80, 320, 91, 21));
        label_5->setFont(font1);
        code_2 = new QLineEdit(fenetre_etudiant);
        code_2->setObjectName("code_2");
        code_2->setGeometry(QRect(80, 390, 141, 41));
        code_2->setFont(font);
        bouton_photo = new QPushButton(fenetre_etudiant);
        bouton_photo->setObjectName("bouton_photo");
        bouton_photo->setGeometry(QRect(80, 350, 141, 41));
        bouton_photo->setFont(font1);

        retranslateUi(fenetre_etudiant);

        QMetaObject::connectSlotsByName(fenetre_etudiant);
    } // setupUi

    void retranslateUi(QDialog *fenetre_etudiant)
    {
        fenetre_etudiant->setWindowTitle(QCoreApplication::translate("fenetre_etudiant", "Inscription \303\240 LISA (\303\251tudiants)", nullptr));
        nom->setText(QString());
        label_1->setText(QCoreApplication::translate("fenetre_etudiant", "Nom", nullptr));
        bouton->setText(QCoreApplication::translate("fenetre_etudiant", "OK", nullptr));
        label_4->setText(QCoreApplication::translate("fenetre_etudiant", "Promotion", nullptr));
        label_6->setText(QCoreApplication::translate("fenetre_etudiant", "Code secret \303\240 4 chiffres ", nullptr));
        label_2->setText(QCoreApplication::translate("fenetre_etudiant", "Pr\303\251nom", nullptr));
        label_3->setText(QCoreApplication::translate("fenetre_etudiant", "Bienvenue \303\240 l'interface d'inscription \303\240 LISA pour \n"
"les \303\251tudiants", nullptr));
        promotion->setItemText(0, QCoreApplication::translate("fenetre_etudiant", "Promotion", nullptr));
        promotion->setItemText(1, QCoreApplication::translate("fenetre_etudiant", "BTS SN 21", nullptr));

        resultat->setText(QString());
        label_5->setText(QCoreApplication::translate("fenetre_etudiant", "Photo", nullptr));
        code_2->setText(QCoreApplication::translate("fenetre_etudiant", "Non prise", nullptr));
        bouton_photo->setText(QCoreApplication::translate("fenetre_etudiant", "Prendre photo", nullptr));
    } // retranslateUi

};

namespace Ui {
    class fenetre_etudiant: public Ui_fenetre_etudiant {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FENETRE_ETUDIANT_H
