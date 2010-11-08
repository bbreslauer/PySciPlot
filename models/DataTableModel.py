from PyQt4.QtCore import QAbstractTableModel, QVariant, Qt, QModelIndex, QString, pyqtSignal

import Util
from Wave import Wave
from Waves import Waves

class DataTableModel(QAbstractTableModel):
    """
    This is the data model for a table.
    
    A DataTableModel object contains links to all the Wave objects that are displayed in the associated view.

    Signals that are emitted from this class are:
    """

    # Signals
    dataChanged = pyqtSignal(QModelIndex, QModelIndex)
    
    def __init__(self, wavesIn=[], parent=None, *args):
        """
        Initialize a table model.  Add the initial set of wave(s) to the model.

        wavesIn is a list of Wave objects that should be initially added to the table.
        parent is the parent QT object.
        *args is anything other arguments that should be passed to the superclass constructor.
        """

        QAbstractTableModel.__init__(self, parent, *args)

        self._waves = Waves()

        for wave in wavesIn:
            self.addColumn(wave)

        # Connect signals from waves object
        self._waves.waveAdded.connect(self.doReset)
        self._waves.waveRemoved[Wave].connect(self.doReset)
        if parent:
            parent.waves().waveRemoved[Wave].connect(self.removeColumn)
        
    def rowCount(self, parent = QModelIndex()):
        """Return the number of rows."""

        if (len(self._waves.waves()) == 0):
            return 0

        rows = 0
        for wave in self._waves.waves():
            if (len(wave.data()) > rows):
                rows = len(wave.data())
        return rows + 1 # Want the extra row for adding more rows of data

    def columnCount(self, parent = QModelIndex()):
        """Return the number of columns."""

        return len(self._waves.waves())

    def data(self, index, role = Qt.DisplayRole):
        """Return the data at position index with the given role."""

        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole and role != Qt.EditRole:
            return QVariant()
        elif index.column() >= len(self._waves.waves()):
            return QVariant()
        elif index.row() >= len(self._waves.waves()[index.column()].data()):
            return QVariant()
        elif self._waves.waves()[index.column()].data()[index.row()] == "":
            return QVariant()
        #
        # If we return long() or float() instead of str(), then the view uses a spinbox
        # and we cannot easily return to a blank entry
        elif 'Integer' == self._waves.waves()[index.column()].dataType():
            return str(self._waves.waves()[index.column()].data()[index.row()])
        elif 'Decimal' == self._waves.waves()[index.column()].dataType():
            return str(self._waves.waves()[index.column()].data()[index.row()])
        elif 'String' == self._waves.waves()[index.column()].dataType():
            return str(self._waves.waves()[index.column()].data()[index.row()])
        return QVariant()

    def headerData(self, section, orientation, role):
        """
        Return the given header text for the specified role and section in the orientation.

        orientation is either horizontal (column headers) or vertical (row headers).
        """

        if orientation == Qt.Horizontal and section < len(self._waves.waves()) and role == Qt.DisplayRole:
            return QVariant(QString(self._waves.waves()[section].name()))
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return QVariant(section)
        return QVariant()

    def flags(self, index):
        """Return the flags for the item at the given index."""

        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable
    
    def waves(self):
        return self._waves


    # Modifying methods
    def addColumn(self, wave):
        """Add a column (wave) to the end of the table.  Return True if the column is added, False otherwise."""

        return self.insertColumn(len(self._waves.waves()), wave)

    def insertColumn(self, position, wave):
        """Insert a column (wave) after the column described by position.  Return True if the column is added, False otherwise."""
        
        if self._waves.insertWave(position, wave):
            wave.nameChanged.connect(self.doReset)
            wave.dataModified.connect(self.doReset)
            return True
        return False

    def insertRows(self, position, rows, index):
        """
        Insert blank rows in all waves in the table.  Return True.
        """

        for wave in self._waves.waves():
            for i in range(rows):
                wave.insert(position, "")
        return True

    def moveColumn(self, fromIndex, toIndex):
        """
        Move a column for position fromIndex to position toIndex in the _waves object.  This method is intended to be called when columns are dragged around in the table view.  This is done in the underlying data instead of in the QT objects because of bugs in QT's renumbering of logical indices (or lack thereof!) when columns are dragged around.

        Returns True if the column move was successful, False otherwise.
        """

        # Make sure indices are valid
        if (fromIndex < 0 or fromIndex > len(self._waves.waves()) or toIndex < 0 or toIndex > len(self._waves.waves())):
            return False

        if fromIndex == toIndex:
            return True

        # This works regardless of whether fromIndex is > or < toIndex
        tmpWave = self._waves.removeWave(self._waves.waves()[fromIndex].name())
        self._waves.insertWave(toIndex, tmpWave)
        return True

    def removeColumn(self, wave):
        """
        Remove the column (wave) given by wave.  Return True if the column is removed, False otherwise.
        """
        return self._waves.removeWave(wave.name())

    def setData(self, index, value, role):
        """
        Set the data at position index to value if the position is editable.  Return True if the data is set, False otherwise.

        Emits the Wave.dataModified signal if the data is changed.
        """

        result = False

        Util.debug(2, "DataTableModel.setData", "Setting data")

        if index.isValid() and role == Qt.EditRole:
            wave = self._waves.waves()[index.column()]

            # Disregard if there is no change
            if self.data(index) == value.toString():
                return False

            # Convert from QVariant to QString to str
            value = str(value.toString())

            Util.debug(2, "DataTableModel.setData", "Setting " + str(wave.name()) + "[" + str(index.row()) + "] to " + str(wave.convertValueToDataType(value)))
            result = wave.setData(index.row(), wave.convertValueToDataType(value))
            
            self.dataChanged.emit(index, index)

        return result

    def doReset(self, *args):
        """Take any number of arguments and just reset the model."""
        self.reset()

    
    # Helper function for debugging purposes
    def printColumns(self):
        for wave in self.waves:
            print wave.getName()















