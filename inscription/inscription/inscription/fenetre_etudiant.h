#ifndef FENETRE_ETUDIANT_H
#define FENETRE_ETUDIANT_H

#include <QDialog>

namespace Ui {
class fenetre_etudiant;
}

class fenetre_etudiant : public QDialog
{
    Q_OBJECT

public:
    explicit fenetre_etudiant(QWidget *parent = nullptr);
    ~fenetre_etudiant();

private slots:

    void on_nom_textChanged(const QString &arg1);

    void on_prenom_textChanged(const QString &arg1);

    void on_code_textChanged(const QString &arg1);

    void on_promotion_currentTextChanged(const QString &arg1);

    void on_bouton_clicked();

private:
    Ui::fenetre_etudiant *ui;
};

#endif // FENETRE_ETUDIANT_H
