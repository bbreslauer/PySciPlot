# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_TextOptionsWidget.ui'
#
# Created: Fri May 27 16:40:10 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TextOptionsWidget(object):
    def setupUi(self, TextOptionsWidget):
        TextOptionsWidget.setObjectName(_fromUtf8("TextOptionsWidget"))
        TextOptionsWidget.resize(543, 477)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TextOptionsWidget.sizePolicy().hasHeightForWidth())
        TextOptionsWidget.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(TextOptionsWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttons = QtGui.QDialogButtonBox(TextOptionsWidget)
        self.buttons.setOrientation(QtCore.Qt.Horizontal)
        self.buttons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Reset)
        self.buttons.setCenterButtons(True)
        self.buttons.setObjectName(_fromUtf8("buttons"))
        self.gridLayout.addWidget(self.buttons, 15, 1, 1, 4)
        self.groupBox = QtGui.QGroupBox(TextOptionsWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.name = QtGui.QListWidget(self.groupBox)
        self.name.setMinimumSize(QtCore.QSize(175, 0))
        self.name.setObjectName(_fromUtf8("name"))
        self.gridLayout_2.addWidget(self.name, 0, 0, 11, 1)
        self.gridLayout.addWidget(self.groupBox, 5, 1, 2, 1)
        self.groupBox_2 = QtGui.QGroupBox(TextOptionsWidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.color = QColorButton(self.groupBox_2)
        self.color.setMinimumSize(QtCore.QSize(60, 0))
        self.color.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
""))
        self.color.setObjectName(_fromUtf8("color"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.color)
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_7)
        self.backgroundcolor = QColorButton(self.groupBox_2)
        self.backgroundcolor.setMinimumSize(QtCore.QSize(60, 0))
        self.backgroundcolor.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.backgroundcolor.setObjectName(_fromUtf8("backgroundcolor"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.backgroundcolor)
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setMinimumSize(QtCore.QSize(0, 0))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_8)
        self.horizontalalignment = QtGui.QComboBox(self.groupBox_2)
        self.horizontalalignment.setMinimumSize(QtCore.QSize(100, 0))
        self.horizontalalignment.setObjectName(_fromUtf8("horizontalalignment"))
        self.horizontalalignment.addItem(_fromUtf8(""))
        self.horizontalalignment.addItem(_fromUtf8(""))
        self.horizontalalignment.addItem(_fromUtf8(""))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.horizontalalignment)
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setMinimumSize(QtCore.QSize(0, 0))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_9)
        self.verticalalignment = QtGui.QComboBox(self.groupBox_2)
        self.verticalalignment.setMinimumSize(QtCore.QSize(100, 0))
        self.verticalalignment.setObjectName(_fromUtf8("verticalalignment"))
        self.verticalalignment.addItem(_fromUtf8(""))
        self.verticalalignment.addItem(_fromUtf8(""))
        self.verticalalignment.addItem(_fromUtf8(""))
        self.verticalalignment.addItem(_fromUtf8(""))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.verticalalignment)
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_10)
        self.linespacing = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.linespacing.setSingleStep(0.2)
        self.linespacing.setProperty(_fromUtf8("value"), 1.0)
        self.linespacing.setObjectName(_fromUtf8("linespacing"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.linespacing)
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_11)
        self.rotation = QtGui.QComboBox(self.groupBox_2)
        self.rotation.setMinimumSize(QtCore.QSize(100, 0))
        self.rotation.setObjectName(_fromUtf8("rotation"))
        self.rotation.addItem(_fromUtf8(""))
        self.rotation.addItem(_fromUtf8(""))
        self.rotation.addItem(_fromUtf8(""))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.rotation)
        self.rotationCustom = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.rotationCustom.setEnabled(False)
        self.rotationCustom.setDecimals(1)
        self.rotationCustom.setMaximum(360.0)
        self.rotationCustom.setObjectName(_fromUtf8("rotationCustom"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.rotationCustom)
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_12)
        self.alpha = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.alpha.setMaximum(1.0)
        self.alpha.setSingleStep(0.1)
        self.alpha.setProperty(_fromUtf8("value"), 1.0)
        self.alpha.setObjectName(_fromUtf8("alpha"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.alpha)
        self.gridLayout.addWidget(self.groupBox_2, 6, 2, 1, 3)
        self.groupBox_3 = QtGui.QGroupBox(TextOptionsWidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setRowWrapPolicy(QtGui.QFormLayout.DontWrapRows)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.size = QtGui.QSpinBox(self.groupBox_3)
        self.size.setMinimum(1)
        self.size.setMaximum(255)
        self.size.setProperty(_fromUtf8("value"), 12)
        self.size.setObjectName(_fromUtf8("size"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.size)
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.style = QtGui.QComboBox(self.groupBox_3)
        self.style.setMinimumSize(QtCore.QSize(100, 0))
        self.style.setObjectName(_fromUtf8("style"))
        self.style.addItem(_fromUtf8(""))
        self.style.addItem(_fromUtf8(""))
        self.style.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.style)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.variant = QtGui.QComboBox(self.groupBox_3)
        self.variant.setMinimumSize(QtCore.QSize(100, 0))
        self.variant.setObjectName(_fromUtf8("variant"))
        self.variant.addItem(_fromUtf8(""))
        self.variant.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.variant)
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.stretch = QtGui.QSpinBox(self.groupBox_3)
        self.stretch.setMaximum(1000)
        self.stretch.setProperty(_fromUtf8("value"), 100)
        self.stretch.setObjectName(_fromUtf8("stretch"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.stretch)
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.weight = QtGui.QSpinBox(self.groupBox_3)
        self.weight.setMaximum(1000)
        self.weight.setProperty(_fromUtf8("value"), 100)
        self.weight.setObjectName(_fromUtf8("weight"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.weight)
        self.gridLayout.addWidget(self.groupBox_3, 5, 2, 1, 3)
        self.storedSettingsButton = QStoredSettingsButton(TextOptionsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.storedSettingsButton.sizePolicy().hasHeightForWidth())
        self.storedSettingsButton.setSizePolicy(sizePolicy)
        self.storedSettingsButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.storedSettingsButton.setArrowType(QtCore.Qt.LeftArrow)
        self.storedSettingsButton.setObjectName(_fromUtf8("storedSettingsButton"))
        self.gridLayout.addWidget(self.storedSettingsButton, 5, 5, 2, 1)

        self.retranslateUi(TextOptionsWidget)
        QtCore.QObject.connect(self.color, QtCore.SIGNAL(_fromUtf8("clicked()")), self.color.createColorDialog)
        QtCore.QObject.connect(self.backgroundcolor, QtCore.SIGNAL(_fromUtf8("clicked()")), self.backgroundcolor.createColorDialog)
        QtCore.QObject.connect(self.rotation, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), TextOptionsWidget.rotationBoxHandler)
        QtCore.QObject.connect(self.buttons, QtCore.SIGNAL(_fromUtf8("clicked(QAbstractButton*)")), TextOptionsWidget.buttonClickHandler)
        QtCore.QObject.connect(self.storedSettingsButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.storedSettingsButton.toggleWidget)
        TextOptionsWidget.setTabOrder(self.name, self.size)
        TextOptionsWidget.setTabOrder(self.size, self.style)
        TextOptionsWidget.setTabOrder(self.style, self.variant)
        TextOptionsWidget.setTabOrder(self.variant, self.stretch)
        TextOptionsWidget.setTabOrder(self.stretch, self.weight)
        TextOptionsWidget.setTabOrder(self.weight, self.color)
        TextOptionsWidget.setTabOrder(self.color, self.backgroundcolor)
        TextOptionsWidget.setTabOrder(self.backgroundcolor, self.alpha)
        TextOptionsWidget.setTabOrder(self.alpha, self.horizontalalignment)
        TextOptionsWidget.setTabOrder(self.horizontalalignment, self.verticalalignment)
        TextOptionsWidget.setTabOrder(self.verticalalignment, self.linespacing)
        TextOptionsWidget.setTabOrder(self.linespacing, self.rotation)
        TextOptionsWidget.setTabOrder(self.rotation, self.rotationCustom)
        TextOptionsWidget.setTabOrder(self.rotationCustom, self.buttons)

    def retranslateUi(self, TextOptionsWidget):
        TextOptionsWidget.setWindowTitle(QtGui.QApplication.translate("TextOptionsWidget", "Text Options", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("TextOptionsWidget", "Font", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("TextOptionsWidget", "Display Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("TextOptionsWidget", "Text Color", None, QtGui.QApplication.UnicodeUTF8))
        self.color.setText(QtGui.QApplication.translate("TextOptionsWidget", "(0,0,0,255)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("TextOptionsWidget", "Text Background Color", None, QtGui.QApplication.UnicodeUTF8))
        self.backgroundcolor.setText(QtGui.QApplication.translate("TextOptionsWidget", "(255,255,255,0)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("TextOptionsWidget", "Horizontal Alignment", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalalignment.setItemText(0, QtGui.QApplication.translate("TextOptionsWidget", "center", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalalignment.setItemText(1, QtGui.QApplication.translate("TextOptionsWidget", "right", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalalignment.setItemText(2, QtGui.QApplication.translate("TextOptionsWidget", "left", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("TextOptionsWidget", "Vertical Alignment", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalalignment.setItemText(0, QtGui.QApplication.translate("TextOptionsWidget", "center", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalalignment.setItemText(1, QtGui.QApplication.translate("TextOptionsWidget", "top", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalalignment.setItemText(2, QtGui.QApplication.translate("TextOptionsWidget", "bottom", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalalignment.setItemText(3, QtGui.QApplication.translate("TextOptionsWidget", "baseline", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("TextOptionsWidget", "Line Spacing", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("TextOptionsWidget", "Rotation", None, QtGui.QApplication.UnicodeUTF8))
        self.rotation.setItemText(0, QtGui.QApplication.translate("TextOptionsWidget", "horizontal", None, QtGui.QApplication.UnicodeUTF8))
        self.rotation.setItemText(1, QtGui.QApplication.translate("TextOptionsWidget", "vertical", None, QtGui.QApplication.UnicodeUTF8))
        self.rotation.setItemText(2, QtGui.QApplication.translate("TextOptionsWidget", "custom", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("TextOptionsWidget", "Alpha (Transparency)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("TextOptionsWidget", "Font Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("TextOptionsWidget", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("TextOptionsWidget", "Style", None, QtGui.QApplication.UnicodeUTF8))
        self.style.setItemText(0, QtGui.QApplication.translate("TextOptionsWidget", "normal", None, QtGui.QApplication.UnicodeUTF8))
        self.style.setItemText(1, QtGui.QApplication.translate("TextOptionsWidget", "italic", None, QtGui.QApplication.UnicodeUTF8))
        self.style.setItemText(2, QtGui.QApplication.translate("TextOptionsWidget", "oblique", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("TextOptionsWidget", "Variant", None, QtGui.QApplication.UnicodeUTF8))
        self.variant.setItemText(0, QtGui.QApplication.translate("TextOptionsWidget", "normal", None, QtGui.QApplication.UnicodeUTF8))
        self.variant.setItemText(1, QtGui.QApplication.translate("TextOptionsWidget", "small-caps", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("TextOptionsWidget", "Character Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("TextOptionsWidget", "Weight (boldness)", None, QtGui.QApplication.UnicodeUTF8))
        self.storedSettingsButton.setText(QtGui.QApplication.translate("TextOptionsWidget", "S\n"
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
from gui.QTextOptionsWidget import QTextOptionsWidget
from gui.QStoredSettingsButton import QStoredSettingsButton
