# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Preferences.ui'
#
# Created: Fri May 27 16:40:09 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName(_fromUtf8("Preferences"))
        Preferences.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(Preferences)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Preferences)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.defaultDirectory = QtGui.QLineEdit(Preferences)
        self.defaultDirectory.setObjectName(_fromUtf8("defaultDirectory"))
        self.gridLayout.addWidget(self.defaultDirectory, 0, 1, 1, 1)
        self.buttons = QtGui.QDialogButtonBox(Preferences)
        self.buttons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Reset|QtGui.QDialogButtonBox.Save)
        self.buttons.setCenterButtons(True)
        self.buttons.setObjectName(_fromUtf8("buttons"))
        self.gridLayout.addWidget(self.buttons, 4, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Preferences)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.projectDirectory = QtGui.QLineEdit(Preferences)
        self.projectDirectory.setObjectName(_fromUtf8("projectDirectory"))
        self.gridLayout.addWidget(self.projectDirectory, 1, 1, 1, 1)
        self.defaultDirectoryButton = QtGui.QPushButton(Preferences)
        self.defaultDirectoryButton.setObjectName(_fromUtf8("defaultDirectoryButton"))
        self.gridLayout.addWidget(self.defaultDirectoryButton, 0, 2, 1, 1)
        self.projectDirectoryButton = QtGui.QPushButton(Preferences)
        self.projectDirectoryButton.setObjectName(_fromUtf8("projectDirectoryButton"))
        self.gridLayout.addWidget(self.projectDirectoryButton, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(Preferences)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.textOptions = QTextOptionsButton(Preferences)
        self.textOptions.setObjectName(_fromUtf8("textOptions"))
        self.gridLayout.addWidget(self.textOptions, 2, 1, 1, 1)

        self.retranslateUi(Preferences)
        QtCore.QObject.connect(self.textOptions, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textOptions.showTextOptionsWidget)
        Preferences.setTabOrder(self.defaultDirectory, self.defaultDirectoryButton)
        Preferences.setTabOrder(self.defaultDirectoryButton, self.projectDirectory)
        Preferences.setTabOrder(self.projectDirectory, self.projectDirectoryButton)
        Preferences.setTabOrder(self.projectDirectoryButton, self.textOptions)
        Preferences.setTabOrder(self.textOptions, self.buttons)

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(QtGui.QApplication.translate("Preferences", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Preferences", "Default Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Preferences", "Project Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.defaultDirectoryButton.setText(QtGui.QApplication.translate("Preferences", "Select...", None, QtGui.QApplication.UnicodeUTF8))
        self.projectDirectoryButton.setText(QtGui.QApplication.translate("Preferences", "Select...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Preferences", "Text Options", None, QtGui.QApplication.UnicodeUTF8))
        self.textOptions.setText(QtGui.QApplication.translate("Preferences", "Select Text Options", None, QtGui.QApplication.UnicodeUTF8))

from gui.QTextOptionsButton import QTextOptionsButton
