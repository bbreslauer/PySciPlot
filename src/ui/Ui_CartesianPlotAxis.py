# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_CartesianPlotAxis.ui'
#
# Created: Tue Sep 27 01:04:57 2011
#      by: pyside-uic 0.2.13 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CartesianPlotAxis(object):
    def setupUi(self, CartesianPlotAxis):
        CartesianPlotAxis.setObjectName("CartesianPlotAxis")
        CartesianPlotAxis.resize(578, 357)
        self.gridLayout_4 = QtGui.QGridLayout(CartesianPlotAxis)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.visible = QtGui.QGroupBox(CartesianPlotAxis)
        self.visible.setMinimumSize(QtCore.QSize(185, 0))
        self.visible.setCheckable(True)
        self.visible.setObjectName("visible")
        self.gridLayout_5 = QtGui.QGridLayout(self.visible)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtGui.QLineEdit(self.visible)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 1, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.visible)
        self.label_19.setObjectName("label_19")
        self.gridLayout_5.addWidget(self.label_19, 1, 0, 1, 1)
        self.labelFont = QTextOptionsButton(self.visible)
        self.labelFont.setObjectName("labelFont")
        self.gridLayout_5.addWidget(self.labelFont, 1, 2, 1, 1)
        self.slaveAxisToOther = QtGui.QCheckBox(self.visible)
        self.slaveAxisToOther.setObjectName("slaveAxisToOther")
        self.gridLayout_5.addWidget(self.slaveAxisToOther, 0, 0, 1, 2)
        self.slavedTo = QtGui.QComboBox(self.visible)
        self.slavedTo.setEnabled(False)
        self.slavedTo.setObjectName("slavedTo")
        self.slavedTo.addItem("")
        self.slavedTo.addItem("")
        self.slavedTo.addItem("")
        self.slavedTo.addItem("")
        self.gridLayout_5.addWidget(self.slavedTo, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.visible, 0, 0, 1, 1)
        self.majorTicksVisible = QtGui.QGroupBox(CartesianPlotAxis)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.majorTicksVisible.sizePolicy().hasHeightForWidth())
        self.majorTicksVisible.setSizePolicy(sizePolicy)
        self.majorTicksVisible.setCheckable(True)
        self.majorTicksVisible.setObjectName("majorTicksVisible")
        self.gridLayout_7 = QtGui.QGridLayout(self.majorTicksVisible)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setHorizontalSpacing(3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_2 = QtGui.QGroupBox(self.majorTicksVisible)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.majorTicksLocationsStackedWidget = QtGui.QStackedWidget(self.groupBox_2)
        self.majorTicksLocationsStackedWidget.setObjectName("majorTicksLocationsStackedWidget")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_6 = QtGui.QGridLayout(self.page)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.useMajorTicksAnchor = QtGui.QCheckBox(self.page)
        self.useMajorTicksAnchor.setEnabled(False)
        self.useMajorTicksAnchor.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.useMajorTicksAnchor.setObjectName("useMajorTicksAnchor")
        self.gridLayout_6.addWidget(self.useMajorTicksAnchor, 0, 0, 1, 1)
        self.majorTicksAnchor = QtGui.QLineEdit(self.page)
        self.majorTicksAnchor.setEnabled(False)
        self.majorTicksAnchor.setObjectName("majorTicksAnchor")
        self.gridLayout_6.addWidget(self.majorTicksAnchor, 0, 1, 1, 1)
        self.useMajorTicksSpacing = QtGui.QRadioButton(self.page)
        self.useMajorTicksSpacing.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.useMajorTicksSpacing.setObjectName("useMajorTicksSpacing")
        self.gridLayout_6.addWidget(self.useMajorTicksSpacing, 1, 0, 1, 1)
        self.majorTicksSpacing = QtGui.QLineEdit(self.page)
        self.majorTicksSpacing.setEnabled(False)
        self.majorTicksSpacing.setObjectName("majorTicksSpacing")
        self.gridLayout_6.addWidget(self.majorTicksSpacing, 1, 1, 1, 1)
        self.useMajorTicksNumber = QtGui.QRadioButton(self.page)
        self.useMajorTicksNumber.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.useMajorTicksNumber.setChecked(True)
        self.useMajorTicksNumber.setObjectName("useMajorTicksNumber")
        self.gridLayout_6.addWidget(self.useMajorTicksNumber, 3, 0, 1, 1)
        self.majorTicksNumber = QtGui.QSpinBox(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.majorTicksNumber.sizePolicy().hasHeightForWidth())
        self.majorTicksNumber.setSizePolicy(sizePolicy)
        self.majorTicksNumber.setMinimum(2)
        self.majorTicksNumber.setProperty("value", 5)
        self.majorTicksNumber.setObjectName("majorTicksNumber")
        self.gridLayout_6.addWidget(self.majorTicksNumber, 3, 1, 1, 1)
        self.useMajorTicksWaveValues = QtGui.QRadioButton(self.page)
        self.useMajorTicksWaveValues.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.useMajorTicksWaveValues.setObjectName("useMajorTicksWaveValues")
        self.gridLayout_6.addWidget(self.useMajorTicksWaveValues, 4, 0, 1, 1)
        self.majorTicksWaveValues = QtGui.QComboBox(self.page)
        self.majorTicksWaveValues.setEnabled(False)
        self.majorTicksWaveValues.setObjectName("majorTicksWaveValues")
        self.gridLayout_6.addWidget(self.majorTicksWaveValues, 4, 1, 1, 1)
        self.majorTicksLocationsStackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_8 = QtGui.QGridLayout(self.page_2)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_2 = QtGui.QLabel(self.page_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_8.addWidget(self.label_2, 0, 0, 1, 1)
        self.majorTicksLogBase = QtGui.QLineEdit(self.page_2)
        self.majorTicksLogBase.setObjectName("majorTicksLogBase")
        self.gridLayout_8.addWidget(self.majorTicksLogBase, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.page_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 1, 0, 1, 1)
        self.majorTicksLogLocations = QtGui.QLineEdit(self.page_2)
        self.majorTicksLogLocations.setObjectName("majorTicksLogLocations")
        self.gridLayout_8.addWidget(self.majorTicksLogLocations, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem, 2, 0, 1, 1)
        self.majorTicksLocationsStackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.majorTicksLocationsStackedWidget, 0, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 0, 3, 1, 1)
        self.line_2 = QtGui.QFrame(self.majorTicksVisible)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_7.addWidget(self.line_2, 0, 4, 1, 1)
        self.majorTicksLabelVisible = QtGui.QGroupBox(self.majorTicksVisible)
        self.majorTicksLabelVisible.setAlignment(QtCore.Qt.AlignCenter)
        self.majorTicksLabelVisible.setFlat(True)
        self.majorTicksLabelVisible.setCheckable(True)
        self.majorTicksLabelVisible.setObjectName("majorTicksLabelVisible")
        self.gridLayout_2 = QtGui.QGridLayout(self.majorTicksLabelVisible)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtGui.QLabel(self.majorTicksLabelVisible)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 2)
        self.label_31 = QtGui.QLabel(self.majorTicksLabelVisible)
        self.label_31.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 4, 0, 1, 1)
        self.majorTicksLabelUseNumeric = QtGui.QRadioButton(self.majorTicksLabelVisible)
        self.majorTicksLabelUseNumeric.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.majorTicksLabelUseNumeric.setChecked(True)
        self.majorTicksLabelUseNumeric.setObjectName("majorTicksLabelUseNumeric")
        self.gridLayout_2.addWidget(self.majorTicksLabelUseNumeric, 0, 0, 1, 2)
        self.majorTicksLabelUseWave = QtGui.QRadioButton(self.majorTicksLabelVisible)
        self.majorTicksLabelUseWave.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.majorTicksLabelUseWave.setObjectName("majorTicksLabelUseWave")
        self.gridLayout_2.addWidget(self.majorTicksLabelUseWave, 1, 0, 1, 2)
        self.majorTicksDirection = QtGui.QComboBox(self.majorTicksLabelVisible)
        self.majorTicksDirection.setObjectName("majorTicksDirection")
        self.majorTicksDirection.addItem("")
        self.majorTicksDirection.addItem("")
        self.majorTicksDirection.addItem("")
        self.gridLayout_2.addWidget(self.majorTicksDirection, 4, 1, 1, 1)
        self.majorTicksLength = QtGui.QSpinBox(self.majorTicksLabelVisible)
        self.majorTicksLength.setProperty("value", 4)
        self.majorTicksLength.setObjectName("majorTicksLength")
        self.gridLayout_2.addWidget(self.majorTicksLength, 5, 1, 1, 1)
        self.label_33 = QtGui.QLabel(self.majorTicksLabelVisible)
        self.label_33.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout_2.addWidget(self.label_33, 5, 0, 1, 1)
        self.label_34 = QtGui.QLabel(self.majorTicksLabelVisible)
        self.label_34.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout_2.addWidget(self.label_34, 5, 2, 1, 1)
        self.majorTicksWidth = QtGui.QSpinBox(self.majorTicksLabelVisible)
        self.majorTicksWidth.setProperty("value", 1)
        self.majorTicksWidth.setObjectName("majorTicksWidth")
        self.gridLayout_2.addWidget(self.majorTicksWidth, 5, 3, 1, 1)
        self.majorTicksColor = QColorButton(self.majorTicksLabelVisible)
        self.majorTicksColor.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.majorTicksColor.setObjectName("majorTicksColor")
        self.gridLayout_2.addWidget(self.majorTicksColor, 4, 3, 1, 1)
        self.majorTicksLabelNumericFormat = QtGui.QLineEdit(self.majorTicksLabelVisible)
        self.majorTicksLabelNumericFormat.setObjectName("majorTicksLabelNumericFormat")
        self.gridLayout_2.addWidget(self.majorTicksLabelNumericFormat, 0, 2, 1, 2)
        self.majorTicksLabelWave = QtGui.QComboBox(self.majorTicksLabelVisible)
        self.majorTicksLabelWave.setEnabled(False)
        self.majorTicksLabelWave.setObjectName("majorTicksLabelWave")
        self.gridLayout_2.addWidget(self.majorTicksLabelWave, 1, 2, 1, 2)
        self.label_32 = QtGui.QLabel(self.majorTicksLabelVisible)
        self.label_32.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout_2.addWidget(self.label_32, 4, 2, 1, 1)
        self.majorTicksLabelFont = QTextOptionsButton(self.majorTicksLabelVisible)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.majorTicksLabelFont.sizePolicy().hasHeightForWidth())
        self.majorTicksLabelFont.setSizePolicy(sizePolicy)
        self.majorTicksLabelFont.setMinimumSize(QtCore.QSize(5, 0))
        self.majorTicksLabelFont.setObjectName("majorTicksLabelFont")
        self.gridLayout_2.addWidget(self.majorTicksLabelFont, 2, 2, 1, 2)
        self.gridLayout_7.addWidget(self.majorTicksLabelVisible, 0, 5, 1, 1)
        self.gridLayout_7.setRowStretch(0, 1)
        self.gridLayout_4.addWidget(self.majorTicksVisible, 1, 0, 1, 2)
        self.minorTicksVisible = QtGui.QGroupBox(CartesianPlotAxis)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minorTicksVisible.sizePolicy().hasHeightForWidth())
        self.minorTicksVisible.setSizePolicy(sizePolicy)
        self.minorTicksVisible.setCheckable(True)
        self.minorTicksVisible.setObjectName("minorTicksVisible")
        self.gridLayout_3 = QtGui.QGridLayout(self.minorTicksVisible)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.minorTicksLocationsStackedWidget = QtGui.QStackedWidget(self.minorTicksVisible)
        self.minorTicksLocationsStackedWidget.setObjectName("minorTicksLocationsStackedWidget")
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout = QtGui.QVBoxLayout(self.page_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_26 = QtGui.QLabel(self.page_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.verticalLayout.addWidget(self.label_26)
        self.minorTicksNumber = QtGui.QSpinBox(self.page_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minorTicksNumber.sizePolicy().hasHeightForWidth())
        self.minorTicksNumber.setSizePolicy(sizePolicy)
        self.minorTicksNumber.setMaximumSize(QtCore.QSize(50, 16777215))
        self.minorTicksNumber.setMinimum(1)
        self.minorTicksNumber.setProperty("value", 5)
        self.minorTicksNumber.setObjectName("minorTicksNumber")
        self.verticalLayout.addWidget(self.minorTicksNumber)
        self.minorTicksLocationsStackedWidget.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtGui.QLabel(self.page_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.minorTicksLogLocations = QtGui.QLineEdit(self.page_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minorTicksLogLocations.sizePolicy().hasHeightForWidth())
        self.minorTicksLogLocations.setSizePolicy(sizePolicy)
        self.minorTicksLogLocations.setObjectName("minorTicksLogLocations")
        self.verticalLayout_2.addWidget(self.minorTicksLogLocations)
        self.minorTicksLocationsStackedWidget.addWidget(self.page_4)
        self.gridLayout_3.addWidget(self.minorTicksLocationsStackedWidget, 0, 0, 2, 1)
        self.label_24 = QtGui.QLabel(self.minorTicksVisible)
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 0, 2, 1, 1)
        self.label_27 = QtGui.QLabel(self.minorTicksVisible)
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 0, 3, 1, 1)
        self.label_28 = QtGui.QLabel(self.minorTicksVisible)
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 0, 4, 1, 1)
        self.minorTicksDirection = QtGui.QComboBox(self.minorTicksVisible)
        self.minorTicksDirection.setMaximumSize(QtCore.QSize(100, 16777215))
        self.minorTicksDirection.setObjectName("minorTicksDirection")
        self.minorTicksDirection.addItem("")
        self.minorTicksDirection.addItem("")
        self.minorTicksDirection.addItem("")
        self.gridLayout_3.addWidget(self.minorTicksDirection, 1, 1, 1, 1)
        self.minorTicksColor = QColorButton(self.minorTicksVisible)
        self.minorTicksColor.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.minorTicksColor.setObjectName("minorTicksColor")
        self.gridLayout_3.addWidget(self.minorTicksColor, 1, 2, 1, 1)
        self.minorTicksLength = QtGui.QSpinBox(self.minorTicksVisible)
        self.minorTicksLength.setMaximumSize(QtCore.QSize(50, 16777215))
        self.minorTicksLength.setProperty("value", 2)
        self.minorTicksLength.setObjectName("minorTicksLength")
        self.gridLayout_3.addWidget(self.minorTicksLength, 1, 3, 1, 1)
        self.minorTicksWidth = QtGui.QSpinBox(self.minorTicksVisible)
        self.minorTicksWidth.setMaximumSize(QtCore.QSize(50, 16777215))
        self.minorTicksWidth.setProperty("value", 1)
        self.minorTicksWidth.setObjectName("minorTicksWidth")
        self.gridLayout_3.addWidget(self.minorTicksWidth, 1, 4, 1, 1)
        self.label_23 = QtGui.QLabel(self.minorTicksVisible)
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 0, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setColumnStretch(2, 2)
        self.gridLayout_3.setColumnStretch(3, 1)
        self.gridLayout_3.setColumnStretch(4, 1)
        self.gridLayout_4.addWidget(self.minorTicksVisible, 2, 0, 1, 2)
        self.scaleGroupBox = QtGui.QGroupBox(CartesianPlotAxis)
        self.scaleGroupBox.setObjectName("scaleGroupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scaleGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.autoscale = QtGui.QCheckBox(self.scaleGroupBox)
        self.autoscale.setChecked(True)
        self.autoscale.setObjectName("autoscale")
        self.horizontalLayout.addWidget(self.autoscale)
        self.label_21 = QtGui.QLabel(self.scaleGroupBox)
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout.addWidget(self.label_21)
        self.scaleType = QtGui.QComboBox(self.scaleGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scaleType.sizePolicy().hasHeightForWidth())
        self.scaleType.setSizePolicy(sizePolicy)
        self.scaleType.setObjectName("scaleType")
        self.scaleType.addItem("")
        self.scaleType.addItem("")
        self.scaleType.addItem("")
        self.horizontalLayout.addWidget(self.scaleType)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_20 = QtGui.QLabel(self.scaleGroupBox)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_2.addWidget(self.label_20)
        self.minimum = QtGui.QLineEdit(self.scaleGroupBox)
        self.minimum.setEnabled(False)
        self.minimum.setObjectName("minimum")
        self.horizontalLayout_2.addWidget(self.minimum)
        self.label_22 = QtGui.QLabel(self.scaleGroupBox)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_2.addWidget(self.label_22)
        self.maximum = QtGui.QLineEdit(self.scaleGroupBox)
        self.maximum.setEnabled(False)
        self.maximum.setObjectName("maximum")
        self.horizontalLayout_2.addWidget(self.maximum)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout_4.addWidget(self.scaleGroupBox, 0, 1, 1, 1)
        self.storedSettingsButton = QStoredSettingsButton(CartesianPlotAxis)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.storedSettingsButton.sizePolicy().hasHeightForWidth())
        self.storedSettingsButton.setSizePolicy(sizePolicy)
        self.storedSettingsButton.setMaximumSize(QtCore.QSize(26, 16777215))
        self.storedSettingsButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.storedSettingsButton.setArrowType(QtCore.Qt.LeftArrow)
        self.storedSettingsButton.setObjectName("storedSettingsButton")
        self.gridLayout_4.addWidget(self.storedSettingsButton, 0, 2, 4, 1)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.gridLayout_4.setColumnStretch(2, 1)

        self.retranslateUi(CartesianPlotAxis)
        self.majorTicksLocationsStackedWidget.setCurrentIndex(0)
        self.minorTicksLocationsStackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.storedSettingsButton, QtCore.SIGNAL("clicked()"), self.storedSettingsButton.toggleWidget)
        QtCore.QObject.connect(self.labelFont, QtCore.SIGNAL("clicked()"), self.labelFont.showTextOptionsWidget)
        QtCore.QObject.connect(self.autoscale, QtCore.SIGNAL("toggled(bool)"), self.minimum.setDisabled)
        QtCore.QObject.connect(self.autoscale, QtCore.SIGNAL("toggled(bool)"), self.maximum.setDisabled)
        QtCore.QObject.connect(self.majorTicksLabelFont, QtCore.SIGNAL("clicked()"), self.majorTicksLabelFont.showTextOptionsWidget)
        QtCore.QObject.connect(self.majorTicksColor, QtCore.SIGNAL("clicked()"), self.majorTicksColor.createColorDialog)
        QtCore.QObject.connect(self.minorTicksColor, QtCore.SIGNAL("clicked()"), self.minorTicksColor.createColorDialog)
        QtCore.QObject.connect(self.useMajorTicksSpacing, QtCore.SIGNAL("toggled(bool)"), self.majorTicksSpacing.setEnabled)
        QtCore.QObject.connect(self.useMajorTicksNumber, QtCore.SIGNAL("toggled(bool)"), self.majorTicksNumber.setEnabled)
        QtCore.QObject.connect(self.majorTicksVisible, QtCore.SIGNAL("toggled(bool)"), self.minorTicksVisible.setEnabled)
        QtCore.QObject.connect(self.useMajorTicksAnchor, QtCore.SIGNAL("toggled(bool)"), self.majorTicksAnchor.setEnabled)
        QtCore.QObject.connect(self.majorTicksLabelUseNumeric, QtCore.SIGNAL("toggled(bool)"), self.majorTicksLabelNumericFormat.setEnabled)
        QtCore.QObject.connect(self.majorTicksLabelUseWave, QtCore.SIGNAL("toggled(bool)"), self.majorTicksLabelWave.setEnabled)
        QtCore.QObject.connect(self.useMajorTicksWaveValues, QtCore.SIGNAL("toggled(bool)"), self.majorTicksWaveValues.setEnabled)
        QtCore.QObject.connect(self.scaleType, QtCore.SIGNAL("currentIndexChanged(QString)"), CartesianPlotAxis.changeScaleType)
        QtCore.QObject.connect(self.useMajorTicksWaveValues, QtCore.SIGNAL("toggled(bool)"), CartesianPlotAxis.disableAnchorToValue)
        QtCore.QObject.connect(self.useMajorTicksNumber, QtCore.SIGNAL("toggled(bool)"), CartesianPlotAxis.disableAnchorToValue)
        QtCore.QObject.connect(self.useMajorTicksSpacing, QtCore.SIGNAL("toggled(bool)"), CartesianPlotAxis.enableAnchorToValue)
        QtCore.QObject.connect(self.slaveAxisToOther, QtCore.SIGNAL("toggled(bool)"), self.slavedTo.setEnabled)
        QtCore.QObject.connect(self.slaveAxisToOther, QtCore.SIGNAL("toggled(bool)"), self.scaleGroupBox.setDisabled)
        QtCore.QObject.connect(self.visible, QtCore.SIGNAL("toggled(bool)"), CartesianPlotAxis.setAxisVisible)
        CartesianPlotAxis.setTabOrder(self.label, self.majorTicksVisible)
        CartesianPlotAxis.setTabOrder(self.majorTicksVisible, self.useMajorTicksAnchor)
        CartesianPlotAxis.setTabOrder(self.useMajorTicksAnchor, self.majorTicksAnchor)
        CartesianPlotAxis.setTabOrder(self.majorTicksAnchor, self.useMajorTicksSpacing)
        CartesianPlotAxis.setTabOrder(self.useMajorTicksSpacing, self.majorTicksSpacing)
        CartesianPlotAxis.setTabOrder(self.majorTicksSpacing, self.useMajorTicksNumber)
        CartesianPlotAxis.setTabOrder(self.useMajorTicksNumber, self.majorTicksNumber)
        CartesianPlotAxis.setTabOrder(self.majorTicksNumber, self.useMajorTicksWaveValues)
        CartesianPlotAxis.setTabOrder(self.useMajorTicksWaveValues, self.majorTicksWaveValues)
        CartesianPlotAxis.setTabOrder(self.majorTicksWaveValues, self.majorTicksLabelVisible)
        CartesianPlotAxis.setTabOrder(self.majorTicksLabelVisible, self.majorTicksLabelUseNumeric)
        CartesianPlotAxis.setTabOrder(self.majorTicksLabelUseNumeric, self.majorTicksLabelNumericFormat)
        CartesianPlotAxis.setTabOrder(self.majorTicksLabelNumericFormat, self.majorTicksLabelUseWave)
        CartesianPlotAxis.setTabOrder(self.majorTicksLabelUseWave, self.majorTicksLabelWave)
        CartesianPlotAxis.setTabOrder(self.majorTicksLabelWave, self.majorTicksLabelFont)
        CartesianPlotAxis.setTabOrder(self.majorTicksLabelFont, self.majorTicksDirection)
        CartesianPlotAxis.setTabOrder(self.majorTicksDirection, self.majorTicksColor)
        CartesianPlotAxis.setTabOrder(self.majorTicksColor, self.majorTicksLength)
        CartesianPlotAxis.setTabOrder(self.majorTicksLength, self.majorTicksWidth)
        CartesianPlotAxis.setTabOrder(self.majorTicksWidth, self.minorTicksVisible)
        CartesianPlotAxis.setTabOrder(self.minorTicksVisible, self.minorTicksNumber)
        CartesianPlotAxis.setTabOrder(self.minorTicksNumber, self.minorTicksDirection)
        CartesianPlotAxis.setTabOrder(self.minorTicksDirection, self.minorTicksColor)
        CartesianPlotAxis.setTabOrder(self.minorTicksColor, self.minorTicksLength)
        CartesianPlotAxis.setTabOrder(self.minorTicksLength, self.minorTicksWidth)
        CartesianPlotAxis.setTabOrder(self.minorTicksWidth, self.storedSettingsButton)
        CartesianPlotAxis.setTabOrder(self.storedSettingsButton, self.majorTicksLogLocations)
        CartesianPlotAxis.setTabOrder(self.majorTicksLogLocations, self.majorTicksLogBase)
        CartesianPlotAxis.setTabOrder(self.majorTicksLogBase, self.minorTicksLogLocations)

    def retranslateUi(self, CartesianPlotAxis):
        CartesianPlotAxis.setWindowTitle(QtGui.QApplication.translate("CartesianPlotAxis", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.visible.setTitle(QtGui.QApplication.translate("CartesianPlotAxis", "Axis Visible", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Label", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFont.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Label Font", None, QtGui.QApplication.UnicodeUTF8))
        self.slaveAxisToOther.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Mirror other Axis", None, QtGui.QApplication.UnicodeUTF8))
        self.slavedTo.setItemText(0, QtGui.QApplication.translate("CartesianPlotAxis", "bottom", None, QtGui.QApplication.UnicodeUTF8))
        self.slavedTo.setItemText(1, QtGui.QApplication.translate("CartesianPlotAxis", "left", None, QtGui.QApplication.UnicodeUTF8))
        self.slavedTo.setItemText(2, QtGui.QApplication.translate("CartesianPlotAxis", "top", None, QtGui.QApplication.UnicodeUTF8))
        self.slavedTo.setItemText(3, QtGui.QApplication.translate("CartesianPlotAxis", "right", None, QtGui.QApplication.UnicodeUTF8))
        self.majorTicksVisible.setTitle(QtGui.QApplication.translate("CartesianPlotAxis", "Major Ticks", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("CartesianPlotAxis", "Locations", None, QtGui.QApplication.UnicodeUTF8))
        self.useMajorTicksAnchor.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Anchor to value", None, QtGui.QApplication.UnicodeUTF8))
        self.majorTicksAnchor.setText(QtGui.QApplication.translate("CartesianPlotAxis", "0.00", None, QtGui.QApplication.UnicodeUTF8))
        self.useMajorTicksSpacing.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Spacing between", None, QtGui.QApplication.UnicodeUTF8))
        self.majorTicksSpacing.setText(QtGui.QApplication.translate("CartesianPlotAxis", "2.00", None, QtGui.QApplication.UnicodeUTF8))
        self.useMajorTicksNumber.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Number of", None, QtGui.QApplication.UnicodeUTF8))
        self.useMajorTicksWaveValues.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Wave values", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Base", None, QtGui.QApplication.UnicodeUTF8))
        self.majorTicksLogBase.setText(QtGui.QApplication.translate("CartesianPlotAxis", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Tick Locations", None, QtGui.QApplication.UnicodeUTF8))
        self.majorTicksLogLocations.setText(QtGui.QApplication.translate("CartesianPlotAxis", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.majorTicksLabelVisible.setTitle(QtGui.QApplication.translate("CartesianPlotAxis", "Labels", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Tick Label", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Direction", None, QtGui.QApplication.UnicodeUTF8))
        self.majorTicksLabelUseNumeric.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Numeric Labels", None, QtGui.QApplication.UnicodeUTF8))
        self.majorTicksLabelUseWave.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Wave-based Labels", None, QtGui.QApplication.UnicodeUTF8))
        self.majorTicksDirection.setItemText(0, QtGui.QApplication.translate("CartesianPlotAxis", "in", None, QtGui.QApplication.UnicodeUTF8))
        self.majorTicksDirection.setItemText(1, QtGui.QApplication.translate("CartesianPlotAxis", "out", None, QtGui.QApplication.UnicodeUTF8))
        self.majorTicksDirection.setItemText(2, QtGui.QApplication.translate("CartesianPlotAxis", "both", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.majorTicksColor.setText(QtGui.QApplication.translate("CartesianPlotAxis", "(0,0,0,255)", None, QtGui.QApplication.UnicodeUTF8))
        self.majorTicksLabelNumericFormat.setText(QtGui.QApplication.translate("CartesianPlotAxis", "%.2g", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.majorTicksLabelFont.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Font", None, QtGui.QApplication.UnicodeUTF8))
        self.minorTicksVisible.setTitle(QtGui.QApplication.translate("CartesianPlotAxis", "Minor Ticks", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Number", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Tick Locations", None, QtGui.QApplication.UnicodeUTF8))
        self.minorTicksLogLocations.setText(QtGui.QApplication.translate("CartesianPlotAxis", "1,2,3,4,5,6,7,8,9", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.minorTicksDirection.setItemText(0, QtGui.QApplication.translate("CartesianPlotAxis", "in", None, QtGui.QApplication.UnicodeUTF8))
        self.minorTicksDirection.setItemText(1, QtGui.QApplication.translate("CartesianPlotAxis", "out", None, QtGui.QApplication.UnicodeUTF8))
        self.minorTicksDirection.setItemText(2, QtGui.QApplication.translate("CartesianPlotAxis", "both", None, QtGui.QApplication.UnicodeUTF8))
        self.minorTicksColor.setText(QtGui.QApplication.translate("CartesianPlotAxis", "(0,0,0,255)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Direction", None, QtGui.QApplication.UnicodeUTF8))
        self.scaleGroupBox.setTitle(QtGui.QApplication.translate("CartesianPlotAxis", "Scale", None, QtGui.QApplication.UnicodeUTF8))
        self.autoscale.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Autoscale?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.scaleType.setItemText(0, QtGui.QApplication.translate("CartesianPlotAxis", "Linear", None, QtGui.QApplication.UnicodeUTF8))
        self.scaleType.setItemText(1, QtGui.QApplication.translate("CartesianPlotAxis", "Logarithmic", None, QtGui.QApplication.UnicodeUTF8))
        self.scaleType.setItemText(2, QtGui.QApplication.translate("CartesianPlotAxis", "Symmetric Log", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Minimum", None, QtGui.QApplication.UnicodeUTF8))
        self.minimum.setText(QtGui.QApplication.translate("CartesianPlotAxis", "-10.00", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("CartesianPlotAxis", "Maximum", None, QtGui.QApplication.UnicodeUTF8))
        self.maximum.setText(QtGui.QApplication.translate("CartesianPlotAxis", "10.00", None, QtGui.QApplication.UnicodeUTF8))
        self.storedSettingsButton.setText(QtGui.QApplication.translate("CartesianPlotAxis", "S\n"
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

from gui.QTextOptionsButton import QTextOptionsButton
from gui.QColorButton import QColorButton
from gui.QStoredSettingsButton import QStoredSettingsButton
