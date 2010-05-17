from PyQt4.QtCore import QModelIndex, Qt, QVariant, QString
from PyQt4.QtGui import QStringListModel

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
        self._waves.waveRemoved.connect(self.doReset)

    def rowCount(self, parent=QModelIndex()):
        return len(self._waves.waves())
    
    def data(self, index, role):
        if index.isValid() and role == Qt.DisplayRole:
            return QVariant(QString(self._waves.waves()[index.row()].name()))
        else:
            return QVariant()
            
    def doReset(self, *args):
        self.reset()

