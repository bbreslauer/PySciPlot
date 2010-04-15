# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManageWavesDialog.ui'
#
# Created: Tue Mar 23 23:19:26 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ManageWavesDialog(object):
    def setupUi(self, ManageWavesDialog):
        ManageWavesDialog.setObjectName("ManageWavesDialog")
        ManageWavesDialog.resize(600, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ManageWavesDialog.sizePolicy().hasHeightForWidth())
        ManageWavesDialog.setSizePolicy(sizePolicy)
        ManageWavesDialog.setMinimumSize(QtCore.QSize(600, 400))
        ManageWavesDialog.setBaseSize(QtCore.QSize(600, 400))
        self.horizontalLayoutWidget = QtGui.QWidget(ManageWavesDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-5, 0, 611, 401))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.waveNameLabel = QtGui.QLabel(self.horizontalLayoutWidget)
        self.waveNameLabel.setObjectName("waveNameLabel")
        self.verticalLayout.addWidget(self.waveNameLabel)
        self.waveNameLineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.waveNameLineEdit.setObjectName("waveNameLineEdit")
        self.verticalLayout.addWidget(self.waveNameLineEdit)
        self.createWaveButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.createWaveButton.setObjectName("createWaveButton")
        self.verticalLayout.addWidget(self.createWaveButton)
        self.wavesListView = QtGui.QListView(self.horizontalLayoutWidget)
        self.wavesListView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.wavesListView.setObjectName("wavesListView")
        self.verticalLayout.addWidget(self.wavesListView)
        self.removeWaveButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.removeWaveButton.setObjectName("removeWaveButton")
        self.verticalLayout.addWidget(self.removeWaveButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.closeButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout_3.addWidget(self.closeButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(ManageWavesDialog)
        QtCore.QMetaObject.connectSlotsByName(ManageWavesDialog)

    def retranslateUi(self, ManageWavesDialog):
        ManageWavesDialog.setWindowTitle(QtGui.QApplication.translate("ManageWavesDialog", "Manage Waves", None, QtGui.QApplication.UnicodeUTF8))
        self.waveNameLabel.setText(QtGui.QApplication.translate("ManageWavesDialog", "New Wave Name", None, QtGui.QApplication.UnicodeUTF8))
        self.createWaveButton.setText(QtGui.QApplication.translate("ManageWavesDialog", "Create Wave", None, QtGui.QApplication.UnicodeUTF8))
        self.removeWaveButton.setText(QtGui.QApplication.translate("ManageWavesDialog", "Remove Wave(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("ManageWavesDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

