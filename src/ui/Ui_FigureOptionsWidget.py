# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_FigureOptionsWidget.ui'
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

class Ui_FigureOptionsWidget(object):
    def setupUi(self, FigureOptionsWidget):
        FigureOptionsWidget.setObjectName(_fromUtf8("FigureOptionsWidget"))
        FigureOptionsWidget.resize(568, 355)
        self.gridLayout = QtGui.QGridLayout(FigureOptionsWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_7 = QtGui.QLabel(FigureOptionsWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtGui.QLabel(FigureOptionsWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 1)
        self.rows = QtGui.QSpinBox(FigureOptionsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rows.sizePolicy().hasHeightForWidth())
        self.rows.setSizePolicy(sizePolicy)
        self.rows.setMinimumSize(QtCore.QSize(50, 0))
        self.rows.setMinimum(1)
        self.rows.setObjectName(_fromUtf8("rows"))
        self.gridLayout_2.addWidget(self.rows, 0, 1, 1, 1)
        self.columns = QtGui.QSpinBox(FigureOptionsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.columns.sizePolicy().hasHeightForWidth())
        self.columns.setSizePolicy(sizePolicy)
        self.columns.setMinimumSize(QtCore.QSize(50, 0))
        self.columns.setMinimum(1)
        self.columns.setObjectName(_fromUtf8("columns"))
        self.gridLayout_2.addWidget(self.columns, 0, 3, 1, 1)
        self.linkPlotAxes = QtGui.QCheckBox(FigureOptionsWidget)
        self.linkPlotAxes.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.linkPlotAxes.setObjectName(_fromUtf8("linkPlotAxes"))
        self.gridLayout_2.addWidget(self.linkPlotAxes, 0, 4, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_2, 4, 0, 1, 3)
        self.windowTitle = QtGui.QLineEdit(FigureOptionsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windowTitle.sizePolicy().hasHeightForWidth())
        self.windowTitle.setSizePolicy(sizePolicy)
        self.windowTitle.setMinimumSize(QtCore.QSize(150, 0))
        self.windowTitle.setObjectName(_fromUtf8("windowTitle"))
        self.gridLayout.addWidget(self.windowTitle, 0, 1, 1, 2)
        self.label_24 = QtGui.QLabel(FigureOptionsWidget)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout.addWidget(self.label_24, 0, 0, 1, 1)
        self.label_13 = QtGui.QLabel(FigureOptionsWidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)
        self.title = QtGui.QLineEdit(FigureOptionsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setMinimumSize(QtCore.QSize(150, 0))
        self.title.setObjectName(_fromUtf8("title"))
        self.gridLayout.addWidget(self.title, 1, 1, 1, 1)
        self.titleFont = QTextOptionsButton(FigureOptionsWidget)
        self.titleFont.setObjectName(_fromUtf8("titleFont"))
        self.gridLayout.addWidget(self.titleFont, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(FigureOptionsWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.backgroundColor = QColorButton(FigureOptionsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backgroundColor.sizePolicy().hasHeightForWidth())
        self.backgroundColor.setSizePolicy(sizePolicy)
        self.backgroundColor.setMinimumSize(QtCore.QSize(55, 0))
        self.backgroundColor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.backgroundColor.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
""))
        self.backgroundColor.setObjectName(_fromUtf8("backgroundColor"))
        self.gridLayout.addWidget(self.backgroundColor, 2, 1, 1, 2)
        self.label_20 = QtGui.QLabel(FigureOptionsWidget)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout.addWidget(self.label_20, 3, 0, 1, 1)
        self.axesPadding = QtGui.QDoubleSpinBox(FigureOptionsWidget)
        self.axesPadding.setSingleStep(0.1)
        self.axesPadding.setProperty(_fromUtf8("value"), 0.5)
        self.axesPadding.setObjectName(_fromUtf8("axesPadding"))
        self.gridLayout.addWidget(self.axesPadding, 3, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 4, 1, 1)
        self.line_2 = QtGui.QFrame(FigureOptionsWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 3)
        self.buttons = QtGui.QDialogButtonBox(FigureOptionsWidget)
        self.buttons.setOrientation(QtCore.Qt.Horizontal)
        self.buttons.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Reset)
        self.buttons.setCenterButtons(True)
        self.buttons.setObjectName(_fromUtf8("buttons"))
        self.gridLayout.addWidget(self.buttons, 6, 0, 1, 3)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 3, 1, 1)
        self.storedSettingsButton = QStoredSettingsButton(FigureOptionsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.storedSettingsButton.sizePolicy().hasHeightForWidth())
        self.storedSettingsButton.setSizePolicy(sizePolicy)
        self.storedSettingsButton.setMaximumSize(QtCore.QSize(26, 16777215))
        self.storedSettingsButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.storedSettingsButton.setArrowType(QtCore.Qt.LeftArrow)
        self.storedSettingsButton.setObjectName(_fromUtf8("storedSettingsButton"))
        self.gridLayout.addWidget(self.storedSettingsButton, 0, 3, 8, 1)

        self.retranslateUi(FigureOptionsWidget)
        QtCore.QObject.connect(self.backgroundColor, QtCore.SIGNAL(_fromUtf8("clicked()")), self.backgroundColor.createColorDialog)
        QtCore.QObject.connect(self.titleFont, QtCore.SIGNAL(_fromUtf8("clicked()")), self.titleFont.showTextOptionsWidget)
        QtCore.QObject.connect(self.buttons, QtCore.SIGNAL(_fromUtf8("clicked(QAbstractButton*)")), FigureOptionsWidget.buttonClickHandler)
        QtCore.QObject.connect(self.storedSettingsButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.storedSettingsButton.toggleWidget)

    def retranslateUi(self, FigureOptionsWidget):
        FigureOptionsWidget.setWindowTitle(QtGui.QApplication.translate("FigureOptionsWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("FigureOptionsWidget", "Rows", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("FigureOptionsWidget", "Columns", None, QtGui.QApplication.UnicodeUTF8))
        self.linkPlotAxes.setText(QtGui.QApplication.translate("FigureOptionsWidget", "Link Axes Together", None, QtGui.QApplication.UnicodeUTF8))
        self.windowTitle.setToolTip(QtGui.QApplication.translate("FigureOptionsWidget", "Window Title Text", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("FigureOptionsWidget", "Window Title", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("FigureOptionsWidget", "Figure Title", None, QtGui.QApplication.UnicodeUTF8))
        self.titleFont.setText(QtGui.QApplication.translate("FigureOptionsWidget", "Font", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("FigureOptionsWidget", "Background Color", None, QtGui.QApplication.UnicodeUTF8))
        self.backgroundColor.setText(QtGui.QApplication.translate("FigureOptionsWidget", "(255,255,255,255)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("FigureOptionsWidget", "Padding between Plots", None, QtGui.QApplication.UnicodeUTF8))
        self.storedSettingsButton.setText(QtGui.QApplication.translate("FigureOptionsWidget", "S\n"
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
from gui.QFigureOptionsWidget import QFigureOptionsWidget
from gui.QStoredSettingsButton import QStoredSettingsButton
