# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_CurveFitting.ui'
#
# Created: Sun Jun  5 22:04:55 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CurveFitting(object):
    def setupUi(self, CurveFitting):
        CurveFitting.setObjectName(_fromUtf8("CurveFitting"))
        CurveFitting.resize(546, 499)
        self.verticalLayout = QtGui.QVBoxLayout(CurveFitting)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(CurveFitting)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabFunction = QtGui.QWidget()
        self.tabFunction.setObjectName(_fromUtf8("tabFunction"))
        self.gridLayout = QtGui.QGridLayout(self.tabFunction)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.tabFunction)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.function = QtGui.QComboBox(self.tabFunction)
        self.function.setObjectName(_fromUtf8("function"))
        self.function.addItem(_fromUtf8(""))
        self.function.addItem(_fromUtf8(""))
        self.function.addItem(_fromUtf8(""))
        self.function.addItem(_fromUtf8(""))
        self.function.addItem(_fromUtf8(""))
        self.function.addItem(_fromUtf8(""))
        self.function.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.function, 0, 1, 1, 1)
        self.parameterTable = QtGui.QTableWidget(self.tabFunction)
        self.parameterTable.setEnabled(True)
        self.parameterTable.setObjectName(_fromUtf8("parameterTable"))
        self.parameterTable.setColumnCount(2)
        self.parameterTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.parameterTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.parameterTable.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.parameterTable, 4, 0, 1, 2)
        self.functionStackedWidget = QtGui.QStackedWidget(self.tabFunction)
        self.functionStackedWidget.setObjectName(_fromUtf8("functionStackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.formLayout = QtGui.QFormLayout(self.page)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.polynomialDegree = QtGui.QSpinBox(self.page)
        self.polynomialDegree.setProperty(_fromUtf8("value"), 2)
        self.polynomialDegree.setObjectName(_fromUtf8("polynomialDegree"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.polynomialDegree)
        self.functionStackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.functionStackedWidget.addWidget(self.page_2)
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.functionStackedWidget.addWidget(self.page_5)
        self.page_7 = QtGui.QWidget()
        self.page_7.setObjectName(_fromUtf8("page_7"))
        self.functionStackedWidget.addWidget(self.page_7)
        self.page_9 = QtGui.QWidget()
        self.page_9.setObjectName(_fromUtf8("page_9"))
        self.functionStackedWidget.addWidget(self.page_9)
        self.page_11 = QtGui.QWidget()
        self.page_11.setObjectName(_fromUtf8("page_11"))
        self.functionStackedWidget.addWidget(self.page_11)
        self.page_14 = QtGui.QWidget()
        self.page_14.setObjectName(_fromUtf8("page_14"))
        self.functionStackedWidget.addWidget(self.page_14)
        self.gridLayout.addWidget(self.functionStackedWidget, 1, 0, 1, 2)
        self.equationStackedWidget = QtGui.QStackedWidget(self.tabFunction)
        self.equationStackedWidget.setObjectName(_fromUtf8("equationStackedWidget"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.label_10 = QtGui.QLabel(self.page_3)
        self.label_10.setGeometry(QtCore.QRect(100, 20, 184, 13))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.equationStackedWidget.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.label_9 = QtGui.QLabel(self.page_4)
        self.label_9.setGeometry(QtCore.QRect(140, 30, 221, 41))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.equationStackedWidget.addWidget(self.page_4)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.label_14 = QtGui.QLabel(self.page_6)
        self.label_14.setGeometry(QtCore.QRect(170, 30, 221, 41))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.equationStackedWidget.addWidget(self.page_6)
        self.page_8 = QtGui.QWidget()
        self.page_8.setObjectName(_fromUtf8("page_8"))
        self.label_15 = QtGui.QLabel(self.page_8)
        self.label_15.setGeometry(QtCore.QRect(160, 30, 211, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.equationStackedWidget.addWidget(self.page_8)
        self.page_10 = QtGui.QWidget()
        self.page_10.setObjectName(_fromUtf8("page_10"))
        self.label_16 = QtGui.QLabel(self.page_10)
        self.label_16.setGeometry(QtCore.QRect(110, 30, 261, 31))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.equationStackedWidget.addWidget(self.page_10)
        self.page_12 = QtGui.QWidget()
        self.page_12.setObjectName(_fromUtf8("page_12"))
        self.label_17 = QtGui.QLabel(self.page_12)
        self.label_17.setGeometry(QtCore.QRect(70, 30, 391, 41))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.equationStackedWidget.addWidget(self.page_12)
        self.page_13 = QtGui.QWidget()
        self.page_13.setObjectName(_fromUtf8("page_13"))
        self.label_18 = QtGui.QLabel(self.page_13)
        self.label_18.setGeometry(QtCore.QRect(110, 20, 291, 41))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.equationStackedWidget.addWidget(self.page_13)
        self.gridLayout.addWidget(self.equationStackedWidget, 2, 0, 1, 2)
        self.initialValuesWave = QWaveComboBox(self.tabFunction)
        self.initialValuesWave.setEnabled(False)
        self.initialValuesWave.setObjectName(_fromUtf8("initialValuesWave"))
        self.gridLayout.addWidget(self.initialValuesWave, 3, 1, 1, 1)
        self.useInitialValuesWave = QtGui.QCheckBox(self.tabFunction)
        self.useInitialValuesWave.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.useInitialValuesWave.setObjectName(_fromUtf8("useInitialValuesWave"))
        self.gridLayout.addWidget(self.useInitialValuesWave, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tabFunction, _fromUtf8(""))
        self.tabData = QtGui.QWidget()
        self.tabData.setObjectName(_fromUtf8("tabData"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tabData)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.tabData)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.tabData)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)
        self.xWave = QWaveComboBox(self.tabData)
        self.xWave.setObjectName(_fromUtf8("xWave"))
        self.gridLayout_2.addWidget(self.xWave, 1, 0, 1, 1)
        self.yWave = QWaveComboBox(self.tabData)
        self.yWave.setObjectName(_fromUtf8("yWave"))
        self.gridLayout_2.addWidget(self.yWave, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.tabData)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.dataRangeStart = QWaveStartSpinBox(self.groupBox)
        self.dataRangeStart.setObjectName(_fromUtf8("dataRangeStart"))
        self.gridLayout_3.addWidget(self.dataRangeStart, 1, 0, 1, 1)
        self.dataRangeEnd = QWaveEndSpinBox(self.groupBox)
        self.dataRangeEnd.setObjectName(_fromUtf8("dataRangeEnd"))
        self.gridLayout_3.addWidget(self.dataRangeEnd, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tabData, _fromUtf8(""))
        self.tabOutput = QtGui.QWidget()
        self.tabOutput.setObjectName(_fromUtf8("tabOutput"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tabOutput)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.outputParameters = QtGui.QGroupBox(self.tabOutput)
        self.outputParameters.setCheckable(True)
        self.outputParameters.setObjectName(_fromUtf8("outputParameters"))
        self.formLayout_2 = QtGui.QFormLayout(self.outputParameters)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_7 = QtGui.QLabel(self.outputParameters)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.parameterDestination = QtGui.QLineEdit(self.outputParameters)
        self.parameterDestination.setObjectName(_fromUtf8("parameterDestination"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.parameterDestination)
        self.saveLabels = QtGui.QCheckBox(self.outputParameters)
        self.saveLabels.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.saveLabels.setChecked(True)
        self.saveLabels.setObjectName(_fromUtf8("saveLabels"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.saveLabels)
        self.saveLabelsDestination = QtGui.QLineEdit(self.outputParameters)
        self.saveLabelsDestination.setObjectName(_fromUtf8("saveLabelsDestination"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.saveLabelsDestination)
        self.gridLayout_4.addWidget(self.outputParameters, 1, 1, 1, 1)
        self.createTable = QtGui.QCheckBox(self.tabOutput)
        self.createTable.setChecked(True)
        self.createTable.setObjectName(_fromUtf8("createTable"))
        self.gridLayout_4.addWidget(self.createTable, 0, 1, 1, 1)
        self.outputInterpolation = QtGui.QGroupBox(self.tabOutput)
        self.outputInterpolation.setCheckable(True)
        self.outputInterpolation.setObjectName(_fromUtf8("outputInterpolation"))
        self.formLayout_3 = QtGui.QFormLayout(self.outputInterpolation)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_13 = QtGui.QLabel(self.outputInterpolation)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_13)
        self.interpolationDestination = QtGui.QLineEdit(self.outputInterpolation)
        self.interpolationDestination.setObjectName(_fromUtf8("interpolationDestination"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.interpolationDestination)
        self.useWaveForInterpolation = QtGui.QGroupBox(self.outputInterpolation)
        self.useWaveForInterpolation.setCheckable(True)
        self.useWaveForInterpolation.setObjectName(_fromUtf8("useWaveForInterpolation"))
        self.formLayout_5 = QtGui.QFormLayout(self.useWaveForInterpolation)
        self.formLayout_5.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.label_8 = QtGui.QLabel(self.useWaveForInterpolation)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.label_11 = QtGui.QLabel(self.useWaveForInterpolation)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtGui.QLabel(self.useWaveForInterpolation)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_12)
        self.interpolationWaveRangeStart = QWaveStartSpinBox(self.useWaveForInterpolation)
        self.interpolationWaveRangeStart.setObjectName(_fromUtf8("interpolationWaveRangeStart"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.FieldRole, self.interpolationWaveRangeStart)
        self.interpolationWave = QWaveComboBox(self.useWaveForInterpolation)
        self.interpolationWave.setObjectName(_fromUtf8("interpolationWave"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.interpolationWave)
        self.interpolationWaveRangeEnd = QWaveEndSpinBox(self.useWaveForInterpolation)
        self.interpolationWaveRangeEnd.setObjectName(_fromUtf8("interpolationWaveRangeEnd"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.FieldRole, self.interpolationWaveRangeEnd)
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.SpanningRole, self.useWaveForInterpolation)
        self.useDomainForInterpolation = QtGui.QGroupBox(self.outputInterpolation)
        self.useDomainForInterpolation.setEnabled(True)
        self.useDomainForInterpolation.setCheckable(True)
        self.useDomainForInterpolation.setChecked(False)
        self.useDomainForInterpolation.setObjectName(_fromUtf8("useDomainForInterpolation"))
        self.formLayout_4 = QtGui.QFormLayout(self.useDomainForInterpolation)
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.interpolationCustomWaveName = QtGui.QLineEdit(self.useDomainForInterpolation)
        self.interpolationCustomWaveName.setObjectName(_fromUtf8("interpolationCustomWaveName"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.interpolationCustomWaveName)
        self.interpolationCustomLowerLimit = QtGui.QLineEdit(self.useDomainForInterpolation)
        self.interpolationCustomLowerLimit.setObjectName(_fromUtf8("interpolationCustomLowerLimit"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.interpolationCustomLowerLimit)
        self.interpolationCustomNumPoints = QtGui.QSpinBox(self.useDomainForInterpolation)
        self.interpolationCustomNumPoints.setMaximum(1000)
        self.interpolationCustomNumPoints.setProperty(_fromUtf8("value"), 100)
        self.interpolationCustomNumPoints.setObjectName(_fromUtf8("interpolationCustomNumPoints"))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.FieldRole, self.interpolationCustomNumPoints)
        self.label_20 = QtGui.QLabel(self.useDomainForInterpolation)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_20)
        self.label_22 = QtGui.QLabel(self.useDomainForInterpolation)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_22)
        self.interpolationCustomUpperLimit = QtGui.QLineEdit(self.useDomainForInterpolation)
        self.interpolationCustomUpperLimit.setObjectName(_fromUtf8("interpolationCustomUpperLimit"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.interpolationCustomUpperLimit)
        self.label_19 = QtGui.QLabel(self.useDomainForInterpolation)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_19)
        self.label_21 = QtGui.QLabel(self.useDomainForInterpolation)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_21)
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.SpanningRole, self.useDomainForInterpolation)
        self.gridLayout_4.addWidget(self.outputInterpolation, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tabOutput, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.doFitButton = QtGui.QPushButton(CurveFitting)
        self.doFitButton.setObjectName(_fromUtf8("doFitButton"))
        self.horizontalLayout.addWidget(self.doFitButton)
        self.closeButton = QtGui.QPushButton(CurveFitting)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout.addWidget(self.closeButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(CurveFitting)
        self.tabWidget.setCurrentIndex(0)
        self.function.setCurrentIndex(0)
        self.functionStackedWidget.setCurrentIndex(0)
        self.equationStackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.function, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.functionStackedWidget.setCurrentIndex)
        QtCore.QObject.connect(self.function, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.equationStackedWidget.setCurrentIndex)
        QtCore.QObject.connect(self.useInitialValuesWave, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.initialValuesWave.setEnabled)

    def retranslateUi(self, CurveFitting):
        CurveFitting.setWindowTitle(QtGui.QApplication.translate("CurveFitting", "Curve Fitting", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CurveFitting", "Function", None, QtGui.QApplication.UnicodeUTF8))
        self.function.setItemText(0, QtGui.QApplication.translate("CurveFitting", "Polynomial", None, QtGui.QApplication.UnicodeUTF8))
        self.function.setItemText(1, QtGui.QApplication.translate("CurveFitting", "Sinusoid", None, QtGui.QApplication.UnicodeUTF8))
        self.function.setItemText(2, QtGui.QApplication.translate("CurveFitting", "Power Law", None, QtGui.QApplication.UnicodeUTF8))
        self.function.setItemText(3, QtGui.QApplication.translate("CurveFitting", "Exponential", None, QtGui.QApplication.UnicodeUTF8))
        self.function.setItemText(4, QtGui.QApplication.translate("CurveFitting", "Logarithm", None, QtGui.QApplication.UnicodeUTF8))
        self.function.setItemText(5, QtGui.QApplication.translate("CurveFitting", "Gaussian", None, QtGui.QApplication.UnicodeUTF8))
        self.function.setItemText(6, QtGui.QApplication.translate("CurveFitting", "Lorentzian", None, QtGui.QApplication.UnicodeUTF8))
        self.parameterTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("CurveFitting", "Parameter", None, QtGui.QApplication.UnicodeUTF8))
        self.parameterTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("CurveFitting", "Initial Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CurveFitting", "Polynomial Degree", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("CurveFitting", "y = p0 + p1 * x + p2 * x^2 + ...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("CurveFitting", "y = p0 + p1 * Cos(2 * pi * x / p2 + p3)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("CurveFitting", "y = y0 + a * x^k", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("CurveFitting", "y = y0 + A * e^(b * x)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("CurveFitting", "y = y0 + a * log(base, x)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("CurveFitting", "y = amp * e^(-(x - mean)^2/(2 * width^2))", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("CurveFitting", "y = amp * hwhm / ((x - mean)^2 + hwhm^2)", None, QtGui.QApplication.UnicodeUTF8))
        self.useInitialValuesWave.setText(QtGui.QApplication.translate("CurveFitting", "Insert Wave for Initial Values", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFunction), QtGui.QApplication.translate("CurveFitting", "Function", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CurveFitting", "X Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CurveFitting", "Y Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("CurveFitting", "Data Range", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("CurveFitting", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("CurveFitting", "End", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabData), QtGui.QApplication.translate("CurveFitting", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.outputParameters.setTitle(QtGui.QApplication.translate("CurveFitting", "Output Parameters?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("CurveFitting", "Destination Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.saveLabels.setText(QtGui.QApplication.translate("CurveFitting", "Save Labels to Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.createTable.setText(QtGui.QApplication.translate("CurveFitting", "Create Table with Outputs", None, QtGui.QApplication.UnicodeUTF8))
        self.outputInterpolation.setTitle(QtGui.QApplication.translate("CurveFitting", "Apply fit to domain?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("CurveFitting", "Destination Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.useWaveForInterpolation.setTitle(QtGui.QApplication.translate("CurveFitting", "Use Wave for interpolation domain", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("CurveFitting", "Wave to Interpolate Over", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("CurveFitting", "Start Index", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("CurveFitting", "End Index", None, QtGui.QApplication.UnicodeUTF8))
        self.useDomainForInterpolation.setTitle(QtGui.QApplication.translate("CurveFitting", "Custom Domain", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("CurveFitting", "Upper Limit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("CurveFitting", "Wave Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("CurveFitting", "Lower Limit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("CurveFitting", "Number of points", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOutput), QtGui.QApplication.translate("CurveFitting", "Output Options", None, QtGui.QApplication.UnicodeUTF8))
        self.doFitButton.setText(QtGui.QApplication.translate("CurveFitting", "Fit Curve", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("CurveFitting", "Close", None, QtGui.QApplication.UnicodeUTF8))

from gui.QWaveLimitSpinBox import QWaveEndSpinBox, QWaveStartSpinBox
from gui.QWaveComboBox import QWaveComboBox
