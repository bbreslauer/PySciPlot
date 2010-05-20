from PyQt4.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant, QString, pyqtSignal

class TraceListModel(QAbstractTableModel):
    """
    All the data that corresponds to traces in a figure are displayed based on this model.
    
    Signals that are emitted from this class are:
        traceAdded   - emitted when a trace is added to the list
        traceRemoved - emitted when a trace is removed from the list
    """

    traceAdded   = pyqtSignal()
    traceRemoved = pyqtSignal()


    def __init__(self, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self._parent = parent
        self._data = []
        self._columnNames = ['X', 'Y']
       
        # Connect signals
        self.traceAdded.connect(self.doReset)
        self.traceRemoved.connect(self.doReset)
        self.dataChanged.connect(self.doReset)

    def rowCount(self, parent=QModelIndex()):
        """Return the number of traces in all the plots in the figure."""
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        """Return the number of columns."""
        return len(self._columnNames)

    def headerData(self, section, orientation, role):
        """Return the header for the given section and orientation."""

        if orientation == Qt.Horizontal and section < self.columnCount() and role == Qt.DisplayRole:
            return QVariant(QString(self._columnNames[section]))
        return QVariant()
    
    def data(self, index, role):
        """Return the data for the given index."""

        if index.isValid() and role == Qt.DisplayRole:
            return QVariant(self._data[index.row()].columnValue(index.column()))
        else:
            return QVariant()
            
    def clearData(self):
        """Reset data array to a blank list."""
        self._data = []

    def flags(self, index):
        """Return the flags for the given index."""

        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable
    
    def doReset(self, *args):
        "doing"
        self.reset()

    def addEntry(self, entry):
        self._data.append(entry)
        self.dataChanged.emit(self.index(len(self._data)-1, 0), self.index(len(self._data)-1, 2))
        return True

    def getTraceListEntryByRow(self, row):
        return self._data[row]

