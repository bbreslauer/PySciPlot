# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ExportData.ui'
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

class Ui_ExportData(object):
    def setupUi(self, ExportData):
        ExportData.setObjectName(_fromUtf8("ExportData"))
        ExportData.resize(354, 527)
        self.verticalLayout_5 = QtGui.QVBoxLayout(ExportData)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox_2 = QtGui.QGroupBox(ExportData)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.fileName = QtGui.QLineEdit(self.groupBox_2)
        self.fileName.setObjectName(_fromUtf8("fileName"))
        self.gridLayout.addWidget(self.fileName, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.outputType = QtGui.QComboBox(self.groupBox_2)
        self.outputType.setObjectName(_fromUtf8("outputType"))
        self.outputType.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.outputType, 1, 1, 1, 2)
        self.stackedWidget = QtGui.QStackedWidget(self.groupBox_2)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.delimitedStackedWidget = QtGui.QWidget()
        self.delimitedStackedWidget.setObjectName(_fromUtf8("delimitedStackedWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.delimitedStackedWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.delimitedStackedWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.delimitedDelimiterGroupBox = QtGui.QGroupBox(self.delimitedStackedWidget)
        self.delimitedDelimiterGroupBox.setTitle(_fromUtf8(""))
        self.delimitedDelimiterGroupBox.setObjectName(_fromUtf8("delimitedDelimiterGroupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.delimitedDelimiterGroupBox)
        self.horizontalLayout.setContentsMargins(2, 0, 0, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.delimitedCommaRadio = QtGui.QRadioButton(self.delimitedDelimiterGroupBox)
        self.delimitedCommaRadio.setChecked(True)
        self.delimitedCommaRadio.setObjectName(_fromUtf8("delimitedCommaRadio"))
        self.delimiterButtonGroup = QtGui.QButtonGroup(ExportData)
        self.delimiterButtonGroup.setObjectName(_fromUtf8("delimiterButtonGroup"))
        self.delimiterButtonGroup.addButton(self.delimitedCommaRadio)
        self.horizontalLayout.addWidget(self.delimitedCommaRadio)
        self.delimitedTabRadio = QtGui.QRadioButton(self.delimitedDelimiterGroupBox)
        self.delimitedTabRadio.setObjectName(_fromUtf8("delimitedTabRadio"))
        self.delimiterButtonGroup.addButton(self.delimitedTabRadio)
        self.horizontalLayout.addWidget(self.delimitedTabRadio)
        self.delimitedOtherRadio = QtGui.QRadioButton(self.delimitedDelimiterGroupBox)
        self.delimitedOtherRadio.setObjectName(_fromUtf8("delimitedOtherRadio"))
        self.delimiterButtonGroup.addButton(self.delimitedOtherRadio)
        self.horizontalLayout.addWidget(self.delimitedOtherRadio)
        self.delimitedOtherDelimiter = QtGui.QLineEdit(self.delimitedDelimiterGroupBox)
        self.delimitedOtherDelimiter.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delimitedOtherDelimiter.sizePolicy().hasHeightForWidth())
        self.delimitedOtherDelimiter.setSizePolicy(sizePolicy)
        self.delimitedOtherDelimiter.setMaximumSize(QtCore.QSize(20, 16777215))
        self.delimitedOtherDelimiter.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delimitedOtherDelimiter.setFont(font)
        self.delimitedOtherDelimiter.setMaxLength(1)
        self.delimitedOtherDelimiter.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.delimitedOtherDelimiter.setObjectName(_fromUtf8("delimitedOtherDelimiter"))
        self.horizontalLayout.addWidget(self.delimitedOtherDelimiter)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 5)
        self.gridLayout_2.addWidget(self.delimitedDelimiterGroupBox, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.delimitedStackedWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.delimitedDataDirectionGroupBox = QtGui.QGroupBox(self.delimitedStackedWidget)
        self.delimitedDataDirectionGroupBox.setTitle(_fromUtf8(""))
        self.delimitedDataDirectionGroupBox.setObjectName(_fromUtf8("delimitedDataDirectionGroupBox"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.delimitedDataDirectionGroupBox)
        self.horizontalLayout_3.setContentsMargins(2, 0, 0, 0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.dataDirectionColumns = QtGui.QRadioButton(self.delimitedDataDirectionGroupBox)
        self.dataDirectionColumns.setChecked(True)
        self.dataDirectionColumns.setObjectName(_fromUtf8("dataDirectionColumns"))
        self.dataDirectionButtonGroup = QtGui.QButtonGroup(ExportData)
        self.dataDirectionButtonGroup.setObjectName(_fromUtf8("dataDirectionButtonGroup"))
        self.dataDirectionButtonGroup.addButton(self.dataDirectionColumns)
        self.horizontalLayout_3.addWidget(self.dataDirectionColumns)
        self.dataDirectionRows = QtGui.QRadioButton(self.delimitedDataDirectionGroupBox)
        self.dataDirectionRows.setChecked(False)
        self.dataDirectionRows.setObjectName(_fromUtf8("dataDirectionRows"))
        self.dataDirectionButtonGroup.addButton(self.dataDirectionRows)
        self.horizontalLayout_3.addWidget(self.dataDirectionRows)
        self.gridLayout_2.addWidget(self.delimitedDataDirectionGroupBox, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.delimitedStackedWidget)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 2, 0, 1, 3)
        self.fileNameButton = QtGui.QPushButton(self.groupBox_2)
        self.fileNameButton.setObjectName(_fromUtf8("fileNameButton"))
        self.gridLayout.addWidget(self.fileNameButton, 0, 2, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(ExportData)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.allWavesListView = QtGui.QListView(self.groupBox_3)
        self.allWavesListView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.allWavesListView.setObjectName(_fromUtf8("allWavesListView"))
        self.verticalLayout.addWidget(self.allWavesListView)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.addWaveButton = QtGui.QPushButton(self.groupBox_3)
        self.addWaveButton.setObjectName(_fromUtf8("addWaveButton"))
        self.verticalLayout_2.addWidget(self.addWaveButton)
        self.removeWaveButton = QtGui.QPushButton(self.groupBox_3)
        self.removeWaveButton.setObjectName(_fromUtf8("removeWaveButton"))
        self.verticalLayout_2.addWidget(self.removeWaveButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_3.addWidget(self.label_5)
        self.fileWavesListView = QtGui.QListView(self.groupBox_3)
        self.fileWavesListView.setDragEnabled(True)
        self.fileWavesListView.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.fileWavesListView.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.fileWavesListView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.fileWavesListView.setObjectName(_fromUtf8("fileWavesListView"))
        self.verticalLayout_3.addWidget(self.fileWavesListView)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.groupBox_5 = QtGui.QGroupBox(ExportData)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.exportDataButton = QtGui.QPushButton(self.groupBox_5)
        self.exportDataButton.setObjectName(_fromUtf8("exportDataButton"))
        self.verticalLayout_4.addWidget(self.exportDataButton)
        self.verticalLayout_5.addWidget(self.groupBox_5)

        self.retranslateUi(ExportData)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.delimitedOtherRadio, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.delimitedOtherDelimiter.setEnabled)
        QtCore.QObject.connect(self.outputType, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.stackedWidget.setCurrentIndex)

    def retranslateUi(self, ExportData):
        ExportData.setWindowTitle(QtGui.QApplication.translate("ExportData", "Export Data", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ExportData", "Step 1 - File Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ExportData", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ExportData", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.outputType.setItemText(0, QtGui.QApplication.translate("ExportData", "Delimited", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ExportData", "Delimiter", None, QtGui.QApplication.UnicodeUTF8))
        self.delimitedCommaRadio.setText(QtGui.QApplication.translate("ExportData", "Comma", None, QtGui.QApplication.UnicodeUTF8))
        self.delimitedTabRadio.setText(QtGui.QApplication.translate("ExportData", "Tab", None, QtGui.QApplication.UnicodeUTF8))
        self.delimitedOtherRadio.setText(QtGui.QApplication.translate("ExportData", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.delimitedOtherDelimiter.setText(QtGui.QApplication.translate("ExportData", ",", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ExportData", "Data as", None, QtGui.QApplication.UnicodeUTF8))
        self.dataDirectionColumns.setText(QtGui.QApplication.translate("ExportData", "Columns", None, QtGui.QApplication.UnicodeUTF8))
        self.dataDirectionRows.setText(QtGui.QApplication.translate("ExportData", "Rows", None, QtGui.QApplication.UnicodeUTF8))
        self.fileNameButton.setText(QtGui.QApplication.translate("ExportData", "Select...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ExportData", "Step 2 - Select Data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ExportData", "All Waves", None, QtGui.QApplication.UnicodeUTF8))
        self.addWaveButton.setText(QtGui.QApplication.translate("ExportData", "Add -->", None, QtGui.QApplication.UnicodeUTF8))
        self.removeWaveButton.setText(QtGui.QApplication.translate("ExportData", "<-- Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ExportData", "Waves to Export", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("ExportData", "Step 3 - Export", None, QtGui.QApplication.UnicodeUTF8))
        self.exportDataButton.setText(QtGui.QApplication.translate("ExportData", "Export Data", None, QtGui.QApplication.UnicodeUTF8))
