#ifndef FENETRE_INTERVENANT_H
#define FENETRE_INTERVENANT_H

#include <QDialog>

namespace Ui {
class fenetre_intervenant;
}

class fenetre_intervenant : public QDialog
{
    Q_OBJECT

public:
    explicit fenetre_intervenant(QWidget *parent = nullptr);
    ~fenetre_intervenant();


private slots:

    void on_nom_textChanged(const QString &arg1);

    void on_prenom_textChanged(const QString &arg1);

    void on_code_textChanged(const QString &arg1);

    void on_module_currentTextChanged(const QString &arg1);

    void on_bouton_clicked();

private:
    Ui::fenetre_intervenant *ui;
};

#endif // FENETRE_INTERVENANT_H
