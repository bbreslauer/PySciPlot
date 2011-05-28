# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_SaveFigureOptionsDialog.ui'
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

class Ui_SaveFigureOptionsDialog(object):
    def setupUi(self, SaveFigureOptionsDialog):
        SaveFigureOptionsDialog.setObjectName(_fromUtf8("SaveFigureOptionsDialog"))
        SaveFigureOptionsDialog.setWindowModality(QtCore.Qt.WindowModal)
        SaveFigureOptionsDialog.resize(239, 300)
        SaveFigureOptionsDialog.setModal(True)
        self.formLayout = QtGui.QFormLayout(SaveFigureOptionsDialog)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(SaveFigureOptionsDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.dpi = QtGui.QSpinBox(SaveFigureOptionsDialog)
        self.dpi.setMaximum(10000)
        self.dpi.setProperty(_fromUtf8("value"), 100)
        self.dpi.setObjectName(_fromUtf8("dpi"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.dpi)
        self.label_2 = QtGui.QLabel(SaveFigureOptionsDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.orientation = QtGui.QComboBox(SaveFigureOptionsDialog)
        self.orientation.setObjectName(_fromUtf8("orientation"))
        self.orientation.addItem(_fromUtf8(""))
        self.orientation.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.orientation)
        self.buttonBox = QtGui.QDialogButtonBox(SaveFigureOptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.buttonBox)

        self.retranslateUi(SaveFigureOptionsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SaveFigureOptionsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SaveFigureOptionsDialog.reject)

    def retranslateUi(self, SaveFigureOptionsDialog):
        SaveFigureOptionsDialog.setWindowTitle(QtGui.QApplication.translate("SaveFigureOptionsDialog", "Save Figure Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SaveFigureOptionsDialog", "dpi", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SaveFigureOptionsDialog", "Orientation", None, QtGui.QApplication.UnicodeUTF8))
        self.orientation.setItemText(0, QtGui.QApplication.translate("SaveFigureOptionsDialog", "Landscape", None, QtGui.QApplication.UnicodeUTF8))
        self.orientation.setItemText(1, QtGui.QApplication.translate("SaveFigureOptionsDialog", "Portrait", None, QtGui.QApplication.UnicodeUTF8))

