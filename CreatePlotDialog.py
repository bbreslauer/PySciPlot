# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreatePlotDialog.ui'
#
# Created: Sun Apr  4 21:56:12 2010
#      by: PyQt4 UI code generator snapshot-4.7.3-22b0acdb1b62
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CreatePlotDialog(object):
    def setupUi(self, CreatePlotDialog):
        CreatePlotDialog.setObjectName("CreatePlotDialog")
        CreatePlotDialog.resize(400, 300)
        self.gridLayoutWidget = QtGui.QWidget(CreatePlotDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.xAxisListView = QtGui.QListView(self.gridLayoutWidget)
        self.xAxisListView.setObjectName("xAxisListView")
        self.gridLayout.addWidget(self.xAxisListView, 1, 0, 1, 1)
        self.xAxisLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.xAxisLabel.setObjectName("xAxisLabel")
        self.gridLayout.addWidget(self.xAxisLabel, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.yAxisLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.yAxisLabel.setObjectName("yAxisLabel")
        self.gridLayout.addWidget(self.yAxisLabel, 0, 1, 1, 1)
        self.yAxisListView = QtGui.QListView(self.gridLayoutWidget)
        self.yAxisListView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.yAxisListView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.yAxisListView.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.yAxisListView.setObjectName("yAxisListView")
        self.gridLayout.addWidget(self.yAxisListView, 1, 1, 1, 1)

        self.retranslateUi(CreatePlotDialog)
        QtCore.QMetaObject.connectSlotsByName(CreatePlotDialog)

    def retranslateUi(self, CreatePlotDialog):
        CreatePlotDialog.setWindowTitle(QtGui.QApplication.translate("CreatePlotDialog", "Create Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.xAxisLabel.setText(QtGui.QApplication.translate("CreatePlotDialog", "X Axis", None, QtGui.QApplication.UnicodeUTF8))
        self.yAxisLabel.setText(QtGui.QApplication.translate("CreatePlotDialog", "Y Axis", None, QtGui.QApplication.UnicodeUTF8))

