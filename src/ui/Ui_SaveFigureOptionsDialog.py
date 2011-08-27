# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_SaveFigureOptionsDialog.ui'
#
# Created: Sat Aug 27 19:02:55 2011
#      by: pyside-uic 0.2.13 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SaveFigureOptionsDialog(object):
    def setupUi(self, SaveFigureOptionsDialog):
        SaveFigureOptionsDialog.setObjectName("SaveFigureOptionsDialog")
        SaveFigureOptionsDialog.setWindowModality(QtCore.Qt.WindowModal)
        SaveFigureOptionsDialog.resize(239, 300)
        SaveFigureOptionsDialog.setModal(True)
        self.formLayout = QtGui.QFormLayout(SaveFigureOptionsDialog)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(SaveFigureOptionsDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.dpi = QtGui.QSpinBox(SaveFigureOptionsDialog)
        self.dpi.setMaximum(10000)
        self.dpi.setProperty("value", 100)
        self.dpi.setObjectName("dpi")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.dpi)
        self.label_2 = QtGui.QLabel(SaveFigureOptionsDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.orientation = QtGui.QComboBox(SaveFigureOptionsDialog)
        self.orientation.setObjectName("orientation")
        self.orientation.addItem("")
        self.orientation.addItem("")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.orientation)
        self.buttonBox = QtGui.QDialogButtonBox(SaveFigureOptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.buttonBox)

        self.retranslateUi(SaveFigureOptionsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SaveFigureOptionsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SaveFigureOptionsDialog.reject)

    def retranslateUi(self, SaveFigureOptionsDialog):
        SaveFigureOptionsDialog.setWindowTitle(QtGui.QApplication.translate("SaveFigureOptionsDialog", "Save Figure Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SaveFigureOptionsDialog", "dpi", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SaveFigureOptionsDialog", "Orientation", None, QtGui.QApplication.UnicodeUTF8))
        self.orientation.setItemText(0, QtGui.QApplication.translate("SaveFigureOptionsDialog", "Landscape", None, QtGui.QApplication.UnicodeUTF8))
        self.orientation.setItemText(1, QtGui.QApplication.translate("SaveFigureOptionsDialog", "Portrait", None, QtGui.QApplication.UnicodeUTF8))

