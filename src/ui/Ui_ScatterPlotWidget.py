# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ScatterPlotWidget.ui'
#
# Created: Sat May 14 21:36:06 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ScatterPlotWidget(object):
    def setupUi(self, ScatterPlotWidget):
        ScatterPlotWidget.setObjectName(_fromUtf8("ScatterPlotWidget"))
        ScatterPlotWidget.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(ScatterPlotWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(ScatterPlotWidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttons = QtGui.QDialogButtonBox(ScatterPlotWidget)
        self.buttons.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Reset)
        self.buttons.setCenterButtons(True)
        self.buttons.setObjectName(_fromUtf8("buttons"))
        self.verticalLayout.addWidget(self.buttons)

        self.retranslateUi(ScatterPlotWidget)
        self.tabWidget.setCurrentIndex(-1)

    def retranslateUi(self, ScatterPlotWidget):
        ScatterPlotWidget.setWindowTitle(QtGui.QApplication.translate("ScatterPlotWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

