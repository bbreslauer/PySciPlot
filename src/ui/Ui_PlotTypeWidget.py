# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_PlotTypeWidget.ui'
#
# Created: Wed Sep  7 23:34:13 2011
#      by: pyside-uic 0.2.13 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_PlotTypeWidget(object):
    def setupUi(self, PlotTypeWidget):
        PlotTypeWidget.setObjectName("PlotTypeWidget")
        PlotTypeWidget.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(PlotTypeWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(PlotTypeWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttons = QtGui.QDialogButtonBox(PlotTypeWidget)
        self.buttons.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Reset)
        self.buttons.setCenterButtons(True)
        self.buttons.setObjectName("buttons")
        self.verticalLayout.addWidget(self.buttons)

        self.retranslateUi(PlotTypeWidget)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QObject.connect(self.buttons, QtCore.SIGNAL("clicked(QAbstractButton*)"), PlotTypeWidget.buttonClickHandler)

    def retranslateUi(self, PlotTypeWidget):
        PlotTypeWidget.setWindowTitle(QtGui.QApplication.translate("PlotTypeWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))

