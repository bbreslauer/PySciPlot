# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_CreateTableDialog.ui'
#
# Created: Sat Aug 27 19:02:54 2011
#      by: pyside-uic 0.2.13 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CreateTableDialog(object):
    def setupUi(self, CreateTableDialog):
        CreateTableDialog.setObjectName("CreateTableDialog")
        CreateTableDialog.resize(400, 350)
        self.verticalLayout_4 = QtGui.QVBoxLayout(CreateTableDialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(CreateTableDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.tableName = QtGui.QLineEdit(CreateTableDialog)
        self.tableName.setObjectName("tableName")
        self.horizontalLayout_3.addWidget(self.tableName)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(CreateTableDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.allWavesListView = QtGui.QListView(CreateTableDialog)
        self.allWavesListView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.allWavesListView.setObjectName("allWavesListView")
        self.verticalLayout.addWidget(self.allWavesListView)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.addWaveButton = QtGui.QPushButton(CreateTableDialog)
        self.addWaveButton.setObjectName("addWaveButton")
        self.verticalLayout_2.addWidget(self.addWaveButton)
        self.removeWaveButton = QtGui.QPushButton(CreateTableDialog)
        self.removeWaveButton.setObjectName("removeWaveButton")
        self.verticalLayout_2.addWidget(self.removeWaveButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtGui.QLabel(CreateTableDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.tableWavesListView = QtGui.QListView(CreateTableDialog)
        self.tableWavesListView.setDragEnabled(True)
        self.tableWavesListView.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.tableWavesListView.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tableWavesListView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.tableWavesListView.setObjectName("tableWavesListView")
        self.verticalLayout_3.addWidget(self.tableWavesListView)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.createTableButton = QtGui.QPushButton(CreateTableDialog)
        self.createTableButton.setObjectName("createTableButton")
        self.horizontalLayout_2.addWidget(self.createTableButton)
        self.closeWindowButton = QtGui.QPushButton(CreateTableDialog)
        self.closeWindowButton.setObjectName("closeWindowButton")
        self.horizontalLayout_2.addWidget(self.closeWindowButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.retranslateUi(CreateTableDialog)

    def retranslateUi(self, CreateTableDialog):
        CreateTableDialog.setWindowTitle(QtGui.QApplication.translate("CreateTableDialog", "Create Table", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CreateTableDialog", "Table Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tableName.setText(QtGui.QApplication.translate("CreateTableDialog", "Table", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CreateTableDialog", "All Waves", None, QtGui.QApplication.UnicodeUTF8))
        self.addWaveButton.setText(QtGui.QApplication.translate("CreateTableDialog", "Add -->", None, QtGui.QApplication.UnicodeUTF8))
        self.removeWaveButton.setText(QtGui.QApplication.translate("CreateTableDialog", "<-- Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CreateTableDialog", "Waves in Table", None, QtGui.QApplication.UnicodeUTF8))
        self.createTableButton.setText(QtGui.QApplication.translate("CreateTableDialog", "Create Table", None, QtGui.QApplication.UnicodeUTF8))
        self.closeWindowButton.setText(QtGui.QApplication.translate("CreateTableDialog", "Close Window", None, QtGui.QApplication.UnicodeUTF8))

