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


from PyQt4.QtCore import QAbstractListModel, QModelIndex, Qt, QVariant

class FigureListModel(QAbstractListModel):
    """
    A list of all the figures in the application.
    """

    def __init__(self, figures, parent=None, *args):
        QAbstractListModel.__init__(self, parent, *args)
        self.parent = parent
        self._figures = figures

    def rowCount(self, parent=QModelIndex()):
        """Return the number of rows in this model."""
        return self._figures.length()

    def index(self, row, column, parent=QModelIndex()):
        if row > self._figures.length():
            return self.createIndex(row, column, parent)
        return self.createIndex(row, column, self._figures.getFigure(row))

    def data(self, index, role):
        """Return the name of the figure entry at the given index."""

        if index.isValid() and (role == Qt.DisplayRole or role == Qt.EditRole):
            if self._figures.getFigure(index.row()):
                return self._figures.getFigure(index.row()).get('windowTitle')
        return QVariant()

    def headerData(self, section, orientation, role):
        """Return the header for the given section and orientation."""

        if orientation == Qt.Horizontal:
            return QVariant("Figures")
        elif orientation == Qt.Vertical:
            return QVariant(section)
        return QVariant()

    def flags(self, index):
        """Return the flags for the given index."""

        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable

    def setData(self, index, value, role):
        "Change the name for the figure at index."""
        if index.isValid() and role == Qt.EditRole and self._figures.getFigure(index.row()):
            # Do not allow for blank figure names
            if value == "":
                return False
            self._figures.getFigure(index.row()).set_('windowTitle', str(value.toString()))
            self.dataChanged.emit(index, index)
            return True
        return False

    def doReset(self, *args):
        """Take any number of arguments and just reset the model."""
        self.reset()

    def getFigure(self, row):
        if self._figures:
            return self._figures.getFigure(row)
        return None

