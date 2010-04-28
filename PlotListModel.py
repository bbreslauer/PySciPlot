from PyQt4.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant, QString, pyqtSignal

from PlotListEntry import PlotListEntry

class PlotListModel(QAbstractTableModel):
    """
    All the data that corresponds to plots in a figure are displayed based on this model.
    
    Signals that are emitted from this class are:
        plotAdded   - emitted when a plot is added to the list
        plotRemoved - emitted when a plot is removed from the list
    """

    plotAdded   = pyqtSignal()
    plotRemoved = pyqtSignal()


    def __init__(self, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.parent = parent
        self.data = []
        
        # Connect signals
        self.plotAdded.connect(self.doReset)
        self.plotRemoved.connect(self.doReset)

    def rowCount(self, parent=QModelIndex()):
        """Return the number of rows in this model."""
        return len(self.data)
        
    def columnCount(self, parent=QModelIndex()):
        """Return the number of columns in this model."""
        if (len(self.data) == 0):
            return 0
        return self.data[0].numColumns()
    
    def headerData(self, section, orientation, role):
        """Return the header for the given section and orientation."""

        if orientation == Qt.Horizontal and section < self.columnCount() and role == Qt.DisplayRole:
            return QVariant(QString(self.data[0].columnName(section)))
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return QVariant(section)
        return QVariant()
    
    def data(self, index, role):
        """Return the data for the given index."""

        if index.isValid() and role == Qt.DisplayRole:
            return QVariant(self.data[index.row()].columnValue(index.column()))
        else:
            return QVariant()
            
    def flags(self, index):
        """Return the flags for the given index."""

        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable
    
    def addPlotListEntry(self, ple):
        """Add an entry to the plot list."""

        self.data.append(ple)
        self.plotAdded.emit()
        return True
    
    def getPlotListEntry(self, row):
        """Return the plot list at the given row."""

        if row < self.rowCount():
            return self.data[row]
        return
    
    def doReset(self, *args):
        "doing"
        self.reset()

    def getAllPlotListEntries(self):
        return self.data
        
