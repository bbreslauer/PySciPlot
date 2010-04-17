from PyQt4.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant, QString

from PlotListEntry import PlotListEntry

class PlotListModel(QAbstractTableModel):
    def __init__(self, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.parent = parent
        self.data = []

    def rowCount(self, parent=QModelIndex()):
        return len(self.data)
        
    def columnCount(self, parent=QModelIndex()):
        if (len(self.data) == 0):
            return 0
        return self.data[0].numColumns()
    
    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and section < self.columnCount() and role == Qt.DisplayRole:
            return QVariant(QString(self.data[0].columnName(section)))
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return QVariant(section)
        return QVariant()
    
    def data(self, index, role):
        if index.isValid() and role == Qt.DisplayRole:
            return QVariant(self.data[index.row()].columnValue(index.column()))
        else:
            return QVariant()
            
    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable
    
    def addPlotListEntry(self, ple):
        self.data.append(ple)
        self.reset()
        return True
    
    def getPlotListEntry(self, row):
        if row < self.rowCount():
            return self.data[row]
        return
    
    def getAllPlotListEntries(self):
        return self.data
        
