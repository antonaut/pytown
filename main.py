#!/usr/bin/env python

import sys

from PyQt4 import QtGui

from ui_mainwin import Ui_MainWindow


class PyDBWin(QtGui.QMainWindow):
	""" Sets up gui and a DBConnection."""

	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)



if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)

	win = PyDBWin()
	win.show()
	sys.exit(app.exec_())

