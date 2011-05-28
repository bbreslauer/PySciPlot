# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ImportCSV.ui'
#
# Created: Sat May 28 00:16:57 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ImportCSV(object):
    def setupUi(self, ImportCSV):
        ImportCSV.setObjectName(_fromUtf8("ImportCSV"))
        ImportCSV.resize(500, 549)
        self.verticalLayout = QtGui.QVBoxLayout(ImportCSV)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(ImportCSV)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.csvFileName = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.csvFileName.sizePolicy().hasHeightForWidth())
        self.csvFileName.setSizePolicy(sizePolicy)
        self.csvFileName.setMinimumSize(QtCore.QSize(200, 0))
        self.csvFileName.setObjectName(_fromUtf8("csvFileName"))
        self.gridLayout.addWidget(self.csvFileName, 0, 1, 1, 3)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.loadDataButton = QtGui.QPushButton(self.groupBox)
        self.loadDataButton.setObjectName(_fromUtf8("loadDataButton"))
        self.gridLayout.addWidget(self.loadDataButton, 6, 0, 1, 5)
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setContentsMargins(2, 0, 0, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.commaRadio = QtGui.QRadioButton(self.groupBox_4)
        self.commaRadio.setChecked(True)
        self.commaRadio.setObjectName(_fromUtf8("commaRadio"))
        self.delimiterButtonGroup = QtGui.QButtonGroup(ImportCSV)
        self.delimiterButtonGroup.setObjectName(_fromUtf8("delimiterButtonGroup"))
        self.delimiterButtonGroup.addButton(self.commaRadio)
        self.horizontalLayout.addWidget(self.commaRadio)
        self.tabRadio = QtGui.QRadioButton(self.groupBox_4)
        self.tabRadio.setObjectName(_fromUtf8("tabRadio"))
        self.delimiterButtonGroup.addButton(self.tabRadio)
        self.horizontalLayout.addWidget(self.tabRadio)
        self.otherRadio = QtGui.QRadioButton(self.groupBox_4)
        self.otherRadio.setObjectName(_fromUtf8("otherRadio"))
        self.delimiterButtonGroup.addButton(self.otherRadio)
        self.horizontalLayout.addWidget(self.otherRadio)
        self.otherDelimiter = QtGui.QLineEdit(self.groupBox_4)
        self.otherDelimiter.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.otherDelimiter.sizePolicy().hasHeightForWidth())
        self.otherDelimiter.setSizePolicy(sizePolicy)
        self.otherDelimiter.setMaximumSize(QtCore.QSize(20, 16777215))
        self.otherDelimiter.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.otherDelimiter.setFont(font)
        self.otherDelimiter.setMaxLength(1)
        self.otherDelimiter.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.otherDelimiter.setObjectName(_fromUtf8("otherDelimiter"))
        self.horizontalLayout.addWidget(self.otherDelimiter)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 5)
        self.gridLayout.addWidget(self.groupBox_4, 1, 1, 1, 4)
        self.csvFileNameButton = QtGui.QPushButton(self.groupBox)
        self.csvFileNameButton.setObjectName(_fromUtf8("csvFileNameButton"))
        self.gridLayout.addWidget(self.csvFileNameButton, 0, 4, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.defaultDataType = QtGui.QComboBox(self.groupBox)
        self.defaultDataType.setObjectName(_fromUtf8("defaultDataType"))
        self.defaultDataType.addItem(_fromUtf8(""))
        self.defaultDataType.addItem(_fromUtf8(""))
        self.defaultDataType.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.defaultDataType, 4, 1, 1, 1)
        self.firstRowWaveNames = QtGui.QCheckBox(self.groupBox)
        self.firstRowWaveNames.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.firstRowWaveNames.setObjectName(_fromUtf8("firstRowWaveNames"))
        self.gridLayout.addWidget(self.firstRowWaveNames, 2, 0, 1, 2)
        self.waveNamePrefix = QtGui.QLineEdit(self.groupBox)
        self.waveNamePrefix.setEnabled(False)
        self.waveNamePrefix.setObjectName(_fromUtf8("waveNamePrefix"))
        self.gridLayout.addWidget(self.waveNamePrefix, 2, 4, 1, 1)
        self.useWaveNamePrefix = QtGui.QCheckBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.useWaveNamePrefix.sizePolicy().hasHeightForWidth())
        self.useWaveNamePrefix.setSizePolicy(sizePolicy)
        self.useWaveNamePrefix.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.useWaveNamePrefix.setObjectName(_fromUtf8("useWaveNamePrefix"))
        self.gridLayout.addWidget(self.useWaveNamePrefix, 2, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(ImportCSV)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.data = QtGui.QTableWidget(self.groupBox_2)
        self.data.setObjectName(_fromUtf8("data"))
        self.data.setColumnCount(0)
        self.data.setRowCount(0)
        self.gridLayout_2.addWidget(self.data, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(ImportCSV)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.importDataButton = QtGui.QPushButton(self.groupBox_3)
        self.importDataButton.setObjectName(_fromUtf8("importDataButton"))
        self.verticalLayout_2.addWidget(self.importDataButton)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(ImportCSV)
        QtCore.QObject.connect(self.otherRadio, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.otherDelimiter.setEnabled)
        QtCore.QObject.connect(self.useWaveNamePrefix, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.waveNamePrefix.setEnabled)
        ImportCSV.setTabOrder(self.csvFileName, self.csvFileNameButton)
        ImportCSV.setTabOrder(self.csvFileNameButton, self.commaRadio)
        ImportCSV.setTabOrder(self.commaRadio, self.tabRadio)
        ImportCSV.setTabOrder(self.tabRadio, self.otherRadio)
        ImportCSV.setTabOrder(self.otherRadio, self.otherDelimiter)
        ImportCSV.setTabOrder(self.otherDelimiter, self.loadDataButton)
        ImportCSV.setTabOrder(self.loadDataButton, self.data)
        ImportCSV.setTabOrder(self.data, self.importDataButton)

    def retranslateUi(self, ImportCSV):
        ImportCSV.setWindowTitle(QtGui.QApplication.translate("ImportCSV", "Import Data From CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ImportCSV", "Step 1 - Select CSV File", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ImportCSV", "CSV File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ImportCSV", "Delimiter", None, QtGui.QApplication.UnicodeUTF8))
        self.loadDataButton.setText(QtGui.QApplication.translate("ImportCSV", "Load Data", None, QtGui.QApplication.UnicodeUTF8))
        self.commaRadio.setText(QtGui.QApplication.translate("ImportCSV", "Comma", None, QtGui.QApplication.UnicodeUTF8))
        self.tabRadio.setText(QtGui.QApplication.translate("ImportCSV", "Tab", None, QtGui.QApplication.UnicodeUTF8))
        self.otherRadio.setText(QtGui.QApplication.translate("ImportCSV", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.otherDelimiter.setText(QtGui.QApplication.translate("ImportCSV", ",", None, QtGui.QApplication.UnicodeUTF8))
        self.csvFileNameButton.setText(QtGui.QApplication.translate("ImportCSV", "Select...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ImportCSV", "Default Data Type", None, QtGui.QApplication.UnicodeUTF8))
        self.defaultDataType.setItemText(0, QtGui.QApplication.translate("ImportCSV", "Integer", None, QtGui.QApplication.UnicodeUTF8))
        self.defaultDataType.setItemText(1, QtGui.QApplication.translate("ImportCSV", "Decimal", None, QtGui.QApplication.UnicodeUTF8))
        self.defaultDataType.setItemText(2, QtGui.QApplication.translate("ImportCSV", "String", None, QtGui.QApplication.UnicodeUTF8))
        self.firstRowWaveNames.setText(QtGui.QApplication.translate("ImportCSV", "Use first row for\n"
"wave names", None, QtGui.QApplication.UnicodeUTF8))
        self.useWaveNamePrefix.setText(QtGui.QApplication.translate("ImportCSV", "Prefix names", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ImportCSV", "Step 2 - Verify Data and enter wave names", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ImportCSV", "Step 3 - Import", None, QtGui.QApplication.UnicodeUTF8))
        self.importDataButton.setText(QtGui.QApplication.translate("ImportCSV", "Import Data", None, QtGui.QApplication.UnicodeUTF8))

