from PyQt4.QtCore import QAbstractTableModel, QVariant, Qt, SIGNAL, QModelIndex,  QString
from Waves import Waves

class DataTableModel(QAbstractTableModel):
    def __init__(self, wavesIn=[], parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mainWindow = parent
        self.waves = Waves([], self)
        for wave in wavesIn:
            self.waves.append(wave)
        
        # This makes sure that all entries in the table are editable
        self.addBlanksToWaves()
        
    def rowCount(self, parent = QModelIndex()):
        if (len(self.waves) == 0):
            return 0
        _max = 0
        for wave in self.waves:
            if (len(wave) > _max):
                _max = len(wave)
        return _max

    def columnCount(self, parent = QModelIndex()):
        return len(self.waves)

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        elif index.column() >= len(self.waves):
            return QVariant()
        elif index.row() >= len(self.waves[index.column()]):
            return QVariant()
        elif self.waves[index.column()][index.row()] == "":
            return QVariant()
        return QVariant(self.waves[index.column()][index.row()])

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and section < len(self.waves) and role == Qt.DisplayRole:
            return QVariant(QString(self.waves[section].getName()))
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return QVariant(section)
        return QVariant()

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable
        
    def setData(self, index, value, role):
        if index.isValid() and role == Qt.EditRole:
            # Check if value can be converted to double
            if value.toDouble()[1]:
                self.waves[index.column()][index.row()] = value.toDouble()[0]
                self.reset()
                if (self.rowCount(self) == (index.row() + 1)):
                    self.insertRows(self.rowCount(self), 1, index)
                self.mainWindow.emit(SIGNAL("waveUpdated"), self.waves[index.column()])
                self.emit(SIGNAL("dataChanged(PyQt_PyObject, PyQt_PyObject)"),  index,  index)
                return True
        return False
            
    def addBlanksToWaves(self):
        for wave in self.waves:
            _tmp = wave.pop()
            while _tmp == "":
                _tmp = wave.pop()
            wave.append(_tmp)
            
        _rows = self.rowCount(self)
        for wave in self.waves:
            wave.extend([""] * (_rows - len(wave) + 1))
        
    def insertRows(self, position, rows, index):
        self.beginInsertRows(QModelIndex(), position, position+rows-1)
        for i in range(rows):
            for wave in self.waves:
                wave.insert(position, "")
        self.endInsertRows()
        return True

    # the waves rename automatically, because the waves in this model are the same (they
    # have the same reference) as the waves in the main application
    def checkWaveRenamed(self, wave):
        self.reset()
    
    def checkWaveUpdated(self, wave):
        self.reset()
    
    def checkWaveRemoved(self, wave):
        self.removeColumn(wave)
        self.reset()
    
    def checkColumnsRemoved(self):
        self.reset()
        
    def checkColumnsAdded(self):
        self.reset()

    def addColumn(self, wave):
        self.beginInsertColumns(QModelIndex(), len(self.waves), len(self.waves)+1)
        self.waves.append(wave)
        self.endInsertColumns()
        self.addBlanksToWaves()
        self.mainWindow.emit(SIGNAL("columnsAdded"))
        return True

    def insertColumn(self, position, wave):
        return self.insertColumns(position, Waves([wave]))

    def insertColumns(self, position, waves):
        self.beginInsertColumns(QModelIndex(), position, len(self.waves))
        for wave in waves:
            self.waves.insert(position, waves.pop())
        self.endInsertColumns()
        self.addBlanksToWaves()
        self.mainWindow.emit(SIGNAL("columnsAdded"))
        return True
        
    def removeColumn(self, wave):
        return self.removeColumns(Waves([wave]))
        
    def removeColumns(self, waves):
        self.beginRemoveColumns(QModelIndex(), 0, len(self.waves))
        for wave in waves:
            self.waves.removeWave(wave)
        self.endRemoveColumns()
        self.mainWindow.emit(SIGNAL("columnsRemoved"))
        return True

    def moveColumn(self,  fromIndex,  toIndex):
        if (fromIndex < 0 or fromIndex > len(self.waves) or toIndex < 0 or toIndex > len(self.waves)):
            return False
        tmpWave = self.waves.pop(fromIndex)
        self.waves.insert(toIndex,  tmpWave)
        self.reset()
        return True

    def printColumns(self):
        for wave in self.waves:
            print wave.getName()















