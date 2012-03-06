# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwin.ui'
#
# Created: Wed Feb 15 14:50:24 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(656, 600)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Pytown", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.loadBooks = QtGui.QPushButton(self.centralwidget)
        self.loadBooks.setEnabled(False)
        self.loadBooks.setGeometry(QtCore.QRect(490, 480, 121, 41))
        self.loadBooks.setText(QtGui.QApplication.translate("MainWindow", "(re)load books", None, QtGui.QApplication.UnicodeUTF8))
        self.loadBooks.setObjectName(_fromUtf8("loadBooks"))
        self.book_title = QtGui.QLineEdit(self.centralwidget)
        self.book_title.setGeometry(QtCore.QRect(60, 30, 113, 23))
        self.book_title.setObjectName(_fromUtf8("book_title"))
        self.new_stock = QtGui.QLineEdit(self.centralwidget)
        self.new_stock.setGeometry(QtCore.QRect(210, 30, 113, 23))
        self.new_stock.setObjectName(_fromUtf8("new_stock"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 61, 16))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Book title", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 10, 71, 16))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "New stock", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.updateButton = QtGui.QPushButton(self.centralwidget)
        self.updateButton.setGeometry(QtCore.QRect(340, 30, 91, 24))
        self.updateButton.setText(QtGui.QApplication.translate("MainWindow", "Update book", None, QtGui.QApplication.UnicodeUTF8))
        self.updateButton.setObjectName(_fromUtf8("updateButton"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 70, 451, 451))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 656, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionBy_aerholt_maxno = QtGui.QAction(MainWindow)
        self.actionBy_aerholt_maxno.setText(QtGui.QApplication.translate("MainWindow", "By aerholt and maxno", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBy_aerholt_maxno.setObjectName(_fromUtf8("actionBy_aerholt_maxno"))
        self.menuAbout.addAction(self.actionBy_aerholt_maxno)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

