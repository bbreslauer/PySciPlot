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


from PySide.QtCore import QAbstractTableModel, Qt, QModelIndex
from PySide.QtGui import QWidget, QApplication, QDialogButtonBox

import Util
from QEditFigureSubWidget import *
from Figure import Figure

class QFigureOptionsWidget(QEditFigureSubWidget):

    properties = (  
                 'windowTitle',
                 'title',
                 'titleFont',
                 'rows',
                 'columns',
                 'width',
                 'height',
                 'backgroundColor',
                )

#    def __init__(self, *args):
#        QEditFigureSubWidget.__init__(self, *args)
#
    def initSubWidgets(self):
        self._paddingModel = PaddingModel(view=self.getChild('padding'))
        self.getChild('padding').setModel(self._paddingModel)

    def changePaddingModelFigure(self):
        """
        Update the figure in the padding model.
        """
        self._paddingModel.setFigure(self._editFigureDialogModule.currentFigure())

    def saveUi(self):
        """Save the UI data to the current Figure object."""
        
        self._editFigureDialogModule.currentFigure().setMultiple(self.getCurrentUi())
        self._paddingModel.savePadding()

    def resetUi(self):
        """Set the UI to the current Figure's settings."""
        try:
            self.setCurrentUi(self._editFigureDialogModule.currentFigure().properties)
            self._paddingModel.resetPadding()
        except:
            # There were probably no figures available (the last one was deleted) and so properties doesn't exist.
            # In this case, just leave the current options alone.
            pass

    def resetUiSize(self):
        """Set the UI to the current Figure's settings, but only for the width and height."""

        try:
            size = {}
            size['width'] = self._editFigureDialogModule.currentFigure().properties['width']
            size['height'] = self._editFigureDialogModule.currentFigure().properties['height']

            self.setCurrentUi(size)
        except:
            pass

    def reload(self):
        pass


class PaddingModel(QAbstractTableModel):
    """
    This model represents the padding options for each plot. Only one view can be
    attached to this model.
    """

    def __init__(self, figure=None, view=None, parent=None, *args):

        QAbstractTableModel.__init__(self, parent, *args)

        self._figure = None
        self._view = view
        self._padding = []
        self.setFigure(figure)

    def setFigure(self, figure):
        if isinstance(figure, Figure) or figure is None:
            try:
                self._figure.numPlotsChanged.disconnect(self.resetPadding)
            except:
                pass
            self._figure = figure
            self.resetPadding()
            try:
                self._figure.numPlotsChanged.connect(self.resetPadding)
            except:
                pass
            self.reset()

    def resetPadding(self):
        self._padding = []

        if self._figure is None:
            return

        for index, plot in enumerate(self._figure.plots()):
            padding = [index, plot.get('bottomPadding'), plot.get('topPadding'), plot.get('leftPadding'), plot.get('rightPadding')]
            self._padding.append(padding)

        self.reset()

    def savePadding(self):
        if self._figure is None:
            return

        for index, plot in enumerate(self._figure.plots()):
            currentProperties = {}
            currentProperties['bottomPadding'] = self._padding[index][1]
            currentProperties['topPadding'] = self._padding[index][2]
            currentProperties['leftPadding'] = self._padding[index][3]
            currentProperties['rightPadding'] = self._padding[index][4]

            plot.setMultiple(currentProperties)

    def flags(self, index):
        """Return the flags for the item at the given index."""

        if not index.isValid():
            return Qt.ItemIsEnabled
        if index.column() == 0:
            return Qt.ItemIsEnabled
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if section == 0:
                return 'Plot'
            elif section == 1:
                return 'Bottom'
            elif section == 2:
                return 'Top'
            elif section == 3:
                return 'Left'
            elif section == 4:
                return 'Right'
            else:
                return ''
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return str(section)
        return None

    def columnCount(self, parent = QModelIndex()):
        return 5

    def rowCount(self, parent = QModelIndex()):
        if self._figure is None:
            return 0
        return self._figure.numPlots()

    def data(self, index, role = Qt.DisplayRole):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole and role != Qt.EditRole:
            return None
        elif index.column() >= self.columnCount():
            return None
        elif index.row() >= self.rowCount():
            return None
        else:
            return self._padding[index.row()][index.column()]

    def setData(self, index, value, role):
        if index.isValid() and role == Qt.EditRole:
            self._padding[index.row()][index.column()] = int(value)

            # also set this value for any other cells that are selected. This makes
            # it easy to set multiple cells to the same value, for instance if you
            # want all left padding to be a certain value.
            for ind in self._view.selectedIndexes():
                self._padding[ind.row()][ind.column()] = int(value)

            return True
        return False

