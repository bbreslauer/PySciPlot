import Util

from PyQt4.QtCore import QObject, pyqtSignal

from pylab import nan

class Wave(QObject):
    """
    Store the name and all data for one wave.

    All data entries must be either a valid data type or a blank string.

    Data types:
        Integer (long)
        Decimal (float)
        String  (str)

    Signals that are emitted from this class are:
        nameChanged  - emitted when the name of the wave is changed
        dataModified - emitted when any data in the wave is changed
    """

    # Signals
    nameChanged = pyqtSignal()
    dataModified = pyqtSignal()

    def __init__(self, waveName, dataType="Decimal", dataIn=[]):
        """
        Initialize a wave. Set name to waveName and data to dataIn.
        
        waveName is a string to define the name of the wave.
        dataIn is a list of numbers that populates the internal Wave data.  Default is an empty list.
        """

        QObject.__init__(self)

        Util.debug(2, "Wave.init", "Creating wave " + waveName)

        self._data = []
        self._name = ""
        self._dataType = dataType

        if self.setName(waveName):
            if dataIn == []:
                pass
                #self._data.append(0)
            else:
                self._data.extend(map(self.convertValueToDataType, dataIn))
        
        Util.debug(1, "Wave.init", "Created wave " + self._name)

    def __str__(self):
        return "%s (%s): %s\n" % (self._name, self._dataType, self._data)

    def data(self):
        """Return the data list."""
        return self._data

    def name(self):
        """Return the name of the wave."""
        return str(self._name)
    
    def dataType(self):
        """Return the type of data that can be stored in the wave."""
        return str(self._dataType)

    def validValue(self, value):
        """Determine whether a given value is acceptable for this wave."""
        valueType = type(value)

        if self._dataType == "Integer":
            return valueType in [int, long]
        elif self._dataType == "Decimal":
            return valueType == float
        elif self._dataType == "String":
            return valueType == str
        return False

    def convertValueToDataType(self, value):
        newValue = ''

        try:
            if self._dataType == "Integer":
                newValue = long(float(value))
            elif self._dataType == "Decimal":
                newValue = float(value)
            elif self._dataType == "String":
                newValue = str(value)
        except ValueError:
            pass
        return newValue

    def goodValue(self, value):
        """Determine whether a value is a valid data type."""
        return self.validValue(value) or (value == '')

    # Modifying methods
    def setName(self, name):
        """
        Convert a string into a valid wave name and name the wave with that string.  Once the wave name has been set, return the current name.

        Emits the nameChanged signal upon successfully changing the name.
        """

        validName = Wave.validateWaveName(name)
        if validName != self._name and validName != "":
            Util.debug(2, "Wave.setName", "Changed wave name from " + str(self._name) + " to " + str(validName))
            self._name = validName
            self.nameChanged.emit()
        return self._name

    def setData(self, position, value):
        """
        Set the entry at position to value.  value must be a valid data type.  position is the zero-based index in the list of data, and so it must be greater than or equal to zero.  If position is larger than the length of the data, then empty strings are added to fill the extra space.  Return True if data was successfully set, False otherwise.

        Emits the dataModified signal if the data is changed.
        """

        if position >= 0:
            if value != "":
                value = self.convertValueToDataType(value)
            if value:
                if position > len(self._data):
                    # extend the list enough so that we can modify the value at position
                    # +1 because list[len(list)] doesn't exist, due to zero-indexing
                    self._data.extend([''] * (position - len(self._data) + 1))
                self._data[position] = value
                Util.debug(3, "Wave.setData", "Changed data at position " + str(position) + " in wave " + str(self._name))
                self.dataModified.emit()
                return True
        return False

    def recastData(self):
        """
        Cast all data to the current type.  This is useful if the data might be in another type, for instance if the type was just changed.
        """

        for i, v in enumerate(self._data):
            self._data[i] = self.convertValueToDataType(v)

        Util.debug(2, "Wave.recastData", "Recast all data in " + str(self._name) + " to " + str(self._dataType) + " type")

    def insert(self, position, value):
        """
        Insert value at position.  value must be a valid data type.

        Emits the dataModified signal if the data is changed.
        """
        
        if position >= 0:
            if value != "":
                value = self.convertValueToDataType(value)
            if self.goodValue(value):
                self._data.insert(position, value)
                Util.debug(2, "Wave.insert", "Inserted data into wave " + str(self._name))
                self.dataModified.emit()
                return True
        return False

    def extend(self, values):
        """
        Extend the wave data by appending all values to the wave.  Equivalent to running Wave.push() for each entry in values.  Returns True if any value is successfully added.

        Emits the dataModified signal for each value in values that is changed.
        """
        result = True
        for value in values:
            result = result and self.push(value)
        Util.debug(2, "Wave.extend", "Extended wave " + str(self._name) + " with " + str(len(values)) + " entries")
        return result

    def push(self, value):
        """
        Append value to wave data. value must be a valid data type.  Returns True if append succeeded, False otherwise.  Equivalent to Wave.insert(len(self.data()), value).

        Emits the dataModified signal.
        """
        return self.insert(len(self._data), value)

    def pop(self, position=-1):
        """
        Remove the value at position from the wave data and return it.  If position is not specified, Remove the last item.
        
        Emits the dataModified signal.
        """
        
        value = self._data.pop(position)
        Util.debug(2, "Wave.pop", "Popped value at position " + str(position) + " from " + str(self._name))
        self.dataModified.emit()
        return value

    def shift(self):
        """
        Remove the first entry in the wave data and return it.  Equivalent to Wave.pop(0).

        Emits the dataModified signal.
        """
        return self.pop(0)

    def unshift(self, value):
        """
        Insert value at the beginning of the wave data.  Returns True if append succeeded, False otherwise.  Equivalent to Wave.insert(0, value)

        Emits the dataModified signal.
        """
        return self.insert(0, value)

    def setDataType(self, dataType):
        """
        Set the type of data that is allowed for this wave.
        """
        
        self._dataType = dataType

        Util.debug(2, "Wave.setDataType", "Changed data type to " + str(self._dataType) + " for wave " + str(self._name))

        # Now convert all the current data in the wave to the new type
        self.recastData()

    def replaceData(self, values):
        """
        Replaces all the data in the wave.  Equivalent to removing all the data followed by Wave.extend, but more efficient.

        Emits the dataModified signal.
        """
        
        self._data = []
        for value in values:
            self._data.append(value)
        self.recastData()
        
        self.dataModified.emit()



    ##################
    # STATIC METHODS #
    ##################
    @staticmethod
    def getName(wave):
        """Return the name of the given wave.  This is a static method."""
        return wave._name

    @staticmethod
    def validateWaveName(waveName):
        """
        Make any necessary conversions to turn a string into a valid wave name.

        If a valid string is passed into this function, the output will necessarily be the same string.

        Currently, these conversions are:
        1) Remove leading and trailing spaces
        2) Replace 4 simple binary math operations (+-*/) with underscores
        3) Replace all whitespace with underscores
        4) Replace any <> with ()
        """

        waveName = waveName.strip()
        waveName = waveName.replace(" ","_")
        waveName = waveName.replace("+","_")
        waveName = waveName.replace("-","_")
        waveName = waveName.replace("*","_")
        waveName = waveName.replace("/","_")
        waveName = waveName.replace("<","(")
        waveName = waveName.replace(">",")")
        return waveName

    @staticmethod
    def convertToFloatList(wave):
        """
        Convert all int, long, or float entries in data list to floats.  If an entry is not a number (or is complex), use pylab.nan type.  Return list of floats.
        """

        numberData = []
        for entry in wave.data():
            if wave.validValue(entry):
                numberData.append(entry)
            else:
                numberData.append(nan)
        
        return numberData

