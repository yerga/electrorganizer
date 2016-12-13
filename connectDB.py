#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMessageBox, qApp
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def createDB():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('electrorganizer.db')

    if not db.open():
        QMessageBox.critical(None, qApp.tr("Cannot open database"),
                                   qApp.tr("Unable to establish a database connection.\n"
                                                 "This example needs SQLite support. Please read "
                                                 "the Qt SQL driver documentation for information "
                                                 "how to build it.\n\n" "Click Cancel to exit."),
                                   QMessageBox.Cancel)

        return False

    query = QSqlQuery()
    query.exec_("create table components(id int primary key, "
                "name varchar(30), category varchar(20), description varchar(100), "
                "amount int, manufacturer varchar(20), manid varchar(25), "
                "supplier varchar(20), supid varchar(25), price float, storage varchar(20), "
                "link varchar(100), datasheet varchar(100))")



    #query.exec_("insert into components values(1, '1N4001', 'Diodos', 'Rectificadores Vr/50V Io/1A', 10, 'Micro Commercial Components (MCC)', '1N4001-TP', 'Mouser', '833-1N4001-TP', 0.104, 'Caja blanca', 'http://www.mouser.es/ProductDetail/Micro-Commercial-Components-MCC/1N4001-TP', 'http://www.mouser.com/ds/2/258/1N4001-1N4007(DO-41)-349533.pdf')")
    #query.exec_("insert into components values(2, '2.2K', 'Resistencias', 'Resistores de película de metal - a través del orificio 1/4watt 2.2Kohms 5% Rated to 1/2watt', 30, 'Vishay / Dale', 'CCF072K20JKE36', 'Mouser', '71-CCF072K20JKE36', 0.094, 'Caja blanca', 'http://www.mouser.es/ProductDetail/Vishay-Dale/CCF072K20JKE36/', 'http://www.mouser.com/ds/2/427/ccf07-239748.pdf')")
    #query.exec_("insert into components values(3, 'name', 'cat', 'desc', 10, 'man', 'manid', 'supp', 'supid', 1.3, 'storage', 'link', 'data')")

    return True