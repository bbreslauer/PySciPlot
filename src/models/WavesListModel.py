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


from PyQt4.QtCore import QModelIndex, Qt, QVariant, QString
from PyQt4.QtGui import QStringListModel

from Wave import Wave
from Waves import Waves

class WavesListModel(QStringListModel):
    """
    A model for a list of waves.
    """
    
    def __init__(self, wavesIn=Waves(), parent=None, *args):
        QStringListModel.__init__(self, parent, *args)
        self._waves = wavesIn

        # Connect signals
        self._waves.waveAdded.connect(self.doReset)
        self._waves.waveRenamed.connect(self.doReset)
        self._waves.waveRemoved[Wave].connect(self.doReset)

    def waves(self):
        return self._waves

    def waveByRow(self, row):
        return self.waves().waves()[row]

    def getIndexByWaveName(self, name):
        wave = self.waves().getWaveByName(name)
        index = self.waves().waves().index(wave)
        return index

    def appendRow(self, wave):
        self._waves.addWave(wave)

    def rowCount(self, parent=QModelIndex()):
        return len(self._waves.waves())

    def index(self, row, column=0, parent=QModelIndex()):
        if row > self._waves.length():
            return self.createIndex(row, column, parent)
        return self.createIndex(row, column, self.waves().waves()[row])
    
    def data(self, index, role = Qt.DisplayRole):
        if index.isValid() and index.row() < self.rowCount() and role == Qt.DisplayRole:
            return QVariant(QString(self._waves.waves()[index.row()].name()))
        else:
            return QVariant()

    def setData(self, index, value, role):
        """Change the name for the wave at index."""
        newName = str(value.toString())
        if index.isValid() and role == Qt.EditRole and self._waves.waves()[index.row()]:
            # Do not allow for blank wave names
            if Wave.validateWaveName(newName) == "":
                return False
            self._waves.waves()[index.row()].setName(newName)
            return True
        return False

    def removeWave(self, name):
        self._waves.removeWave(name)

    def removeAllWaves(self):
        self._waves.removeAllWaves()

    def doReset(self, *args):
        self.reset()

