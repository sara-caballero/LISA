/****************************************************************************
** Meta object code from reading C++ file 'fenetre_intervenant.h'
**
** Created by: The Qt Meta Object Compiler version 68 (Qt 6.4.2)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <memory>
#include "../../../inscription/inscription/fenetre_intervenant.h"
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'fenetre_intervenant.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 68
#error "This file was generated using the moc from 6.4.2. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_stringdata_fenetre_intervenant_t {
    uint offsetsAndSizes[16];
    char stringdata0[20];
    char stringdata1[19];
    char stringdata2[1];
    char stringdata3[5];
    char stringdata4[22];
    char stringdata5[20];
    char stringdata6[29];
    char stringdata7[18];
};
#define QT_MOC_LITERAL(ofs, len) \
    uint(sizeof(qt_meta_stringdata_fenetre_intervenant_t::offsetsAndSizes) + ofs), len 
Q_CONSTINIT static const qt_meta_stringdata_fenetre_intervenant_t qt_meta_stringdata_fenetre_intervenant = {
    {
        QT_MOC_LITERAL(0, 19),  // "fenetre_intervenant"
        QT_MOC_LITERAL(20, 18),  // "on_nom_textChanged"
        QT_MOC_LITERAL(39, 0),  // ""
        QT_MOC_LITERAL(40, 4),  // "arg1"
        QT_MOC_LITERAL(45, 21),  // "on_prenom_textChanged"
        QT_MOC_LITERAL(67, 19),  // "on_code_textChanged"
        QT_MOC_LITERAL(87, 28),  // "on_module_currentTextChanged"
        QT_MOC_LITERAL(116, 17)   // "on_bouton_clicked"
    },
    "fenetre_intervenant",
    "on_nom_textChanged",
    "",
    "arg1",
    "on_prenom_textChanged",
    "on_code_textChanged",
    "on_module_currentTextChanged",
    "on_bouton_clicked"
};
#undef QT_MOC_LITERAL
} // unnamed namespace

Q_CONSTINIT static const uint qt_meta_data_fenetre_intervenant[] = {

 // content:
      10,       // revision
       0,       // classname
       0,    0, // classinfo
       5,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags, initial metatype offsets
       1,    1,   44,    2, 0x08,    1 /* Private */,
       4,    1,   47,    2, 0x08,    3 /* Private */,
       5,    1,   50,    2, 0x08,    5 /* Private */,
       6,    1,   53,    2, 0x08,    7 /* Private */,
       7,    0,   56,    2, 0x08,    9 /* Private */,

 // slots: parameters
    QMetaType::Void, QMetaType::QString,    3,
    QMetaType::Void, QMetaType::QString,    3,
    QMetaType::Void, QMetaType::QString,    3,
    QMetaType::Void, QMetaType::QString,    3,
    QMetaType::Void,

       0        // eod
};

Q_CONSTINIT const QMetaObject fenetre_intervenant::staticMetaObject = { {
    QMetaObject::SuperData::link<QDialog::staticMetaObject>(),
    qt_meta_stringdata_fenetre_intervenant.offsetsAndSizes,
    qt_meta_data_fenetre_intervenant,
    qt_static_metacall,
    nullptr,
    qt_incomplete_metaTypeArray<qt_meta_stringdata_fenetre_intervenant_t,
        // Q_OBJECT / Q_GADGET
        QtPrivate::TypeAndForceComplete<fenetre_intervenant, std::true_type>,
        // method 'on_nom_textChanged'
        QtPrivate::TypeAndForceComplete<void, std::false_type>,
        QtPrivate::TypeAndForceComplete<const QString &, std::false_type>,
        // method 'on_prenom_textChanged'
        QtPrivate::TypeAndForceComplete<void, std::false_type>,
        QtPrivate::TypeAndForceComplete<const QString &, std::false_type>,
        // method 'on_code_textChanged'
        QtPrivate::TypeAndForceComplete<void, std::false_type>,
        QtPrivate::TypeAndForceComplete<const QString &, std::false_type>,
        // method 'on_module_currentTextChanged'
        QtPrivate::TypeAndForceComplete<void, std::false_type>,
        QtPrivate::TypeAndForceComplete<const QString &, std::false_type>,
        // method 'on_bouton_clicked'
        QtPrivate::TypeAndForceComplete<void, std::false_type>
    >,
    nullptr
} };

void fenetre_intervenant::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<fenetre_intervenant *>(_o);
        (void)_t;
        switch (_id) {
        case 0: _t->on_nom_textChanged((*reinterpret_cast< std::add_pointer_t<QString>>(_a[1]))); break;
        case 1: _t->on_prenom_textChanged((*reinterpret_cast< std::add_pointer_t<QString>>(_a[1]))); break;
        case 2: _t->on_code_textChanged((*reinterpret_cast< std::add_pointer_t<QString>>(_a[1]))); break;
        case 3: _t->on_module_currentTextChanged((*reinterpret_cast< std::add_pointer_t<QString>>(_a[1]))); break;
        case 4: _t->on_bouton_clicked(); break;
        default: ;
        }
    }
}

const QMetaObject *fenetre_intervenant::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *fenetre_intervenant::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_fenetre_intervenant.stringdata0))
        return static_cast<void*>(this);
    return QDialog::qt_metacast(_clname);
}

int fenetre_intervenant::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 5)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 5;
    }
    return _id;
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
