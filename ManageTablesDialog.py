# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManageTablesDialog.ui'
#
# Created: Tue Mar 23 23:19:15 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ManageTablesDialog(object):
    def setupUi(self, ManageTablesDialog):
        ManageTablesDialog.setObjectName("ManageTablesDialog")
        ManageTablesDialog.resize(600, 400)
        ManageTablesDialog.setMinimumSize(QtCore.QSize(400, 300))
        self.gridLayoutWidget = QtGui.QWidget(ManageTablesDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 601, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listView = QtGui.QListView(self.gridLayoutWidget)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 1)
        self.listView_2 = QtGui.QListView(self.gridLayoutWidget)
        self.listView_2.setObjectName("listView_2")
        self.gridLayout.addWidget(self.listView_2, 1, 1, 1, 1)
        self.listView_3 = QtGui.QListView(self.gridLayoutWidget)
        self.listView_3.setObjectName("listView_3")
        self.gridLayout.addWidget(self.listView_3, 1, 2, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.closeButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 2, 0, 1, 3)

        self.retranslateUi(ManageTablesDialog)
        QtCore.QMetaObject.connectSlotsByName(ManageTablesDialog)

    def retranslateUi(self, ManageTablesDialog):
        ManageTablesDialog.setWindowTitle(QtGui.QApplication.translate("ManageTablesDialog", "Manage Tables", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ManageTablesDialog", "Tables", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ManageTablesDialog", "All Waves", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ManageTablesDialog", "Waves in Table", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("ManageTablesDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

