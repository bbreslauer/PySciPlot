# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ManageWavesDialog.ui'
#
# Created: Thu Feb 17 21:40:10 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ManageWavesDialog(object):
    def setupUi(self, ManageWavesDialog):
        ManageWavesDialog.setObjectName(_fromUtf8("ManageWavesDialog"))
        ManageWavesDialog.resize(350, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ManageWavesDialog.sizePolicy().hasHeightForWidth())
        ManageWavesDialog.setSizePolicy(sizePolicy)
        ManageWavesDialog.setMinimumSize(QtCore.QSize(350, 400))
        ManageWavesDialog.setBaseSize(QtCore.QSize(600, 400))
        self.gridLayout = QtGui.QGridLayout(ManageWavesDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(ManageWavesDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.wavesListView = QtGui.QListView(self.groupBox)
        self.wavesListView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.wavesListView.setObjectName(_fromUtf8("wavesListView"))
        self.gridLayout_3.addWidget(self.wavesListView, 1, 0, 1, 2)
        self.removeWaveButton = QtGui.QPushButton(self.groupBox)
        self.removeWaveButton.setObjectName(_fromUtf8("removeWaveButton"))
        self.gridLayout_3.addWidget(self.removeWaveButton, 2, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(ManageWavesDialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.dataType = QtGui.QComboBox(self.groupBox_2)
        self.dataType.setObjectName(_fromUtf8("dataType"))
        self.dataType.addItem(_fromUtf8(""))
        self.dataType.addItem(_fromUtf8(""))
        self.dataType.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.dataType, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 2)
        self.waveOptionsButtons = QtGui.QDialogButtonBox(self.groupBox_2)
        self.waveOptionsButtons.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Reset)
        self.waveOptionsButtons.setCenterButtons(True)
        self.waveOptionsButtons.setObjectName(_fromUtf8("waveOptionsButtons"))
        self.gridLayout_2.addWidget(self.waveOptionsButtons, 3, 0, 1, 2)
        self.waveName = QtGui.QLineEdit(self.groupBox_2)
        self.waveName.setObjectName(_fromUtf8("waveName"))
        self.gridLayout_2.addWidget(self.waveName, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.closeButton = QtGui.QPushButton(ManageWavesDialog)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.gridLayout.addWidget(self.closeButton, 1, 0, 1, 2)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)

        self.retranslateUi(ManageWavesDialog)
        ManageWavesDialog.setTabOrder(self.wavesListView, self.removeWaveButton)
        ManageWavesDialog.setTabOrder(self.removeWaveButton, self.waveName)
        ManageWavesDialog.setTabOrder(self.waveName, self.dataType)
        ManageWavesDialog.setTabOrder(self.dataType, self.waveOptionsButtons)
        ManageWavesDialog.setTabOrder(self.waveOptionsButtons, self.closeButton)

    def retranslateUi(self, ManageWavesDialog):
        ManageWavesDialog.setWindowTitle(QtGui.QApplication.translate("ManageWavesDialog", "Manage Waves", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ManageWavesDialog", "Waves", None, QtGui.QApplication.UnicodeUTF8))
        self.removeWaveButton.setText(QtGui.QApplication.translate("ManageWavesDialog", "Remove Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("ManageWavesDialog", "Wave Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ManageWavesDialog", "Data Type", None, QtGui.QApplication.UnicodeUTF8))
        self.dataType.setItemText(0, QtGui.QApplication.translate("ManageWavesDialog", "Integer", None, QtGui.QApplication.UnicodeUTF8))
        self.dataType.setItemText(1, QtGui.QApplication.translate("ManageWavesDialog", "Decimal", None, QtGui.QApplication.UnicodeUTF8))
        self.dataType.setItemText(2, QtGui.QApplication.translate("ManageWavesDialog", "String", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ManageWavesDialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("ManageWavesDialog", "Close Window", None, QtGui.QApplication.UnicodeUTF8))

