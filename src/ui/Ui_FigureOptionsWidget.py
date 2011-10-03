# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_FigureOptionsWidget.ui'
#
# Created: Sun Oct  2 22:33:39 2011
#      by: pyside-uic 0.2.13 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FigureOptionsWidget(object):
    def setupUi(self, FigureOptionsWidget):
        FigureOptionsWidget.setObjectName("FigureOptionsWidget")
        FigureOptionsWidget.resize(584, 364)
        self.gridLayout = QtGui.QGridLayout(FigureOptionsWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_24 = QtGui.QLabel(FigureOptionsWidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 0, 0, 1, 1)
        self.windowTitle = QtGui.QLineEdit(FigureOptionsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windowTitle.sizePolicy().hasHeightForWidth())
        self.windowTitle.setSizePolicy(sizePolicy)
        self.windowTitle.setMinimumSize(QtCore.QSize(150, 0))
        self.windowTitle.setObjectName("windowTitle")
        self.gridLayout.addWidget(self.windowTitle, 0, 1, 1, 2)
        self.storedSettingsButton = QStoredSettingsButton(FigureOptionsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.storedSettingsButton.sizePolicy().hasHeightForWidth())
        self.storedSettingsButton.setSizePolicy(sizePolicy)
        self.storedSettingsButton.setMaximumSize(QtCore.QSize(26, 16777215))
        self.storedSettingsButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.storedSettingsButton.setArrowType(QtCore.Qt.LeftArrow)
        self.storedSettingsButton.setObjectName("storedSettingsButton")
        self.gridLayout.addWidget(self.storedSettingsButton, 0, 3, 5, 1)
        self.label_13 = QtGui.QLabel(FigureOptionsWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)
        self.title = QtGui.QLineEdit(FigureOptionsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setMinimumSize(QtCore.QSize(150, 0))
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 1, 1, 1, 1)
        self.titleFont = QTextOptionsButton(FigureOptionsWidget)
        self.titleFont.setObjectName("titleFont")
        self.gridLayout.addWidget(self.titleFont, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(FigureOptionsWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.backgroundColor = QColorButton(FigureOptionsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backgroundColor.sizePolicy().hasHeightForWidth())
        self.backgroundColor.setSizePolicy(sizePolicy)
        self.backgroundColor.setMinimumSize(QtCore.QSize(55, 0))
        self.backgroundColor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.backgroundColor.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.backgroundColor.setObjectName("backgroundColor")
        self.gridLayout.addWidget(self.backgroundColor, 2, 1, 1, 2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtGui.QLabel(FigureOptionsWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtGui.QLabel(FigureOptionsWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)
        self.rows = QtGui.QSpinBox(FigureOptionsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rows.sizePolicy().hasHeightForWidth())
        self.rows.setSizePolicy(sizePolicy)
        self.rows.setMinimumSize(QtCore.QSize(50, 0))
        self.rows.setMinimum(1)
        self.rows.setObjectName("rows")
        self.gridLayout_2.addWidget(self.rows, 1, 1, 1, 1)
        self.columns = QtGui.QSpinBox(FigureOptionsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.columns.sizePolicy().hasHeightForWidth())
        self.columns.setSizePolicy(sizePolicy)
        self.columns.setMinimumSize(QtCore.QSize(50, 0))
        self.columns.setMinimum(1)
        self.columns.setObjectName("columns")
        self.gridLayout_2.addWidget(self.columns, 1, 3, 1, 1)
        self.label = QtGui.QLabel(FigureOptionsWidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.width = QtGui.QSpinBox(FigureOptionsWidget)
        self.width.setMaximum(10000)
        self.width.setSingleStep(10)
        self.width.setProperty("value", 600)
        self.width.setObjectName("width")
        self.gridLayout_2.addWidget(self.width, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(FigureOptionsWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.height = QtGui.QSpinBox(FigureOptionsWidget)
        self.height.setMaximum(10000)
        self.height.setSingleStep(10)
        self.height.setProperty("value", 400)
        self.height.setObjectName("height")
        self.gridLayout_2.addWidget(self.height, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 3, 1, 1)
        self.buttons = QtGui.QDialogButtonBox(FigureOptionsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttons.sizePolicy().hasHeightForWidth())
        self.buttons.setSizePolicy(sizePolicy)
        self.buttons.setOrientation(QtCore.Qt.Horizontal)
        self.buttons.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Reset)
        self.buttons.setCenterButtons(True)
        self.buttons.setObjectName("buttons")
        self.gridLayout.addWidget(self.buttons, 6, 0, 1, 3)
        self.line_2 = QtGui.QFrame(FigureOptionsWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 3)
        self.groupBox = QtGui.QGroupBox(FigureOptionsWidget)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.padding = QtGui.QTableView(self.groupBox)
        self.padding.setObjectName("padding")
        self.horizontalLayout.addWidget(self.padding)
        self.gridLayout.addWidget(self.groupBox, 4, 0, 1, 3)

        self.retranslateUi(FigureOptionsWidget)
        QtCore.QObject.connect(self.backgroundColor, QtCore.SIGNAL("clicked()"), self.backgroundColor.createColorDialog)
        QtCore.QObject.connect(self.titleFont, QtCore.SIGNAL("clicked()"), self.titleFont.showTextOptionsWidget)
        QtCore.QObject.connect(self.buttons, QtCore.SIGNAL("clicked(QAbstractButton*)"), FigureOptionsWidget.buttonClickHandler)
        QtCore.QObject.connect(self.storedSettingsButton, QtCore.SIGNAL("clicked()"), self.storedSettingsButton.toggleWidget)

    def retranslateUi(self, FigureOptionsWidget):
        FigureOptionsWidget.setWindowTitle(QtGui.QApplication.translate("FigureOptionsWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("FigureOptionsWidget", "Window Title", None, QtGui.QApplication.UnicodeUTF8))
        self.windowTitle.setToolTip(QtGui.QApplication.translate("FigureOptionsWidget", "Window Title Text", None, QtGui.QApplication.UnicodeUTF8))
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
        self.label_13.setText(QtGui.QApplication.translate("FigureOptionsWidget", "Figure Title", None, QtGui.QApplication.UnicodeUTF8))
        self.titleFont.setText(QtGui.QApplication.translate("FigureOptionsWidget", "Text Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("FigureOptionsWidget", "Background Color", None, QtGui.QApplication.UnicodeUTF8))
        self.backgroundColor.setText(QtGui.QApplication.translate("FigureOptionsWidget", "(255,255,255,255)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("FigureOptionsWidget", "Rows", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("FigureOptionsWidget", "Columns", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FigureOptionsWidget", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FigureOptionsWidget", "Height", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("FigureOptionsWidget", "Padding", None, QtGui.QApplication.UnicodeUTF8))

from gui.QTextOptionsButton import QTextOptionsButton
from gui.QColorButton import QColorButton
from gui.QFigureOptionsWidget import QFigureOptionsWidget
from gui.QStoredSettingsButton import QStoredSettingsButton
