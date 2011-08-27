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


from PySide.QtCore import QModelIndex, Qt,  QMimeData, QDataStream, QIODevice, QAbstractListModel
from PySide.QtGui import QStringListModel, QApplication, QStandardItemModel

from Wave import Wave

class WavesListModel(QAbstractListModel):
    """
    A model for a list of waves.
    """
    
    def __init__(self, waveNames=[], parent=None, *args):
        QAbstractListModel.__init__(self, parent, *args)
        self._app = QApplication.instance().window

        self._orderedWaveNames = []
        for w in waveNames:
            self.appendRow(w)

        # Connect signals
        self.appWaves().waveRemoved[Wave].connect(self.removeWave)

    def appWaves(self):
        """All the waves in the application. NOT limited to the waves in this model."""
        return self._app.waves()
    
    def waves(self):
        """The application waves that are referenced in this model, in order."""
        waves = []
        for waveName in self.orderedWaveNames():
            wave = self.appWaves().wave(waveName)
            if wave:  # If the wave cannot be found, do not add it
                waves.append(wave)
        return waves

    def waveByRow(self, row):
        return self.appWaves().wave(self.waveNameByRow(row))

    def waveNameByRow(self, row):
        try:
            return self.orderedWaveNames()[row]
        except IndexError:
            return None

    def orderedWaves(self):
        """Deprecated: use orderedWaveNames"""
        print "orderedWaves is deprecated. Please use orderedWaveNames instead."
        return self.orderedWaveNames()

    def orderedWaveNames(self):
        """Return the list of waves (in order) in this model."""
        return self._orderedWaveNames

    def getIndexByWaveName(self, name):
        try:
            return self.orderedWaveNames().index(name)
        except:
            return -1

    def updateOrderedWaves(self, oldName, wave):
        index = self.getIndexByWaveName(oldName)
        if index >= 0:
            self.orderedWaveNames()[index] = wave.name()

    def appendRow(self, entry):
        if isinstance(entry, Wave):
            wave = entry
            name = entry.name()
        else:
            wave = self.appWaves().wave(entry)
            name = entry
        self.orderedWaveNames().append(name)
        wave.nameChanged.connect(self.updateOrderedWaves, Qt.UniqueConnection)
        
        self.reset()

    def rowCount(self, parent=QModelIndex()):
        return len(self.orderedWaveNames())

    def index(self, row, column=0, parent=QModelIndex()):
        if row > self.rowCount():
            return self.createIndex(row, column, parent)
        return self.createIndex(row, column, self.waveByRow(row))

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid() and index.row() < self.rowCount() and role == Qt.DisplayRole:
            return str(self.waveNameByRow(index.row()))
        return None

    def flags(self, index):
        defaultFlags = Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled
        if index.isValid():
            return Qt.ItemIsDragEnabled | defaultFlags
        else:
            return Qt.ItemIsDropEnabled | defaultFlags

    def setData(self, index, value, role=Qt.EditRole):

        if index.isValid() and role == Qt.DisplayRole and index.row() < self.rowCount():
            waveName = str(value.toString())
            self.orderedWaveNames()[index.row()] = waveName
            self.dataChanged.emit(index, index)
            return True
        return False

    def insertRows(self, row, count, parent=QModelIndex()):
        self.beginInsertRows(parent, row, row + count - 1)
        for i in range(count):
            self.orderedWaveNames().insert(row, "")
        self.endInsertRows()
        return True

    def removeRow(self, row, parent=QModelIndex()):
        return self.removeRows(row, 1, parent)

    def removeRows(self, row, count, parent=QModelIndex()):
        self.beginRemoveRows(parent, row, row + count - 1)
        numRowsRemoved = 0
        for i in range(count):
            if self.orderedWaveNames().pop(row):
                numRowsRemoved += 1
        self.endRemoveRows()
        return numRowsRemoved == count

    def supportedDropActions(self):
        return Qt.MoveAction

    def removeWave(self, entry):
        """
        Remove all instances of entry from the model.
        """

        if isinstance(entry, Wave):
            wave = entry
            name = entry.name()
        #elif isinstance(entry, QVariant):
        #    name = str(entry.toString())
        #    wave = self.appWaves().wave(name)
        else:
            name = entry
            wave = self.appWaves().wave(name)

        if name not in self.orderedWaveNames():
            # wave does not exist in this model
            return
        
        wave.nameChanged.disconnect(self.updateOrderedWaves)

        while True:
            try:
                self.orderedWaveNames().remove(name)
            except:
                break
        self.doReset()

    def removeAllWaves(self):
        for waveName in self.orderedWaveNames():
            try:
                self.appWaves().wave(waveName).nameChanged.disconnect(self.updateOrderedWaves)
            except:
                pass
        self._orderedWaveNames = []

    def doReset(self, *args):
        self.reset()

