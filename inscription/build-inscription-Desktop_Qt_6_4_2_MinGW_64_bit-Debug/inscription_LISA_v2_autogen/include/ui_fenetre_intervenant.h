/********************************************************************************
** Form generated from reading UI file 'fenetre_intervenant.ui'
**
** Created by: Qt User Interface Compiler version 6.4.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FENETRE_INTERVENANT_H
#define UI_FENETRE_INTERVENANT_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_fenetre_intervenant
{
public:
    QComboBox *module;
    QLineEdit *code;
    QPushButton *bouton;
    QLabel *label_2;
    QLabel *label_4;
    QLabel *label_3;
    QLineEdit *prenom;
    QLabel *label_1;
    QLabel *label_6;
    QLineEdit *nom;
    QLabel *resultat;

    void setupUi(QDialog *fenetre_intervenant)
    {
        if (fenetre_intervenant->objectName().isEmpty())
            fenetre_intervenant->setObjectName("fenetre_intervenant");
        fenetre_intervenant->resize(606, 542);
        module = new QComboBox(fenetre_intervenant);
        module->addItem(QString());
        module->addItem(QString());
        module->addItem(QString());
        module->addItem(QString());
        module->setObjectName("module");
        module->setGeometry(QRect(60, 280, 141, 41));
        QFont font;
        font.setPointSize(10);
        module->setFont(font);
        code = new QLineEdit(fenetre_intervenant);
        code->setObjectName("code");
        code->setGeometry(QRect(330, 280, 141, 41));
        QFont font1;
        font1.setPointSize(12);
        code->setFont(font1);
        bouton = new QPushButton(fenetre_intervenant);
        bouton->setObjectName("bouton");
        bouton->setGeometry(QRect(220, 420, 131, 41));
        QFont font2;
        font2.setPointSize(11);
        bouton->setFont(font2);
        label_2 = new QLabel(fenetre_intervenant);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(330, 140, 63, 20));
        label_2->setFont(font2);
        label_4 = new QLabel(fenetre_intervenant);
        label_4->setObjectName("label_4");
        label_4->setGeometry(QRect(60, 250, 91, 21));
        label_4->setFont(font2);
        label_3 = new QLabel(fenetre_intervenant);
        label_3->setObjectName("label_3");
        label_3->setGeometry(QRect(20, 40, 511, 51));
        QFont font3;
        font3.setPointSize(12);
        font3.setBold(true);
        label_3->setFont(font3);
        prenom = new QLineEdit(fenetre_intervenant);
        prenom->setObjectName("prenom");
        prenom->setGeometry(QRect(330, 170, 141, 41));
        prenom->setFont(font1);
        label_1 = new QLabel(fenetre_intervenant);
        label_1->setObjectName("label_1");
        label_1->setGeometry(QRect(60, 140, 63, 20));
        label_1->setFont(font2);
        label_6 = new QLabel(fenetre_intervenant);
        label_6->setObjectName("label_6");
        label_6->setGeometry(QRect(330, 250, 201, 21));
        label_6->setFont(font2);
        nom = new QLineEdit(fenetre_intervenant);
        nom->setObjectName("nom");
        nom->setGeometry(QRect(60, 170, 141, 41));
        nom->setFont(font1);
        resultat = new QLabel(fenetre_intervenant);
        resultat->setObjectName("resultat");
        resultat->setGeometry(QRect(390, 350, 201, 91));

        retranslateUi(fenetre_intervenant);

        QMetaObject::connectSlotsByName(fenetre_intervenant);
    } // setupUi

    void retranslateUi(QDialog *fenetre_intervenant)
    {
        fenetre_intervenant->setWindowTitle(QCoreApplication::translate("fenetre_intervenant", "Inscription \303\240 LISA (Intervenants)", nullptr));
        module->setItemText(0, QCoreApplication::translate("fenetre_intervenant", "Informatique", nullptr));
        module->setItemText(1, QCoreApplication::translate("fenetre_intervenant", "Anglais", nullptr));
        module->setItemText(2, QCoreApplication::translate("fenetre_intervenant", "Culture g\303\251n\303\251rale", nullptr));
        module->setItemText(3, QCoreApplication::translate("fenetre_intervenant", "Physique", nullptr));

        bouton->setText(QCoreApplication::translate("fenetre_intervenant", "OK", nullptr));
        label_2->setText(QCoreApplication::translate("fenetre_intervenant", "Pr\303\251nom", nullptr));
        label_4->setText(QCoreApplication::translate("fenetre_intervenant", "Module", nullptr));
        label_3->setText(QCoreApplication::translate("fenetre_intervenant", "Bienvenue \303\240 l'interface d'inscription \303\240 LISA pour \n"
"les intervenants", nullptr));
        label_1->setText(QCoreApplication::translate("fenetre_intervenant", "Nom", nullptr));
        label_6->setText(QCoreApplication::translate("fenetre_intervenant", "Code secret \303\240 4 chiffres ", nullptr));
        nom->setText(QString());
        resultat->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class fenetre_intervenant: public Ui_fenetre_intervenant {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FENETRE_INTERVENANT_H
