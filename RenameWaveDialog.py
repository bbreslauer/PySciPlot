# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RenameWaveDialog.ui'
#
# Created: Tue Mar 23 23:19:32 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_RenameWaveDialog(object):
    def setupUi(self, RenameWaveDialog):
        RenameWaveDialog.setObjectName("RenameWaveDialog")
        RenameWaveDialog.setWindowModality(QtCore.Qt.NonModal)
        RenameWaveDialog.resize(250, 100)
        RenameWaveDialog.setMinimumSize(QtCore.QSize(250, 100))
        RenameWaveDialog.setModal(False)
        self.formLayoutWidget = QtGui.QWidget(RenameWaveDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 251, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.oldWaveName = QtGui.QLabel(self.formLayoutWidget)
        self.oldWaveName.setText("")
        self.oldWaveName.setObjectName("oldWaveName")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.oldWaveName)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.newWaveNameLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.newWaveNameLineEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.newWaveNameLineEdit.setObjectName("newWaveNameLineEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.newWaveNameLineEdit)
        self.buttonBox = QtGui.QDialogButtonBox(RenameWaveDialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 60, 160, 25))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(RenameWaveDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), RenameWaveDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), RenameWaveDialog.reject)

    def retranslateUi(self, RenameWaveDialog):
        RenameWaveDialog.setWindowTitle(QtGui.QApplication.translate("RenameWaveDialog", "Rename Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("RenameWaveDialog", "Old Wave Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("RenameWaveDialog", "New Wave Name", None, QtGui.QApplication.UnicodeUTF8))

