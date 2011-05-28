# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_StoredSettingsName.ui'
#
# Created: Sat May 28 00:25:34 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_StoredSettingsName(object):
    def setupUi(self, StoredSettingsName):
        StoredSettingsName.setObjectName(_fromUtf8("StoredSettingsName"))
        StoredSettingsName.resize(246, 102)
        self.gridLayout = QtGui.QGridLayout(StoredSettingsName)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.name = QtGui.QLineEdit(StoredSettingsName)
        self.name.setObjectName(_fromUtf8("name"))
        self.gridLayout.addWidget(self.name, 1, 1, 1, 1)
        self.label = QtGui.QLabel(StoredSettingsName)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtGui.QLabel(StoredSettingsName)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.buttons = QtGui.QDialogButtonBox(StoredSettingsName)
        self.buttons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttons.setCenterButtons(True)
        self.buttons.setObjectName(_fromUtf8("buttons"))
        self.gridLayout.addWidget(self.buttons, 2, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)

        self.retranslateUi(StoredSettingsName)

    def retranslateUi(self, StoredSettingsName):
        StoredSettingsName.setWindowTitle(QtGui.QApplication.translate("StoredSettingsName", "Stored Settings Name", None, QtGui.QApplication.UnicodeUTF8))
        self.name.setPlaceholderText(QtGui.QApplication.translate("StoredSettingsName", "New Setting", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("StoredSettingsName", "What name should these settings have?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("StoredSettingsName", "Name", None, QtGui.QApplication.UnicodeUTF8))

