# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_RenameWaveDialog.ui'
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

class Ui_RenameWaveDialog(object):
    def setupUi(self, RenameWaveDialog):
        RenameWaveDialog.setObjectName(_fromUtf8("RenameWaveDialog"))
        RenameWaveDialog.setProperty(_fromUtf8("modal"), False)
        RenameWaveDialog.resize(250, 100)
        RenameWaveDialog.setMinimumSize(QtCore.QSize(250, 100))
        self.gridLayout = QtGui.QGridLayout(RenameWaveDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(RenameWaveDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.oldWaveName = QtGui.QLabel(RenameWaveDialog)
        self.oldWaveName.setText(_fromUtf8(""))
        self.oldWaveName.setObjectName(_fromUtf8("oldWaveName"))
        self.gridLayout.addWidget(self.oldWaveName, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(RenameWaveDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.newWaveNameLineEdit = QtGui.QLineEdit(RenameWaveDialog)
        self.newWaveNameLineEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.newWaveNameLineEdit.setObjectName(_fromUtf8("newWaveNameLineEdit"))
        self.gridLayout.addWidget(self.newWaveNameLineEdit, 1, 1, 1, 1)
        self.buttons = QtGui.QDialogButtonBox(RenameWaveDialog)
        self.buttons.setOrientation(QtCore.Qt.Horizontal)
        self.buttons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttons.setCenterButtons(True)
        self.buttons.setObjectName(_fromUtf8("buttons"))
        self.gridLayout.addWidget(self.buttons, 2, 0, 1, 2)

        self.retranslateUi(RenameWaveDialog)

    def retranslateUi(self, RenameWaveDialog):
        RenameWaveDialog.setWindowTitle(QtGui.QApplication.translate("RenameWaveDialog", "Rename Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("RenameWaveDialog", "Old Wave Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("RenameWaveDialog", "New Wave Name", None, QtGui.QApplication.UnicodeUTF8))

