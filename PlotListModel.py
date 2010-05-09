from PyQt4.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant, QString, pyqtSignal

class PlotListModel(QAbstractTableModel):
    """
    All the data that corresponds to traces in a figure are displayed based on this model.
    
    Signals that are emitted from this class are:
        traceAdded   - emitted when a trace is added to the list
        traceRemoved - emitted when a trace is removed from the list
    """

    traceAdded   = pyqtSignal()
    traceRemoved = pyqtSignal()


    def __init__(self, figure, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self._parent = parent
        self._figure = figure
        self._columnNames = ['Row', 'Column', 'X', 'Y']
       
        # Connect signals
        self.traceAdded.connect(self.doReset)
        self.traceRemoved.connect(self.doReset)

    def rowCount(self, parent=QModelIndex()):
        """Return the number of traces in all the plots in the figure."""
        numTraces = 0
        for i in range(self._figure.numPlots()):
            numTraces += self._figure.getPlot(i).numTraces()
        return numTraces

    def columnCount(self, parent=QModelIndex()):
        """Return the number of plots in the figure."""
        return self._figure.numPlots()

    def headerData(self, section, orientation, role):
        """Return the header for the given section and orientation."""

        if orientation == Qt.Horizontal and section < self.columnCount() and role == Qt.DisplayRole:
            return QVariant(QString(self._columnNames[section]))
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return QVariant(section)
        return QVariant()
    
    def data(self, index, role):
        """Return the data for the given index."""

        if index.isValid() and role == Qt.DisplayRole:

            pass
            return QVariant(self.data[index.row()].columnValue(index.column()))
        else:
            return QVariant()
            
    def flags(self, index):
        """Return the flags for the given index."""

        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable
    
    def doReset(self, *args):
        "doing"
        self.reset()

