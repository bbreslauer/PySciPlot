from PyQt4.QtCore import QModelIndex, Qt, QVariant, QString
from PyQt4.QtGui import QStringListModel
from Waves import Waves

class WavesListModel(QStringListModel):
    def __init__(self, wavesIn=Waves(), parent=None, *args):
        QStringListModel.__init__(self, parent, *args)
        self.listdata = wavesIn

    def rowCount(self, parent=QModelIndex()):
        return len(self.listdata)
    
    def data(self, index, role):
        if index.isValid() and role == Qt.DisplayRole:
            return QVariant(QString(self.listdata[index.row()].getName()))
        else:
            return QVariant()
            
