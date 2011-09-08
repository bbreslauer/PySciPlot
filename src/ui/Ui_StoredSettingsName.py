# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_StoredSettingsName.ui'
#
# Created: Wed Sep  7 23:34:13 2011
#      by: pyside-uic 0.2.13 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_StoredSettingsName(object):
    def setupUi(self, StoredSettingsName):
        StoredSettingsName.setObjectName("StoredSettingsName")
        StoredSettingsName.resize(246, 102)
        self.gridLayout = QtGui.QGridLayout(StoredSettingsName)
        self.gridLayout.setObjectName("gridLayout")
        self.name = QtGui.QLineEdit(StoredSettingsName)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 1, 1, 1, 1)
        self.label = QtGui.QLabel(StoredSettingsName)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtGui.QLabel(StoredSettingsName)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.buttons = QtGui.QDialogButtonBox(StoredSettingsName)
        self.buttons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttons.setCenterButtons(True)
        self.buttons.setObjectName("buttons")
        self.gridLayout.addWidget(self.buttons, 2, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)

        self.retranslateUi(StoredSettingsName)

    def retranslateUi(self, StoredSettingsName):
        StoredSettingsName.setWindowTitle(QtGui.QApplication.translate("StoredSettingsName", "Stored Settings Name", None, QtGui.QApplication.UnicodeUTF8))
        self.name.setPlaceholderText(QtGui.QApplication.translate("StoredSettingsName", "New Setting", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("StoredSettingsName", "What name should these settings have?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("StoredSettingsName", "Name", None, QtGui.QApplication.UnicodeUTF8))

