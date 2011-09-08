# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_RenameWaveDialog.ui'
#
# Created: Wed Sep  7 23:34:13 2011
#      by: pyside-uic 0.2.13 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_RenameWaveDialog(object):
    def setupUi(self, RenameWaveDialog):
        RenameWaveDialog.setObjectName("RenameWaveDialog")
        RenameWaveDialog.setProperty("modal", False)
        RenameWaveDialog.resize(250, 100)
        RenameWaveDialog.setMinimumSize(QtCore.QSize(250, 100))
        self.gridLayout = QtGui.QGridLayout(RenameWaveDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(RenameWaveDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.oldWaveName = QtGui.QLabel(RenameWaveDialog)
        self.oldWaveName.setText("")
        self.oldWaveName.setObjectName("oldWaveName")
        self.gridLayout.addWidget(self.oldWaveName, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(RenameWaveDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.newWaveNameLineEdit = QtGui.QLineEdit(RenameWaveDialog)
        self.newWaveNameLineEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.newWaveNameLineEdit.setObjectName("newWaveNameLineEdit")
        self.gridLayout.addWidget(self.newWaveNameLineEdit, 1, 1, 1, 1)
        self.buttons = QtGui.QDialogButtonBox(RenameWaveDialog)
        self.buttons.setOrientation(QtCore.Qt.Horizontal)
        self.buttons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttons.setCenterButtons(True)
        self.buttons.setObjectName("buttons")
        self.gridLayout.addWidget(self.buttons, 2, 0, 1, 2)

        self.retranslateUi(RenameWaveDialog)

    def retranslateUi(self, RenameWaveDialog):
        RenameWaveDialog.setWindowTitle(QtGui.QApplication.translate("RenameWaveDialog", "Rename Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("RenameWaveDialog", "Old Wave Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("RenameWaveDialog", "New Wave Name", None, QtGui.QApplication.UnicodeUTF8))

