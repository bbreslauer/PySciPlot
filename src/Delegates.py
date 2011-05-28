# Copyright (C) 2010-2011 Ben Breslauer
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from PyQt4.QtCore import Qt
from PyQt4.QtGui import QItemDelegate, QSpinBox, QComboBox, QLineEdit


class SpinBoxDelegate(QItemDelegate):

    def __init__(self, min, max, *args):
        """
        min and max are the limits that the spin box can scroll to/accept.
        """
        QItemDelegate.__init__(self, *args)
        self.min = min
        self.max = max

    def createEditor(self, parent, option, index):
        editor = QSpinBox(parent)
        editor.setMinimum(self.min)
        editor.setMaximum(self.max)
        return editor

    def setEditorData(self, editor, index):
        editor.setValue(int(index.model().data(index, Qt.EditRole)))

    def setModelData(self, editor, model, index):
        value = editor.value()
        model.setData(index, value, Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


class WavePairListDelegate(QItemDelegate):

    def __init__(self, model, *args):
        """
        model is the model used for the combo box.
        """
        QItemDelegate.__init__(self, *args)
        self.model = model

    def createEditor(self, parent, option, index):
        if index.column() in [0, 1]:
            editor = QComboBox(parent)
            editor.setSizeAdjustPolicy(QComboBox.AdjustToContents)
            editor.setModel(self.model)
        else:
            editor = QLineEdit(parent)
        return editor

    def setEditorData(self, editor, index):
        if index.column() == 0:
            value = index.internalPointer().xName()
            editor.setCurrentIndex(editor.model().getIndexByWaveName(value))
        elif index.column() == 1:
            value = index.internalPointer().yName()
            editor.setCurrentIndex(editor.model().getIndexByWaveName(value))
        elif index.column() == 2:
            value = index.internalPointer().label()
            editor.setText(value)

    def setModelData(self, editor, model, index):
        if index.column() == 0:
            wave = editor.model().waveByRow(editor.currentIndex())
            index.internalPointer().setX(wave)
        elif index.column() == 1:
            wave = editor.model().waveByRow(editor.currentIndex())
            index.internalPointer().setY(wave)
        elif index.column() == 2:
            label = editor.text()
            index.internalPointer().setLabel(label)

    def updateEditorGeometry(self, editor, option, index):
        pass
        editor.setGeometry(option.rect)




