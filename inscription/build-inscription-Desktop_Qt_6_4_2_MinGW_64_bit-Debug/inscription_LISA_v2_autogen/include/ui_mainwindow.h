/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.4.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QLabel *label;
    QLabel *label_1;
    QRadioButton *bouton_etudiant;
    QRadioButton *bouton_intervenant;
    QPushButton *bouton;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(538, 476);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        label = new QLabel(centralwidget);
        label->setObjectName("label");
        label->setGeometry(QRect(50, 40, 501, 31));
        QFont font;
        font.setPointSize(12);
        font.setBold(true);
        label->setFont(font);
        label_1 = new QLabel(centralwidget);
        label_1->setObjectName("label_1");
        label_1->setGeometry(QRect(60, 100, 441, 81));
        QFont font1;
        font1.setPointSize(11);
        label_1->setFont(font1);
        bouton_etudiant = new QRadioButton(centralwidget);
        bouton_etudiant->setObjectName("bouton_etudiant");
        bouton_etudiant->setGeometry(QRect(100, 220, 161, 31));
        bouton_etudiant->setFont(font1);
        bouton_intervenant = new QRadioButton(centralwidget);
        bouton_intervenant->setObjectName("bouton_intervenant");
        bouton_intervenant->setGeometry(QRect(300, 220, 161, 31));
        bouton_intervenant->setFont(font1);
        bouton = new QPushButton(centralwidget);
        bouton->setObjectName("bouton");
        bouton->setGeometry(QRect(320, 340, 121, 41));
        bouton->setFont(font);
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName("menubar");
        menubar->setGeometry(QRect(0, 0, 538, 26));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName("statusbar");
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "Inscription \303\240 LISA", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "Bienvenue \303\240 l'interface d'inscription \303\240 LISA", nullptr));
        label_1->setText(QCoreApplication::translate("MainWindow", "\303\212tes-vous un(e) \303\251tudiant(e) ou un(e) intervenant(e) ?", nullptr));
        bouton_etudiant->setText(QCoreApplication::translate("MainWindow", "Etudiant(e)", nullptr));
        bouton_intervenant->setText(QCoreApplication::translate("MainWindow", "Intervenant(e)", nullptr));
        bouton->setText(QCoreApplication::translate("MainWindow", "OK", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
