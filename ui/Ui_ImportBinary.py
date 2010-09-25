# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ImportBinary.ui'
#
# Created: Fri Sep 24 23:46:44 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ImportBinary(object):
    def setupUi(self, ImportBinary):
        ImportBinary.setObjectName("ImportBinary")
        ImportBinary.resize(373, 129)
        self.gridLayout = QtGui.QGridLayout(ImportBinary)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(ImportBinary)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.fileName = QtGui.QLineEdit(ImportBinary)
        self.fileName.setObjectName("fileName")
        self.gridLayout.addWidget(self.fileName, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(ImportBinary)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(ImportBinary)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.waveName = QtGui.QLineEdit(ImportBinary)
        self.waveName.setObjectName("waveName")
        self.gridLayout.addWidget(self.waveName, 1, 1, 1, 3)
        self.dataType = QtGui.QComboBox(ImportBinary)
        self.dataType.setObjectName("dataType")
        self.dataType.addItem("")
        self.dataType.addItem("")
        self.dataType.addItem("")
        self.gridLayout.addWidget(self.dataType, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(ImportBinary)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)
        self.numBytes = QtGui.QSpinBox(ImportBinary)
        self.numBytes.setProperty("value", 4)
        self.numBytes.setObjectName("numBytes")
        self.gridLayout.addWidget(self.numBytes, 2, 3, 1, 1)
        self.fileNameButton = QtGui.QPushButton(ImportBinary)
        self.fileNameButton.setObjectName("fileNameButton")
        self.gridLayout.addWidget(self.fileNameButton, 0, 3, 1, 1)
        self.importDataButton = QtGui.QPushButton(ImportBinary)
        self.importDataButton.setObjectName("importDataButton")
        self.gridLayout.addWidget(self.importDataButton, 3, 0, 1, 4)

        self.retranslateUi(ImportBinary)

    def retranslateUi(self, ImportBinary):
        ImportBinary.setWindowTitle(QtGui.QApplication.translate("ImportBinary", "Import Binary Data", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ImportBinary", "Binary File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ImportBinary", "Wave Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ImportBinary", "Data Type", None, QtGui.QApplication.UnicodeUTF8))
        self.dataType.setItemText(0, QtGui.QApplication.translate("ImportBinary", "Signed Integer", None, QtGui.QApplication.UnicodeUTF8))
        self.dataType.setItemText(1, QtGui.QApplication.translate("ImportBinary", "Unsigned Integer", None, QtGui.QApplication.UnicodeUTF8))
        self.dataType.setItemText(2, QtGui.QApplication.translate("ImportBinary", "Float", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ImportBinary", "# Bytes", None, QtGui.QApplication.UnicodeUTF8))
        self.fileNameButton.setText(QtGui.QApplication.translate("ImportBinary", "Select...", None, QtGui.QApplication.UnicodeUTF8))
        self.importDataButton.setText(QtGui.QApplication.translate("ImportBinary", "Import Data", None, QtGui.QApplication.UnicodeUTF8))

