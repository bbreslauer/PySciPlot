# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ScatterPlotTraces.ui'
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

class Ui_ScatterPlotTraces(object):
    def setupUi(self, ScatterPlotTraces):
        ScatterPlotTraces.setObjectName(_fromUtf8("ScatterPlotTraces"))
        ScatterPlotTraces.resize(469, 360)
        self.horizontalLayout = QtGui.QHBoxLayout(ScatterPlotTraces)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.wavePairGroupBox = QtGui.QGroupBox(ScatterPlotTraces)
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
        self.wavePairOptionsGroupBox = QtGui.QGroupBox(ScatterPlotTraces)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wavePairOptionsGroupBox.sizePolicy().hasHeightForWidth())
        self.wavePairOptionsGroupBox.setSizePolicy(sizePolicy)
        self.wavePairOptionsGroupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.wavePairOptionsGroupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.wavePairOptionsGroupBox.setBaseSize(QtCore.QSize(300, 0))
        self.wavePairOptionsGroupBox.setObjectName(_fromUtf8("wavePairOptionsGroupBox"))
        self.gridLayout_5 = QtGui.QGridLayout(self.wavePairOptionsGroupBox)
        self.gridLayout_5.setMargin(3)
        self.gridLayout_5.setVerticalSpacing(2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.groupBox = QtGui.QGroupBox(self.wavePairOptionsGroupBox)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_16 = QtGui.QLabel(self.groupBox)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_16)
        self.lineStyle = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineStyle.sizePolicy().hasHeightForWidth())
        self.lineStyle.setSizePolicy(sizePolicy)
        self.lineStyle.setMinimumSize(QtCore.QSize(75, 0))
        self.lineStyle.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineStyle.setObjectName(_fromUtf8("lineStyle"))
        self.lineStyle.addItem(_fromUtf8(""))
        self.lineStyle.addItem(_fromUtf8(""))
        self.lineStyle.addItem(_fromUtf8(""))
        self.lineStyle.addItem(_fromUtf8(""))
        self.lineStyle.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineStyle)
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_13)
        self.lineWidth = QtGui.QDoubleSpinBox(self.groupBox)
        self.lineWidth.setMinimumSize(QtCore.QSize(55, 0))
        self.lineWidth.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineWidth.setProperty(_fromUtf8("value"), 1.0)
        self.lineWidth.setObjectName(_fromUtf8("lineWidth"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineWidth)
        self.label_15 = QtGui.QLabel(self.groupBox)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_15)
        self.lineColor = QColorButton(self.groupBox)
        self.lineColor.setMinimumSize(QtCore.QSize(55, 0))
        self.lineColor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineColor.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.lineColor.setObjectName(_fromUtf8("lineColor"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineColor)
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.wavePairOptionsGroupBox)
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.formLayout_3 = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_21 = QtGui.QLabel(self.groupBox_3)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_21)
        self.pointMarkerEdgeWidth = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.pointMarkerEdgeWidth.setMinimumSize(QtCore.QSize(55, 0))
        self.pointMarkerEdgeWidth.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pointMarkerEdgeWidth.setProperty(_fromUtf8("value"), 1.0)
        self.pointMarkerEdgeWidth.setObjectName(_fromUtf8("pointMarkerEdgeWidth"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.pointMarkerEdgeWidth)
        self.label_20 = QtGui.QLabel(self.groupBox_3)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_20)
        self.pointMarkerEdgeColor = QColorButton(self.groupBox_3)
        self.pointMarkerEdgeColor.setMinimumSize(QtCore.QSize(55, 0))
        self.pointMarkerEdgeColor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pointMarkerEdgeColor.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.pointMarkerEdgeColor.setObjectName(_fromUtf8("pointMarkerEdgeColor"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.pointMarkerEdgeColor)
        self.gridLayout_5.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.wavePairOptionsGroupBox)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_19 = QtGui.QLabel(self.groupBox_2)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_19)
        self.pointMarker = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pointMarker.sizePolicy().hasHeightForWidth())
        self.pointMarker.setSizePolicy(sizePolicy)
        self.pointMarker.setMinimumSize(QtCore.QSize(75, 0))
        self.pointMarker.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pointMarker.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.pointMarker.setObjectName(_fromUtf8("pointMarker"))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.pointMarker.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.pointMarker)
        self.label_18 = QtGui.QLabel(self.groupBox_2)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_18)
        self.pointMarkerSize = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.pointMarkerSize.setMinimumSize(QtCore.QSize(55, 0))
        self.pointMarkerSize.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pointMarkerSize.setMinimum(0.0)
        self.pointMarkerSize.setProperty(_fromUtf8("value"), 5.0)
        self.pointMarkerSize.setObjectName(_fromUtf8("pointMarkerSize"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.pointMarkerSize)
        self.label_17 = QtGui.QLabel(self.groupBox_2)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_17)
        self.pointMarkerFaceColor = QColorButton(self.groupBox_2)
        self.pointMarkerFaceColor.setMinimumSize(QtCore.QSize(55, 0))
        self.pointMarkerFaceColor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pointMarkerFaceColor.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.pointMarkerFaceColor.setObjectName(_fromUtf8("pointMarkerFaceColor"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.pointMarkerFaceColor)
        self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.wavePairOptionsGroupBox)
        self.storedSettingsButton = QStoredSettingsButton(ScatterPlotTraces)
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

        self.retranslateUi(ScatterPlotTraces)
        self.lineStyle.setCurrentIndex(1)
        self.pointMarker.setCurrentIndex(3)
        QtCore.QObject.connect(self.addwavePairButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ScatterPlotTraces.addWavePairsToPlot)
        QtCore.QObject.connect(self.removewavePairButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ScatterPlotTraces.deleteSelectedWavePairs)
        QtCore.QObject.connect(self.wavePairTableView, QtCore.SIGNAL(_fromUtf8("customContextMenuRequested(QPoint)")), ScatterPlotTraces.showWavePairListMenu)
        QtCore.QObject.connect(self.lineColor, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineColor.createColorDialog)
        QtCore.QObject.connect(self.pointMarkerFaceColor, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pointMarkerFaceColor.createColorDialog)
        QtCore.QObject.connect(self.pointMarkerEdgeColor, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pointMarkerEdgeColor.createColorDialog)
        QtCore.QObject.connect(self.storedSettingsButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.storedSettingsButton.toggleWidget)
        ScatterPlotTraces.setTabOrder(self.xAxisListView, self.yAxisListView)
        ScatterPlotTraces.setTabOrder(self.yAxisListView, self.addwavePairButton)
        ScatterPlotTraces.setTabOrder(self.addwavePairButton, self.wavePairTableView)
        ScatterPlotTraces.setTabOrder(self.wavePairTableView, self.removewavePairButton)
        ScatterPlotTraces.setTabOrder(self.removewavePairButton, self.lineStyle)
        ScatterPlotTraces.setTabOrder(self.lineStyle, self.lineWidth)
        ScatterPlotTraces.setTabOrder(self.lineWidth, self.lineColor)
        ScatterPlotTraces.setTabOrder(self.lineColor, self.pointMarker)
        ScatterPlotTraces.setTabOrder(self.pointMarker, self.pointMarkerSize)
        ScatterPlotTraces.setTabOrder(self.pointMarkerSize, self.pointMarkerFaceColor)
        ScatterPlotTraces.setTabOrder(self.pointMarkerFaceColor, self.pointMarkerEdgeWidth)
        ScatterPlotTraces.setTabOrder(self.pointMarkerEdgeWidth, self.pointMarkerEdgeColor)

    def retranslateUi(self, ScatterPlotTraces):
        ScatterPlotTraces.setWindowTitle(QtGui.QApplication.translate("ScatterPlotTraces", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.wavePairGroupBox.setTitle(QtGui.QApplication.translate("ScatterPlotTraces", "Add/Select Traces", None, QtGui.QApplication.UnicodeUTF8))
        self.xAxisLabel.setText(QtGui.QApplication.translate("ScatterPlotTraces", "X Axis", None, QtGui.QApplication.UnicodeUTF8))
        self.yAxisLabel.setText(QtGui.QApplication.translate("ScatterPlotTraces", "Y Axis", None, QtGui.QApplication.UnicodeUTF8))
        self.addwavePairButton.setText(QtGui.QApplication.translate("ScatterPlotTraces", "Add Trace(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.removewavePairButton.setText(QtGui.QApplication.translate("ScatterPlotTraces", "Remove Trace(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.wavePairOptionsGroupBox.setTitle(QtGui.QApplication.translate("ScatterPlotTraces", "Trace Options", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ScatterPlotTraces", "Line Style", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("ScatterPlotTraces", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.lineStyle.setItemText(0, QtGui.QApplication.translate("ScatterPlotTraces", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.lineStyle.setItemText(1, QtGui.QApplication.translate("ScatterPlotTraces", "Solid", None, QtGui.QApplication.UnicodeUTF8))
        self.lineStyle.setItemText(2, QtGui.QApplication.translate("ScatterPlotTraces", "Dashed", None, QtGui.QApplication.UnicodeUTF8))
        self.lineStyle.setItemText(3, QtGui.QApplication.translate("ScatterPlotTraces", "Dash Dot", None, QtGui.QApplication.UnicodeUTF8))
        self.lineStyle.setItemText(4, QtGui.QApplication.translate("ScatterPlotTraces", "Dotted", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("ScatterPlotTraces", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("ScatterPlotTraces", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.lineColor.setText(QtGui.QApplication.translate("ScatterPlotTraces", "(0,0,0,255)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("ScatterPlotTraces", "Marker Edge", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("ScatterPlotTraces", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("ScatterPlotTraces", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarkerEdgeColor.setText(QtGui.QApplication.translate("ScatterPlotTraces", "(0,0,0,255)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ScatterPlotTraces", "Marker", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("ScatterPlotTraces", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(0, QtGui.QApplication.translate("ScatterPlotTraces", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(1, QtGui.QApplication.translate("ScatterPlotTraces", "Point", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(2, QtGui.QApplication.translate("ScatterPlotTraces", "Pixel", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(3, QtGui.QApplication.translate("ScatterPlotTraces", "Circle", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(4, QtGui.QApplication.translate("ScatterPlotTraces", "Triangle - Down", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(5, QtGui.QApplication.translate("ScatterPlotTraces", "Triangle - Up", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(6, QtGui.QApplication.translate("ScatterPlotTraces", "Triangle - Left", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(7, QtGui.QApplication.translate("ScatterPlotTraces", "Triangle - Right", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(8, QtGui.QApplication.translate("ScatterPlotTraces", "Y - Down", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(9, QtGui.QApplication.translate("ScatterPlotTraces", "Y - Up", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(10, QtGui.QApplication.translate("ScatterPlotTraces", "Y - Left", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(11, QtGui.QApplication.translate("ScatterPlotTraces", "Y - Right", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(12, QtGui.QApplication.translate("ScatterPlotTraces", "Square", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(13, QtGui.QApplication.translate("ScatterPlotTraces", "Pentagon", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(14, QtGui.QApplication.translate("ScatterPlotTraces", "Star", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(15, QtGui.QApplication.translate("ScatterPlotTraces", "Hexagon 1", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(16, QtGui.QApplication.translate("ScatterPlotTraces", "Hexagon 2", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(17, QtGui.QApplication.translate("ScatterPlotTraces", "Plus", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(18, QtGui.QApplication.translate("ScatterPlotTraces", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(19, QtGui.QApplication.translate("ScatterPlotTraces", "Diamond", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(20, QtGui.QApplication.translate("ScatterPlotTraces", "Thin Diamond", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(21, QtGui.QApplication.translate("ScatterPlotTraces", "Vertical Line", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarker.setItemText(22, QtGui.QApplication.translate("ScatterPlotTraces", "Horizontal Line", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("ScatterPlotTraces", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("ScatterPlotTraces", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.pointMarkerFaceColor.setText(QtGui.QApplication.translate("ScatterPlotTraces", "(0,0,0,255)", None, QtGui.QApplication.UnicodeUTF8))
        self.storedSettingsButton.setText(QtGui.QApplication.translate("ScatterPlotTraces", "S\n"
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
