# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ModulesLoadingDialog.ui'
#
# Created: Sat May 14 21:36:03 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ModulesLoadingDialog(object):
    def setupUi(self, ModulesLoadingDialog):
        ModulesLoadingDialog.setObjectName(_fromUtf8("ModulesLoadingDialog"))
        ModulesLoadingDialog.resize(263, 291)
        self.verticalLayout = QtGui.QVBoxLayout(ModulesLoadingDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(ModulesLoadingDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.modulesList = QtGui.QListView(ModulesLoadingDialog)
        self.modulesList.setObjectName(_fromUtf8("modulesList"))
        self.verticalLayout.addWidget(self.modulesList)
        self.buttons = QtGui.QDialogButtonBox(ModulesLoadingDialog)
        self.buttons.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Reset)
        self.buttons.setCenterButtons(True)
        self.buttons.setObjectName(_fromUtf8("buttons"))
        self.verticalLayout.addWidget(self.buttons)

        self.retranslateUi(ModulesLoadingDialog)

    def retranslateUi(self, ModulesLoadingDialog):
        ModulesLoadingDialog.setWindowTitle(QtGui.QApplication.translate("ModulesLoadingDialog", "Modules", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ModulesLoadingDialog", "Modules", None, QtGui.QApplication.UnicodeUTF8))

