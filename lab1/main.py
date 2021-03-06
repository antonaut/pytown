#!/usr/bin/env python

import sys

from PyQt4 import QtGui

from ui_mainwin import Ui_MainWindow
from dbiface import BooksIface

class PyDBWin(QtGui.QMainWindow):
	""" Sets up gui and a DBConnection."""

	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		exitAction = QtGui.QAction('&Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(QtGui.qApp.quit)
		self.ui.menuFile.addAction(exitAction)
		self.books = BooksIface()
		self.ui.loadBooks.setEnabled(True)
		self.ui.loadBooks.clicked.connect(self.loadBooks)
		self.ui.updateButton.clicked.connect(self.updateBooks)
		
	def updateBooks(self):
		pass
	
	def loadBooks(self):
		if debug:
			print "Books loaded"
		data = self.books.getAll()
		n = 0
		for key in data:
			m = 0
			for item in data[key]:
				self.ui.tableWidget.setItem(n,m,QTableWidgetItem(item))
				m+=1
			n+=1


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	win = PyDBWin()
	win.show()
	sys.exit(app.exec_())
