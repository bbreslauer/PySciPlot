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

    def rowCount(self, parent=QModelIndex()):
        return len(self._waves.waves())

    def index(self, row, column, parent=QModelIndex()):
        if row > self._waves.length():
            return self.createIndex(row, column, parent)
        return self.createIndex(row, column, self._waves.waves()[row])
    
    def data(self, index, role):
        if index.isValid() and role == Qt.DisplayRole:
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

            
    def doReset(self, *args):
        self.reset()

