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


from PySide.QtCore import QAbstractTableModel, Qt, QModelIndex, Signal, QSize
from PySide.QtGui import QApplication

import Util
from Wave import Wave

class DataTableModel(QAbstractTableModel):
    """
    This is the data model for a table.
    
    A DataTableModel object contains links to all the Wave objects that are displayed in the associated view.

    Signals that are emitted from this class are:
    """

    # Signals
    dataChanged = Signal(QModelIndex, QModelIndex)
    
    def __init__(self, wavesIn=[], parent=None, *args):
        """
        Initialize a table model.  Add the initial set of wave(s) to the model.

        wavesIn is a list of Wave objects that should be initially added to the table.
        parent is the parent QT object.
        *args is anything other arguments that should be passed to the superclass constructor.
        """

        QAbstractTableModel.__init__(self, parent, *args)

        self._app = QApplication.instance().window

        self._waves = []

        for wave in wavesIn:
            self.addColumn(wave)

    def waves(self):
        return self._waves

    def rowCount(self, parent = QModelIndex()):
        """Return the number of rows."""

        if len(self.waves()) == 0:
            return 0

        rows = 0
        for wave in self.waves():
            thisWaveRows = wave.length()
            if thisWaveRows > rows:
                rows = thisWaveRows
        return rows + 1 # Want the extra row for adding more rows of data

    def columnCount(self, parent = QModelIndex()):
        """Return the number of columns."""

        return len(self.waves())

    def index(self, row, column, parent=QModelIndex()):
        if column >= self.columnCount():
            return self.createIndex(row, column, parent)
        elif row >= self.waves()[column].length():
            return self.createIndex(row, column, parent)
        return self.createIndex(row, column, self.waves()[column])

    def data(self, index, role = Qt.DisplayRole):
        """Return the data at position index with the given role."""

        if not index.isValid():
            return None
        elif role != Qt.DisplayRole and role != Qt.EditRole:
            return None
        elif index.column() >= self.columnCount():
            return None
        elif index.row() >= self.waves()[index.column()].length():
            return None
        elif self.waves()[index.column()].data()[index.row()] == "":
            return None
        #
        # If we return long() or float() instead of str(), then the view uses a spinbox
        # and we cannot easily return to a blank entry
        elif 'Integer' == self.waves()[index.column()].dataType():
            return str(self.waves()[index.column()].data()[index.row()])
        elif 'Decimal' == self.waves()[index.column()].dataType():
            return str(self.waves()[index.column()].data()[index.row()])
        elif 'String' == self.waves()[index.column()].dataType():
            return str(self.waves()[index.column()].data()[index.row()])
        return None

    def headerData(self, section, orientation, role):
        """
        Return the given header text for the specified role and section in the orientation.

        orientation is either horizontal (column headers) or vertical (row headers).
        """

        if orientation == Qt.Horizontal and section < self.columnCount() and role == Qt.DisplayRole:
            return str(self.waves()[section].name())
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return str(section)
        return None

    def flags(self, index):
        """Return the flags for the item at the given index."""

        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable

    # Modifying methods
    def addColumn(self, wave):
        """Add a column (wave) to the end of the table.  Return True if the column is added, False otherwise."""

        if self.insertColumn(self.columnCount(), wave):
            self.doReset()
            return True
        return False

    def insertColumn(self, position, wave):
        """Insert a column (wave) after the column described by position.  Return True if the column is added, False otherwise."""
        
        if isinstance(wave, Wave):
            self.waves().insert(position, wave)
            wave.nameChanged.connect(self.doReset)
            wave.dataModified.connect(self.doReset)
            return True
        return False

    def insertRows(self, row, count, parent=QModelIndex()):
        """
        Insert blank rows in all waves in the table.  Return True.
        """

        for wave in self.waves():
            for i in range(count):
                wave.insert(row, "")
        return True

    def removeColumn(self, position):
        """
        Remove the column in the given position.  Return True if the column is removed, False otherwise.
        """
        self.waves().pop(position)
        self.doReset()

    def removeWave(self, wave):
        """
        Remove the column(s) given by wave.  Return True if the column(s) is(are) removed, False otherwise.
        """
        while True:
            try:
                self.waves().remove(wave)
            except:
                break
        self.doReset()

    def removeAllWaves(self):
        """
        Remove all columns.
        """
        self._waves = []
        self.doReset()

    def setData(self, index, value, role):
        """
        Set the data at position index to value if the position is editable.  Return True if the data is set, False otherwise.

        Emits the Wave.dataModified signal if the data is changed.
        """

        result = False

        Util.debug(2, "DataTableModel.setData", "Setting data")

        if index.isValid() and role == Qt.EditRole:
            wave = self.waves()[index.column()]
            value = str(value)

            # Disregard if there is no change
            if str(self.data(index)) == value:
                return False

            Util.debug(2, "DataTableModel.setData", "Setting " + str(wave.name()) + "[" + str(index.row()) + "] to " + str(wave.castToWaveType(value)))
            result = wave.setData(index.row(), wave.castToWaveType(value))
            
            self.dataChanged.emit(index, index)

        return result

    def doReset(self, *args):
        """Take any number of arguments and just reset the model."""
        self.reset()

