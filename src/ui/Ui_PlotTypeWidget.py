# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_PlotTypeWidget.ui'
#
# Created: Sat May 14 21:36:04 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PlotTypeWidget(object):
    def setupUi(self, PlotTypeWidget):
        PlotTypeWidget.setObjectName(_fromUtf8("PlotTypeWidget"))
        PlotTypeWidget.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(PlotTypeWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(PlotTypeWidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttons = QtGui.QDialogButtonBox(PlotTypeWidget)
        self.buttons.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Reset)
        self.buttons.setCenterButtons(True)
        self.buttons.setObjectName(_fromUtf8("buttons"))
        self.verticalLayout.addWidget(self.buttons)

        self.retranslateUi(PlotTypeWidget)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QObject.connect(self.buttons, QtCore.SIGNAL(_fromUtf8("clicked(QAbstractButton*)")), PlotTypeWidget.buttonClickHandler)

    def retranslateUi(self, PlotTypeWidget):
        PlotTypeWidget.setWindowTitle(QtGui.QApplication.translate("PlotTypeWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

