# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_BarPlotBars.ui'
#
# Created: Mon May 30 17:08:44 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_BarPlotBars(object):
    def setupUi(self, BarPlotBars):
        BarPlotBars.setObjectName(_fromUtf8("BarPlotBars"))
        BarPlotBars.resize(469, 360)
        self.horizontalLayout = QtGui.QHBoxLayout(BarPlotBars)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.wavePairGroupBox = QtGui.QGroupBox(BarPlotBars)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wavePairGroupBox.sizePolicy().hasHeightForWidth())
        self.wavePairGroupBox.setSizePolicy(sizePolicy)
        self.wavePairGroupBox.setMinimumSize(QtCore.QSize(225, 0))
        self.wavePairGroupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.wavePairGroupBox.setBaseSize(QtCore.QSize(100, 0))
        self.wavePairGroupBox.setObjectName(_fromUtf8("wavePairGroupBox"))
        self.gridLayout_6 = QtGui.QGridLayout(self.wavePairGroupBox)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.xAxisLabel = QtGui.QLabel(self.wavePairGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xAxisLabel.sizePolicy().hasHeightForWidth())
        self.xAxisLabel.setSizePolicy(sizePolicy)
        self.xAxisLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.xAxisLabel.setObjectName(_fromUtf8("xAxisLabel"))
        self.gridLayout_6.addWidget(self.xAxisLabel, 0, 0, 1, 1)
        self.xAxisListView = QtGui.QListView(self.wavePairGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xAxisListView.sizePolicy().hasHeightForWidth())
        self.xAxisListView.setSizePolicy(sizePolicy)
        self.xAxisListView.setMinimumSize(QtCore.QSize(0, 0))
        self.xAxisListView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.xAxisListView.setTextElideMode(QtCore.Qt.ElideRight)
        self.xAxisListView.setObjectName(_fromUtf8("xAxisListView"))
        self.gridLayout_6.addWidget(self.xAxisListView, 1, 0, 1, 1)
        self.yAxisListView = QtGui.QListView(self.wavePairGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yAxisListView.sizePolicy().hasHeightForWidth())
        self.yAxisListView.setSizePolicy(sizePolicy)
        self.yAxisListView.setMinimumSize(QtCore.QSize(0, 0))
        self.yAxisListView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.yAxisListView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.yAxisListView.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.yAxisListView.setObjectName(_fromUtf8("yAxisListView"))
        self.gridLayout_6.addWidget(self.yAxisListView, 1, 1, 1, 1)
        self.wavePairTableView = QtGui.QTableView(self.wavePairGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wavePairTableView.sizePolicy().hasHeightForWidth())
        self.wavePairTableView.setSizePolicy(sizePolicy)
        self.wavePairTableView.setMinimumSize(QtCore.QSize(0, 0))
        self.wavePairTableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.wavePairTableView.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked)
        self.wavePairTableView.setAlternatingRowColors(False)
        self.wavePairTableView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.wavePairTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.wavePairTableView.setTextElideMode(QtCore.Qt.ElideRight)
        self.wavePairTableView.setSortingEnabled(True)
        self.wavePairTableView.setObjectName(_fromUtf8("wavePairTableView"))
        self.wavePairTableView.horizontalHeader().setDefaultSectionSize(75)
        self.wavePairTableView.verticalHeader().setVisible(False)
        self.gridLayout_6.addWidget(self.wavePairTableView, 3, 0, 1, 2)
        self.yAxisLabel = QtGui.QLabel(self.wavePairGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yAxisLabel.sizePolicy().hasHeightForWidth())
        self.yAxisLabel.setSizePolicy(sizePolicy)
        self.yAxisLabel.setObjectName(_fromUtf8("yAxisLabel"))
        self.gridLayout_6.addWidget(self.yAxisLabel, 0, 1, 1, 1)
        self.addwavePairButton = QtGui.QPushButton(self.wavePairGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addwavePairButton.sizePolicy().hasHeightForWidth())
        self.addwavePairButton.setSizePolicy(sizePolicy)
        self.addwavePairButton.setMinimumSize(QtCore.QSize(80, 0))
        self.addwavePairButton.setObjectName(_fromUtf8("addwavePairButton"))
        self.gridLayout_6.addWidget(self.addwavePairButton, 2, 1, 1, 1)
        self.removewavePairButton = QtGui.QPushButton(self.wavePairGroupBox)
        self.removewavePairButton.setObjectName(_fromUtf8("removewavePairButton"))
        self.gridLayout_6.addWidget(self.removewavePairButton, 2, 0, 1, 1)
        self.horizontalLayout.addWidget(self.wavePairGroupBox)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(BarPlotBars)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.orientation = QtGui.QComboBox(self.groupBox)
        self.orientation.setObjectName(_fromUtf8("orientation"))
        self.orientation.addItem(_fromUtf8(""))
        self.orientation.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.orientation)
        self.verticalLayout.addWidget(self.groupBox)
        self.wavePairOptionsGroupBox = QtGui.QGroupBox(BarPlotBars)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wavePairOptionsGroupBox.sizePolicy().hasHeightForWidth())
        self.wavePairOptionsGroupBox.setSizePolicy(sizePolicy)
        self.wavePairOptionsGroupBox.setObjectName(_fromUtf8("wavePairOptionsGroupBox"))
        self.formlayout = QtGui.QFormLayout(self.wavePairOptionsGroupBox)
        self.formlayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formlayout.setObjectName(_fromUtf8("formlayout"))
        self.label = QtGui.QLabel(self.wavePairOptionsGroupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formlayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.barThickness = QtGui.QDoubleSpinBox(self.wavePairOptionsGroupBox)
        self.barThickness.setMaximum(999999.0)
        self.barThickness.setSingleStep(0.5)
        self.barThickness.setProperty(_fromUtf8("value"), 1.0)
        self.barThickness.setObjectName(_fromUtf8("barThickness"))
        self.formlayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.barThickness)
        self.label_2 = QtGui.QLabel(self.wavePairOptionsGroupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formlayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.barOffset = QtGui.QDoubleSpinBox(self.wavePairOptionsGroupBox)
        self.barOffset.setMaximum(999999.0)
        self.barOffset.setObjectName(_fromUtf8("barOffset"))
        self.formlayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.barOffset)
        self.label_3 = QtGui.QLabel(self.wavePairOptionsGroupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formlayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.fillColor = QColorButton(self.wavePairOptionsGroupBox)
        self.fillColor.setMinimumSize(QtCore.QSize(55, 0))
        self.fillColor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fillColor.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 255);\n"
"color: rgb(0, 0, 0);"))
        self.fillColor.setObjectName(_fromUtf8("fillColor"))
        self.formlayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.fillColor)
        self.label_4 = QtGui.QLabel(self.wavePairOptionsGroupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formlayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.edgeColor = QColorButton(self.wavePairOptionsGroupBox)
        self.edgeColor.setMinimumSize(QtCore.QSize(55, 0))
        self.edgeColor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edgeColor.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.edgeColor.setObjectName(_fromUtf8("edgeColor"))
        self.formlayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.edgeColor)
        self.label_5 = QtGui.QLabel(self.wavePairOptionsGroupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formlayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.edgeWidth = QtGui.QDoubleSpinBox(self.wavePairOptionsGroupBox)
        self.edgeWidth.setObjectName(_fromUtf8("edgeWidth"))
        self.formlayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.edgeWidth)
        self.label_6 = QtGui.QLabel(self.wavePairOptionsGroupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formlayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.align = QtGui.QComboBox(self.wavePairOptionsGroupBox)
        self.align.setObjectName(_fromUtf8("align"))
        self.align.addItem(_fromUtf8(""))
        self.align.addItem(_fromUtf8(""))
        self.formlayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.align)
        self.verticalLayout.addWidget(self.wavePairOptionsGroupBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.storedSettingsButton = QStoredSettingsButton(BarPlotBars)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.storedSettingsButton.sizePolicy().hasHeightForWidth())
        self.storedSettingsButton.setSizePolicy(sizePolicy)
        self.storedSettingsButton.setMaximumSize(QtCore.QSize(26, 16777215))
        self.storedSettingsButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.storedSettingsButton.setArrowType(QtCore.Qt.LeftArrow)
        self.storedSettingsButton.setObjectName(_fromUtf8("storedSettingsButton"))
        self.horizontalLayout.addWidget(self.storedSettingsButton)

        self.retranslateUi(BarPlotBars)
        QtCore.QObject.connect(self.addwavePairButton, QtCore.SIGNAL(_fromUtf8("clicked()")), BarPlotBars.addWavePairsToPlot)
        QtCore.QObject.connect(self.removewavePairButton, QtCore.SIGNAL(_fromUtf8("clicked()")), BarPlotBars.deleteSelectedWavePairs)
        QtCore.QObject.connect(self.wavePairTableView, QtCore.SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), BarPlotBars.showWavePairListMenu)
        QtCore.QObject.connect(self.storedSettingsButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.storedSettingsButton.toggleWidget)
        QtCore.QObject.connect(self.edgeColor, QtCore.SIGNAL(_fromUtf8("clicked()")), self.edgeColor.createColorDialog)
        QtCore.QObject.connect(self.fillColor, QtCore.SIGNAL(_fromUtf8("clicked()")), self.fillColor.createColorDialog)
        BarPlotBars.setTabOrder(self.xAxisListView, self.yAxisListView)
        BarPlotBars.setTabOrder(self.yAxisListView, self.addwavePairButton)
        BarPlotBars.setTabOrder(self.addwavePairButton, self.wavePairTableView)
        BarPlotBars.setTabOrder(self.wavePairTableView, self.removewavePairButton)
        BarPlotBars.setTabOrder(self.removewavePairButton, self.orientation)
        BarPlotBars.setTabOrder(self.orientation, self.barThickness)
        BarPlotBars.setTabOrder(self.barThickness, self.barOffset)
        BarPlotBars.setTabOrder(self.barOffset, self.fillColor)
        BarPlotBars.setTabOrder(self.fillColor, self.edgeColor)
        BarPlotBars.setTabOrder(self.edgeColor, self.edgeWidth)
        BarPlotBars.setTabOrder(self.edgeWidth, self.align)
        BarPlotBars.setTabOrder(self.align, self.storedSettingsButton)

    def retranslateUi(self, BarPlotBars):
        BarPlotBars.setWindowTitle(QtGui.QApplication.translate("BarPlotBars", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.wavePairGroupBox.setTitle(QtGui.QApplication.translate("BarPlotBars", "Add/Select Bars", None, QtGui.QApplication.UnicodeUTF8))
        self.xAxisLabel.setText(QtGui.QApplication.translate("BarPlotBars", "X Axis", None, QtGui.QApplication.UnicodeUTF8))
        self.yAxisLabel.setText(QtGui.QApplication.translate("BarPlotBars", "Y Axis", None, QtGui.QApplication.UnicodeUTF8))
        self.addwavePairButton.setText(QtGui.QApplication.translate("BarPlotBars", "Add Bar(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.removewavePairButton.setText(QtGui.QApplication.translate("BarPlotBars", "Remove Bar(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("BarPlotBars", "Plot Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("BarPlotBars", "Orientation", None, QtGui.QApplication.UnicodeUTF8))
        self.orientation.setItemText(0, QtGui.QApplication.translate("BarPlotBars", "vertical", None, QtGui.QApplication.UnicodeUTF8))
        self.orientation.setItemText(1, QtGui.QApplication.translate("BarPlotBars", "horizontal", None, QtGui.QApplication.UnicodeUTF8))
        self.wavePairOptionsGroupBox.setTitle(QtGui.QApplication.translate("BarPlotBars", "Bar Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("BarPlotBars", "Thickness", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("BarPlotBars", "Offset", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("BarPlotBars", "Fill Color", None, QtGui.QApplication.UnicodeUTF8))
        self.fillColor.setText(QtGui.QApplication.translate("BarPlotBars", "(0,0,255,255)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("BarPlotBars", "Edge Color", None, QtGui.QApplication.UnicodeUTF8))
        self.edgeColor.setText(QtGui.QApplication.translate("BarPlotBars", "(0,0,0,255)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("BarPlotBars", "Edge Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("BarPlotBars", "Align", None, QtGui.QApplication.UnicodeUTF8))
        self.align.setItemText(0, QtGui.QApplication.translate("BarPlotBars", "edge", None, QtGui.QApplication.UnicodeUTF8))
        self.align.setItemText(1, QtGui.QApplication.translate("BarPlotBars", "center", None, QtGui.QApplication.UnicodeUTF8))
        self.storedSettingsButton.setText(QtGui.QApplication.translate("BarPlotBars", "S\n"
"t\n"
"o\n"
"r\n"
"e\n"
"d\n"
"\n"
"S\n"
"e\n"
"t\n"
"t\n"
"i\n"
"n\n"
"g\n"
"s", None, QtGui.QApplication.UnicodeUTF8))

from gui.QColorButton import QColorButton
from gui.QStoredSettingsButton import QStoredSettingsButton
