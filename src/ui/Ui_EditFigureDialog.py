# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_EditFigureDialog.ui'
#
# Created: Sat May 14 21:36:01 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EditFigureDialog(object):
    def setupUi(self, EditFigureDialog):
        EditFigureDialog.setObjectName(_fromUtf8("EditFigureDialog"))
        EditFigureDialog.resize(815, 610)
        self.verticalLayout = QtGui.QVBoxLayout(EditFigureDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.label_44 = QtGui.QLabel(EditFigureDialog)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.gridLayout_8.addWidget(self.label_44, 0, 0, 1, 1)
        self.deleteFigureButton = QtGui.QPushButton(EditFigureDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteFigureButton.sizePolicy().hasHeightForWidth())
        self.deleteFigureButton.setSizePolicy(sizePolicy)
        self.deleteFigureButton.setObjectName(_fromUtf8("deleteFigureButton"))
        self.gridLayout_8.addWidget(self.deleteFigureButton, 0, 6, 1, 1)
        self.showFigureButton = QtGui.QPushButton(EditFigureDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showFigureButton.sizePolicy().hasHeightForWidth())
        self.showFigureButton.setSizePolicy(sizePolicy)
        self.showFigureButton.setObjectName(_fromUtf8("showFigureButton"))
        self.gridLayout_8.addWidget(self.showFigureButton, 0, 5, 1, 1)
        self.addFigureButton = QtGui.QPushButton(EditFigureDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addFigureButton.sizePolicy().hasHeightForWidth())
        self.addFigureButton.setSizePolicy(sizePolicy)
        self.addFigureButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.addFigureButton.setObjectName(_fromUtf8("addFigureButton"))
        self.gridLayout_8.addWidget(self.addFigureButton, 0, 4, 1, 1)
        self.figureSelector = QtGui.QComboBox(EditFigureDialog)
        self.figureSelector.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.figureSelector.setMinimumContentsLength(20)
        self.figureSelector.setObjectName(_fromUtf8("figureSelector"))
        self.gridLayout_8.addWidget(self.figureSelector, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem, 0, 7, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_8)
        self.line = QtGui.QFrame(EditFigureDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.tabWidget = QtGui.QTabWidget(EditFigureDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(EditFigureDialog)
        self.tabWidget.setCurrentIndex(-1)
        EditFigureDialog.setTabOrder(self.figureSelector, self.addFigureButton)
        EditFigureDialog.setTabOrder(self.addFigureButton, self.showFigureButton)
        EditFigureDialog.setTabOrder(self.showFigureButton, self.deleteFigureButton)
        EditFigureDialog.setTabOrder(self.deleteFigureButton, self.tabWidget)

    def retranslateUi(self, EditFigureDialog):
        EditFigureDialog.setWindowTitle(QtGui.QApplication.translate("EditFigureDialog", "Edit Figure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_44.setText(QtGui.QApplication.translate("EditFigureDialog", "Figure", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteFigureButton.setText(QtGui.QApplication.translate("EditFigureDialog", "Delete Figure", None, QtGui.QApplication.UnicodeUTF8))
        self.showFigureButton.setText(QtGui.QApplication.translate("EditFigureDialog", "Show Figure", None, QtGui.QApplication.UnicodeUTF8))
        self.addFigureButton.setText(QtGui.QApplication.translate("EditFigureDialog", "Add Figure", None, QtGui.QApplication.UnicodeUTF8))

