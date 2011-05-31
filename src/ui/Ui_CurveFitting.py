# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_CurveFitting.ui'
#
# Created: Tue May 31 02:40:06 2011
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
        self.gridLayout.addWidget(self.function, 0, 1, 1, 1)
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
        self.gridLayout.addWidget(self.functionStackedWidget, 1, 0, 1, 2)
        self.coefficientTable = QtGui.QTableWidget(self.tabFunction)
        self.coefficientTable.setEnabled(False)
        self.coefficientTable.setObjectName(_fromUtf8("coefficientTable"))
        self.coefficientTable.setColumnCount(1)
        self.coefficientTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.coefficientTable.setHorizontalHeaderItem(0, item)
        self.gridLayout.addWidget(self.coefficientTable, 3, 0, 1, 2)
        self.label_14 = QtGui.QLabel(self.tabFunction)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 2, 0, 1, 2)
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
        self.xWave = QtGui.QComboBox(self.tabData)
        self.xWave.setObjectName(_fromUtf8("xWave"))
        self.gridLayout_2.addWidget(self.xWave, 1, 0, 1, 1)
        self.yWave = QtGui.QComboBox(self.tabData)
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
        self.outputCoefficients = QtGui.QGroupBox(self.tabOutput)
        self.outputCoefficients.setCheckable(True)
        self.outputCoefficients.setObjectName(_fromUtf8("outputCoefficients"))
        self.formLayout_2 = QtGui.QFormLayout(self.outputCoefficients)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_7 = QtGui.QLabel(self.outputCoefficients)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.saveLabels = QtGui.QCheckBox(self.outputCoefficients)
        self.saveLabels.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.saveLabels.setChecked(True)
        self.saveLabels.setObjectName(_fromUtf8("saveLabels"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.saveLabels)
        self.saveFitParameters = QtGui.QCheckBox(self.outputCoefficients)
        self.saveFitParameters.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.saveFitParameters.setObjectName(_fromUtf8("saveFitParameters"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.saveFitParameters)
        self.coefficientDestination = QtGui.QLineEdit(self.outputCoefficients)
        self.coefficientDestination.setObjectName(_fromUtf8("coefficientDestination"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.coefficientDestination)
        self.saveLabelsDestination = QtGui.QLineEdit(self.outputCoefficients)
        self.saveLabelsDestination.setObjectName(_fromUtf8("saveLabelsDestination"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.saveLabelsDestination)
        self.gridLayout_4.addWidget(self.outputCoefficients, 1, 1, 1, 1)
        self.outputInterpolation = QtGui.QGroupBox(self.tabOutput)
        self.outputInterpolation.setCheckable(True)
        self.outputInterpolation.setObjectName(_fromUtf8("outputInterpolation"))
        self.formLayout_3 = QtGui.QFormLayout(self.outputInterpolation)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_8 = QtGui.QLabel(self.outputInterpolation)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
        self.interpolationDomain = QtGui.QComboBox(self.outputInterpolation)
        self.interpolationDomain.setObjectName(_fromUtf8("interpolationDomain"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.interpolationDomain)
        self.groupBox_4 = QtGui.QGroupBox(self.outputInterpolation)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.interpolationRangeStart = QWaveStartSpinBox(self.groupBox_4)
        self.interpolationRangeStart.setObjectName(_fromUtf8("interpolationRangeStart"))
        self.gridLayout_5.addWidget(self.interpolationRangeStart, 1, 0, 1, 1)
        self.interpolationRangeEnd = QWaveEndSpinBox(self.groupBox_4)
        self.interpolationRangeEnd.setObjectName(_fromUtf8("interpolationRangeEnd"))
        self.gridLayout_5.addWidget(self.interpolationRangeEnd, 1, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox_4)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_4)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_5.addWidget(self.label_12, 0, 1, 1, 1)
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.SpanningRole, self.groupBox_4)
        self.label_13 = QtGui.QLabel(self.outputInterpolation)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_13)
        self.interpolationDestination = QtGui.QLineEdit(self.outputInterpolation)
        self.interpolationDestination.setObjectName(_fromUtf8("interpolationDestination"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.interpolationDestination)
        self.gridLayout_4.addWidget(self.outputInterpolation, 1, 2, 1, 1)
        self.createTable = QtGui.QCheckBox(self.tabOutput)
        self.createTable.setChecked(True)
        self.createTable.setObjectName(_fromUtf8("createTable"))
        self.gridLayout_4.addWidget(self.createTable, 0, 1, 1, 1)
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
        self.functionStackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.function, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.functionStackedWidget.setCurrentIndex)

    def retranslateUi(self, CurveFitting):
        CurveFitting.setWindowTitle(QtGui.QApplication.translate("CurveFitting", "Curve Fitting", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CurveFitting", "Function", None, QtGui.QApplication.UnicodeUTF8))
        self.function.setItemText(0, QtGui.QApplication.translate("CurveFitting", "Polynomial", None, QtGui.QApplication.UnicodeUTF8))
        self.function.setItemText(1, QtGui.QApplication.translate("CurveFitting", "test", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CurveFitting", "Number of Terms", None, QtGui.QApplication.UnicodeUTF8))
        self.coefficientTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("CurveFitting", "Coefficients", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("CurveFitting", "Display the function equation here", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFunction), QtGui.QApplication.translate("CurveFitting", "Function", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CurveFitting", "X Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CurveFitting", "Y Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("CurveFitting", "Data Range", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("CurveFitting", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("CurveFitting", "End", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabData), QtGui.QApplication.translate("CurveFitting", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.outputCoefficients.setTitle(QtGui.QApplication.translate("CurveFitting", "Output Coefficients?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("CurveFitting", "Destination Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.saveLabels.setText(QtGui.QApplication.translate("CurveFitting", "Save Labels to Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.saveFitParameters.setText(QtGui.QApplication.translate("CurveFitting", "Include fit parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.outputInterpolation.setTitle(QtGui.QApplication.translate("CurveFitting", "Apply fit to domain?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("CurveFitting", "Wave to Interpolate Over", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("CurveFitting", "Interpolation Range", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("CurveFitting", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("CurveFitting", "End", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("CurveFitting", "Destination Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.createTable.setText(QtGui.QApplication.translate("CurveFitting", "Create Table with Outputs", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOutput), QtGui.QApplication.translate("CurveFitting", "Output Options", None, QtGui.QApplication.UnicodeUTF8))
        self.doFitButton.setText(QtGui.QApplication.translate("CurveFitting", "Fit Curve", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("CurveFitting", "Close", None, QtGui.QApplication.UnicodeUTF8))

from gui.QWaveLimitSpinBox import QWaveEndSpinBox, QWaveStartSpinBox
