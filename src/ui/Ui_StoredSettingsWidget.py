# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_StoredSettingsWidget.ui'
#
# Created: Sat May 28 00:16:59 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_StoredSettingsWidget(object):
    def setupUi(self, StoredSettingsWidget):
        StoredSettingsWidget.setObjectName(_fromUtf8("StoredSettingsWidget"))
        StoredSettingsWidget.resize(267, 453)
        StoredSettingsWidget.setAutoFillBackground(True)
        StoredSettingsWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        StoredSettingsWidget.setFrameShadow(QtGui.QFrame.Sunken)
        StoredSettingsWidget.setLineWidth(2)
        self.gridLayout = QtGui.QGridLayout(StoredSettingsWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.storedSettingsView = QtGui.QListView(StoredSettingsWidget)
        self.storedSettingsView.setObjectName(_fromUtf8("storedSettingsView"))
        self.gridLayout.addWidget(self.storedSettingsView, 1, 1, 1, 3)
        self.label = QtGui.QLabel(StoredSettingsWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 3)
        self.deleteButton = QtGui.QPushButton(StoredSettingsWidget)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.gridLayout.addWidget(self.deleteButton, 2, 2, 1, 1)
        self.saveButton = QtGui.QPushButton(StoredSettingsWidget)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.gridLayout.addWidget(self.saveButton, 2, 1, 1, 1)
        self.loadButton = QtGui.QPushButton(StoredSettingsWidget)
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        self.gridLayout.addWidget(self.loadButton, 2, 3, 1, 1)

        self.retranslateUi(StoredSettingsWidget)
        QtCore.QObject.connect(self.saveButton, QtCore.SIGNAL(_fromUtf8("clicked()")), StoredSettingsWidget.saveClicked)
        QtCore.QObject.connect(self.deleteButton, QtCore.SIGNAL(_fromUtf8("clicked()")), StoredSettingsWidget.deleteClicked)
        QtCore.QObject.connect(self.loadButton, QtCore.SIGNAL(_fromUtf8("clicked()")), StoredSettingsWidget.loadClicked)

    def retranslateUi(self, StoredSettingsWidget):
        StoredSettingsWidget.setWindowTitle(QtGui.QApplication.translate("StoredSettingsWidget", "Stored Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("StoredSettingsWidget", "Stored Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("StoredSettingsWidget", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("StoredSettingsWidget", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.loadButton.setText(QtGui.QApplication.translate("StoredSettingsWidget", "Load", None, QtGui.QApplication.UnicodeUTF8))

