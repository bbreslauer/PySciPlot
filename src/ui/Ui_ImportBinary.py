# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ImportBinary.ui'
#
# Created: Sat May 14 21:36:02 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ImportBinary(object):
    def setupUi(self, ImportBinary):
        ImportBinary.setObjectName(_fromUtf8("ImportBinary"))
        ImportBinary.resize(479, 129)
        self.gridLayout = QtGui.QGridLayout(ImportBinary)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(ImportBinary)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.fileName = QtGui.QLineEdit(ImportBinary)
        self.fileName.setObjectName(_fromUtf8("fileName"))
        self.gridLayout.addWidget(self.fileName, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(ImportBinary)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(ImportBinary)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.waveName = QtGui.QLineEdit(ImportBinary)
        self.waveName.setObjectName(_fromUtf8("waveName"))
        self.gridLayout.addWidget(self.waveName, 1, 1, 1, 3)
        self.dataType = QtGui.QComboBox(ImportBinary)
        self.dataType.setObjectName(_fromUtf8("dataType"))
        self.dataType.addItem(_fromUtf8(""))
        self.dataType.addItem(_fromUtf8(""))
        self.dataType.addItem(_fromUtf8(""))
        self.dataType.addItem(_fromUtf8(""))
        self.dataType.addItem(_fromUtf8(""))
        self.dataType.addItem(_fromUtf8(""))
        self.dataType.addItem(_fromUtf8(""))
        self.dataType.addItem(_fromUtf8(""))
        self.dataType.addItem(_fromUtf8(""))
        self.dataType.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.dataType, 2, 1, 1, 1)
        self.fileNameButton = QtGui.QPushButton(ImportBinary)
        self.fileNameButton.setObjectName(_fromUtf8("fileNameButton"))
        self.gridLayout.addWidget(self.fileNameButton, 0, 3, 1, 1)
        self.importDataButton = QtGui.QPushButton(ImportBinary)
        self.importDataButton.setObjectName(_fromUtf8("importDataButton"))
        self.gridLayout.addWidget(self.importDataButton, 4, 0, 1, 4)
        self.byteOrder = QtGui.QComboBox(ImportBinary)
        self.byteOrder.setObjectName(_fromUtf8("byteOrder"))
        self.byteOrder.addItem(_fromUtf8(""))
        self.byteOrder.addItem(_fromUtf8(""))
        self.byteOrder.addItem(_fromUtf8(""))
        self.byteOrder.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.byteOrder, 2, 3, 1, 1)
        self.label_5 = QtGui.QLabel(ImportBinary)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)

        self.retranslateUi(ImportBinary)
        self.dataType.setCurrentIndex(4)
        ImportBinary.setTabOrder(self.fileName, self.fileNameButton)
        ImportBinary.setTabOrder(self.fileNameButton, self.waveName)
        ImportBinary.setTabOrder(self.waveName, self.dataType)
        ImportBinary.setTabOrder(self.dataType, self.byteOrder)
        ImportBinary.setTabOrder(self.byteOrder, self.importDataButton)

    def retranslateUi(self, ImportBinary):
        ImportBinary.setWindowTitle(QtGui.QApplication.translate("ImportBinary", "Import Binary Data", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ImportBinary", "Binary File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ImportBinary", "Wave Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ImportBinary", "Data Type (byte length)", None, QtGui.QApplication.UnicodeUTF8))
        self.dataType.setItemText(0, QtGui.QApplication.translate("ImportBinary", "Signed Integer (1)", None, QtGui.QApplication.UnicodeUTF8))
        self.dataType.setItemText(1, QtGui.QApplication.translate("ImportBinary", "Unsigned Integer (1)", None, QtGui.QApplication.UnicodeUTF8))
        self.dataType.setItemText(2, QtGui.QApplication.translate("ImportBinary", "Short (2)", None, QtGui.QApplication.UnicodeUTF8))
        self.dataType.setItemText(3, QtGui.QApplication.translate("ImportBinary", "Unsigned Short (2)", None, QtGui.QApplication.UnicodeUTF8))
        self.dataType.setItemText(4, QtGui.QApplication.translate("ImportBinary", "Integer (4)", None, QtGui.QApplication.UnicodeUTF8))
        self.dataType.setItemText(5, QtGui.QApplication.translate("ImportBinary", "Unsigned Integer (4)", None, QtGui.QApplication.UnicodeUTF8))
        self.dataType.setItemText(6, QtGui.QApplication.translate("ImportBinary", "Long (8)", None, QtGui.QApplication.UnicodeUTF8))
        self.dataType.setItemText(7, QtGui.QApplication.translate("ImportBinary", "Unsigned Long (8)", None, QtGui.QApplication.UnicodeUTF8))
        self.dataType.setItemText(8, QtGui.QApplication.translate("ImportBinary", "Float (4)", None, QtGui.QApplication.UnicodeUTF8))
        self.dataType.setItemText(9, QtGui.QApplication.translate("ImportBinary", "Double (8)", None, QtGui.QApplication.UnicodeUTF8))
        self.fileNameButton.setText(QtGui.QApplication.translate("ImportBinary", "Select...", None, QtGui.QApplication.UnicodeUTF8))
        self.importDataButton.setText(QtGui.QApplication.translate("ImportBinary", "Import Data", None, QtGui.QApplication.UnicodeUTF8))
        self.byteOrder.setItemText(0, QtGui.QApplication.translate("ImportBinary", "Native", None, QtGui.QApplication.UnicodeUTF8))
        self.byteOrder.setItemText(1, QtGui.QApplication.translate("ImportBinary", "Big Endian", None, QtGui.QApplication.UnicodeUTF8))
        self.byteOrder.setItemText(2, QtGui.QApplication.translate("ImportBinary", "Little Endian", None, QtGui.QApplication.UnicodeUTF8))
        self.byteOrder.setItemText(3, QtGui.QApplication.translate("ImportBinary", "Network", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ImportBinary", "Byte Order", None, QtGui.QApplication.UnicodeUTF8))

