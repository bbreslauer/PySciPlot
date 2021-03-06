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


from PyQt4.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant, QString, pyqtSignal

class WavePairListModel(QAbstractTableModel):
    """
    All the data that corresponds to wave pairs in a figure are displayed based on this model.
    
    Signals that are emitted from this class are:
        WavePairAdded   - emitted when a WavePair is added to the list
        WavePairRemoved - emitted when a WavePair is removed from the list
    """

    wavePairAdded   = pyqtSignal()
    wavePairRemoved = pyqtSignal()


    def __init__(self, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self._parent = parent
        self._data = []
        self._columnNames = ['X', 'Y', 'Label']
       
        # Connect signals
        self.wavePairAdded.connect(self.doReset)
        self.wavePairRemoved.connect(self.doReset)
        self.dataChanged.connect(self.doReset)

    def rowCount(self, parent=QModelIndex()):
        """Return the number of WavePairs in all the plots in the figure."""
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        """Return the number of columns."""
        return len(self._columnNames)

    def headerData(self, section, orientation, role):
        """Return the header for the given section and orientation."""

        if orientation == Qt.Horizontal and section < self.columnCount() and role == Qt.DisplayRole:
            return QVariant(QString(self._columnNames[section]))
        return QVariant()

    def index(self, row, column, parent=QModelIndex()):
        if row >= len(self._data):
            return self.createIndex(row, column, parent)
        return self.createIndex(row, column, self._data[row])
    
    def data(self, index, role):
        """Return the data for the given index."""

        if self.indexIsValid(index) and role == Qt.DisplayRole:
            if self._columnNames[index.column()] == 'X':
                return QVariant(self._data[index.row()].xName())
            elif self._columnNames[index.column()] == 'Y':
                return QVariant(self._data[index.row()].yName())
            elif self._columnNames[index.column()] == 'Label':
                return QVariant(self._data[index.row()].label())
        else:
            return QVariant()
    
    def indexIsValid(self, index):
        if index.isValid() and index.column() < self.columnCount() and index.row() < self.rowCount():
            return True
        return False

    def clearData(self):
        """Reset data array to a blank list."""
        self._data = []

    def flags(self, index):
        """Return the flags for the given index."""

        if not self.indexIsValid(index):
            return Qt.ItemIsEnabled
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable
    
    def doReset(self, *args):
        self.reset()

    def addWavePair(self, wavePair):
        self._data.append(wavePair)
        self.dataChanged.emit(self.index(len(self._data)-1, 0), self.index(len(self._data)-1, 2))
        return True

    def removeWavePair(self, wavePair):
        try:
            self._data.remove(wavePair)
            self.doReset()
        except:
            pass

    def getWavePairByRow(self, row):
        if row >= 0 and row < self.rowCount():
            return self._data[row]
        return None

