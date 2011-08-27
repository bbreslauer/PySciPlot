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


from PySide.QtCore import QAbstractListModel, QModelIndex, Qt

class PlotListModel(QAbstractListModel):
    """
    A list of all the plots in a figure.
    """

    def __init__(self, figure=None, parent=None, *args):
        QAbstractListModel.__init__(self, parent, *args)
        self.parent = parent
        self._figure = figure 

    def rowCount(self, parent=QModelIndex()):
        """Return the number of rows in this model."""
        if self._figure:
            return self._figure.numPlots()
        return 0

    def index(self, row, column, parent=QModelIndex()):
        # row is the plot number
        if not self._figure or row > self._figure.numPlots():
            return self.createIndex(row, column, parent)
        return self.createIndex(row, column, self._figure.getPlot(row))

    def data(self, index, role):
        """Return the name of the figure entry at the given index."""

        if index.isValid() and role == Qt.DisplayRole and self._figure and index.row() < self._figure.numPlots():
            plotNum = index.row()
            return str(plotNum) + " - " + str(self._figure.getPlot(plotNum).get('name'))
        return None

    def headerData(self, section, orientation, role):
        """Return the header for the given section and orientation."""

        if orientation == Qt.Horizontal:
            return "Plots"
        elif orientation == Qt.Vertical:
            return str(section)
        return None

    def flags(self, index):
        """Return the flags for the given index."""

        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def doReset(self, *args):
        """Take any number of arguments and just reset the model."""
        self.reset()

    def emitDataChanged(self, row, name):
        index = self.index(row - 1, 0)
        print "name: " + str(name) + ", row: " + str(row)
        self.dataChanged.emit(index, index)

    def setFigure(self, figure):
        self._figure = figure
        self.doReset()

    def getPlot(self, row):
        plotNum = row
        if self._figure:
            return self._figure.getPlot(plotNum)
        return None

