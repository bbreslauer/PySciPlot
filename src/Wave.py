# Copyright (C) 2010-2011 Ben Breslauer
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import Util

from PySide.QtCore import QObject, Signal
from numpy import nan

class Wave(QObject):
    # Initialized solely for the signal definition below.
    pass

class Wave(QObject):
    """
    Store the name, type of data, and all data for one wave.

    All data entries must be either a valid data type or a blank (string).

    Data types -- Internal name (Python type):
        Integer (long)
        Decimal (float)
        String  (str)

    Signals that are defined in this class are:
        nameChanged  - emitted when the name of the wave is changed. Args are old name, current wave (self).
        dataModified - emitted when any data in the wave is changed
    """

    # Signals
    nameChanged = Signal(str, Wave)
    dataModified = Signal()
    lengthChanged = Signal()

    def __init__(self, waveName, dataType="Decimal", dataIn=[]):
        """
        Initialize a wave.

        Arguments:
        waveName (str) -- The name of the wave.
        dataType (str) -- The type of data that the wave contains (default: 'Decimal').
        dataIn (list) -- The initial data that the wave will contain. Entries are of type dataType (default: []).
        """

        QObject.__init__(self)

        Util.debug(2, "Wave.init", "Creating wave " + waveName)

        self._data = []
        self._name = ""
        self.setDataType(dataType)

        if self.setName(waveName):
            if dataIn == []:
                pass
            else:
                self._data.extend(map(self.castToWaveType, dataIn))
        
        Util.debug(1, "Wave.init", "Created wave " + self.name())

    def __str__(self):
        """
        Return a string representation of the wave.

        Returns:
        str -- Representation of the wave.
        """

        return "%s (%s, %s): %s\n" % (self._name, self._dataType, len(self._data), self._data)

    def __reduce__(self):
        return tuple([self.__class__, tuple([self.name(), self.dataType(), self.data()])])

    def data(self, start=None, end=None):
        """
        Return a slice of the wave's internal data. Defaults to returning all
        the wave's data.
        
        Arguments:
        start (int) -- Starting index of the data (default: None).
        end (int) -- Ending index of the data (default: None).

        Returns:
        list -- Wave data from, and including, start to, but not including, end.
        """

        return self._data[start:end]

    def length(self):
        """
        Return the length of the wave.

        Returns:
        int -- Length of wave data.
        """

        return len(self._data)

    def name(self):
        """
        Return the name of the wave.

        Returns:
        str -- Name of the wave.
        """

        return str(self._name)
    
    def dataType(self):
        """
        Return the internal data type that can be stored in the wave.
        
        Returns:
        str -- Internal data type.
        """

        return str(self._dataType)

    def validValue(self, value):
        """
        Determine whether a given value is acceptable for this wave.
        
        This method will determine whether the passed argument is compatible
        with the data type of this wave. An empty string is valid for any type
        of wave.

        Arguments:
        value (any) -- The value that needs to be tested.

        Returns:
        True -- If value is compatible with the wave's type
        False -- If value is incompatible with the wave's type.
        """

        if str(value).strip() == "":
            return True

        valueType = type(value)

        if self.dataType() == "Integer":
            return valueType in [int, long]
        elif self.dataType() == "Decimal":
            return valueType == float
        elif self.dataType() == "String":
            return valueType == str
        return False

    def castToWaveType(self, value):
        """
        Cast value to wave's data type.

        Arguments:
        value (any) -- The value to be cast.

        Returns:
        Wave.castValue(value, self.dataType())
        """

        return Wave.castValue(value, self.dataType())
    
    ####
    # Modifying methods
    ####
    def setName(self, name):
        """
        Convert a string into a valid wave name and name the wave with that
        string.
        
        Arguments:
        name (str) -- user-defined wave name.

        Returns:
        str -- The (now new) name of the wave.

        Emits:
        nameChanged -- If the name has been successfully changed (i.e. newName
        != oldName).
        """

        validName = Wave.validateWaveName(name)
        if validName != self.name():
            oldName = self.name()
            self._name = validName
            Util.debug(2, "Wave.setName", "Changed wave name from " + str(oldName) + " to " + str(validName))
            self.nameChanged.emit(oldName, self)
        return self.name()

    def setData(self, position, value):
        """
        Set the data at position to value.
        
        If position is less than zero, then nothing is done and False is
        returned. If position is greater than the length of the wave, then empty
        data points are added to pad the wave.

        Arguments:
        position (int) -- Zero-based index of the wave data to be replaced.
        value (dataType) -- New datum for the wave.

        Returns:
        True -- If data is successfully set.
        False -- If wave is not changed.

        Emits:
        dataModified -- If the data has been changed.
        """

        if position < 0:
            return False

        value = self.castToWaveType(value)
        if value == None:
            return False
        
        # We are adding data to the list
        if position >= self.length():
            # If we are editing the end of the list (or beyond) and we are entering a blank entry, don't extend the list
            if value == "":
                return False

            # Extend the list enough so that we can modify the value at position
            # +1 because list[len(list)] doesn't exist, due to zero-indexing
            self._data.extend([''] * (position - self.length() + 1))
            self.lengthChanged.emit()

        self._data[position] = value
        Util.debug(3, "Wave.setData", "Set " + str(self.name()) + "[" + str(position) + "] = " + str(value))
        self.dataModified.emit()
        return True

    def recastData(self):
        """
        Cast all data to the current type.
        
        This is useful if the data might be in another type, for instance if
        the type was just changed.

        Arguments:
        None

        Returns:
        None
        """

        for i, v in enumerate(self.data()):
            self._data[i] = self.castToWaveType(v)

        self.dataModified.emit()

        Util.debug(2, "Wave.recastData", "Recast all data in " + str(self.name()) + " to " + str(self.dataType()) + " type")

    def insert(self, position, value):
        """
        Insert value at position.
        
        position must be >= 0. Unlike a list, positions less than 0 are
        invalid. value will be cast to the wave's type before being inserted.
        positions greater than len(wave) will be appended.

        Arguments:
        position (int) -- Zero-based index of the location to insert into.
        value (dataType) -- New datum for the wave.

        Returns:
        True -- If data is successfully set.
        False -- If wave is not changed.

        Emits:
        dataModified -- If the data has been changed.
        """
        
        if position < 0:
            return False
        
        value = self.castToWaveType(value)
        if value == None:
            return False

        self._data.insert(position, value)
        Util.debug(2, "Wave.insert", "Inserted data into wave " + str(self.name()))
        self.dataModified.emit()
        self.lengthChanged.emit()
        return True

    def extend(self, values):
        """
        Extend the wave data by appending all values to the wave. Equivalent to
        running Wave.push() for each entry in values. If a non-(list, dataType)
        value is encountered, skip it and continue through values.

        Arguments:
        values (list-of-(list-of*)-dataType) -- List of data to be pushed onto the wave.
                Can contain nested lists, which will be flattened.

        Returns:
        True -- If at least one entry in values is added to the wave.
        False -- If no entry in values is added to the wave.

        Emits:
        dataModified -- If the data has been changed.
        """

        result = True
        for value in values:
            if isinstance(value, list):
                result = self.extend(value) and result
            else:
                result = self.push(value) and result
        Util.debug(2, "Wave.extend", "Extended wave " + str(self.name()) + " with " + str(len(values)) + " entries")
        return result

    def push(self, value):
        """
        Append value to wave data. Equivalent to
        Wave.insert(self.length(), value).

        Arguments:
        value (dataType) -- New datum for the wave.

        Returns:
        True -- If data is successfully set.
        False -- If wave is not changed.

        Emits:
        dataModified -- If the data has been changed.
        """

        return self.insert(self.length(), value)

    def pop(self, position=-1):
        """
        Remove the value at position from the wave data and return it.  If
        position is not specified, remove the last item.
        
        Arguments:
        position (int) -- Zero-based index to remove data at.

        Returns:
        dataType -- Popped value.

        Emits:
        dataModified -- If the data has been changed.
        """
        
        value = self._data.pop(position)
        Util.debug(2, "Wave.pop", "Popped value at position " + str(position) + " from " + str(self.name()))
        self.dataModified.emit()
        self.lengthChanged.emit()
        return value

    def shift(self):
        """
        Remove the first entry in the wave data and return it.  Equivalent to Wave.pop(0).

        Returns:
        dataType -- First entry in the wave.

        Emits:
        dataModified -- If the data has been changed.
        """
        return self.pop(0)

    def unshift(self, value):
        """
        Insert value at the beginning of the wave data. Equivalent to
        Wave.insert(0, value)

        Arguments:
        value (dataType) -- New datum for the wave.

        Returns:
        True -- If data is successfully set.
        False -- If wave is not changed.

        Emits:
        dataModified -- If the data has been changed.
        """

        return self.insert(0, value)

    def setDataType(self, dataType):
        """
        Set the type of data that is allowed for this wave. Also recasts the
        wave's data to the new type.

        Arguments:
        dataType (str) -- Internal data type for the wave.

        Returns:
        None

        Emits:
        dataModified -- If the data has been changed.
        """
        
        self._dataType = dataType

        Util.debug(2, "Wave.setDataType", "Changed data type to " + str(self.dataType()) + " for wave " + str(self.name()))

        # Now convert all the current data in the wave to the new type
        self.recastData()

    def replaceData(self, values):
        """
        Replaces all the data in the wave.  Equivalent to removing all the data followed by Wave.extend, but more efficient.

        Arguments:
        values (list-of-dataType) -- New data for the wave.

        Returns:
        None

        Emits:
        dataModified -- If the data has been changed.
        """
        
        self._data = []
        for value in values:
            self._data.append(value)
        self.recastData()
        
        self.dataModified.emit()
        self.lengthChanged.emit()



    ##################
    # STATIC METHODS #
    ##################
    @staticmethod
    def getName(wave):
        """
        Return the name of the given wave.
    
        Arguments:
        wave (Wave) -- Wave to get the name of.

        Returns:
        str -- Name of the given wave.
        """

        return wave.name()

    @staticmethod
    def validateWaveName(waveName):
        """
        Make any necessary conversions to turn a string into a valid wave name.

        If a valid string is passed into this function, the output will be the
        same string. If an empty string is going to be returned, the returned
        value will instead be "Wave".

        Currently, these conversions are:
        1) Remove leading and trailing spaces
        2) Replace 4 simple binary math operations (+-*/) with underscores
        3) Replace all whitespace with underscores
        4) Replace any <> with ()
        5) If the result is blank, change name to "Wave"

        Arguments:
        waveName (str) -- User-defined name for the wave.

        Returns:
        str -- valid wave name.
        """

        waveName = str(waveName)
        waveName = waveName.strip()
        waveName = waveName.replace(" ","_")
        waveName = waveName.replace("+","_")
        waveName = waveName.replace("-","_")
        waveName = waveName.replace("*","_")
        waveName = waveName.replace("/","_")
        waveName = waveName.replace("<","(")
        waveName = waveName.replace(">",")")
        
        if waveName == "":
            waveName = "Wave"

        return waveName

    @staticmethod
    def convertToFloatList(wave):
        """
        Convert all int, long, or float entries in data list to floats.  If an
        entry is not a number (or is complex), use pylab.nan type.  Return list
        of floats.

        Arguments:
        wave (Wave) -- The wave whose data is to be converted.

        Returns:
        list-of-floats -- List of all the data in the wave, after conversion to float.
        """

        numberData = []
        for datum in wave.data():
            try:
                numberData.append(float(datum))
            except ValueError:
                numberData.append(nan)

        return numberData

    @staticmethod
    def castValue(value, dataType):
        """
        Convert value to the specified data type.

        If value is a QObject, it will never be valid and this method will
        return None immediately. If value is empty (str(value) is only spaces)
        then return an empty string (this covers blank values in a wave). Then
        try to cast the value to the appropriate type.

        Arguments:
        value (any) -- The value to be converted.
        dataType (str) -- The internal data type to convert the value to.

        Returns:
        None if value is a QObject or cannot be cast.
        An empty string if value contains nothing or only spaces.
        value cast to the Python type defined by dataType.
        """

        newValue = None

        # We might get QVariants or other QT objects occasionally, and we want
        # to discard them
        if isinstance(value, QObject):
            return None

        # Cannot cast an empty value (only spaces) to a long or float, so
        # we're taking care of this case early. We return an empty string.
        if str(value).strip() == "":
            return str("")
        
        # Now try to cast the value
        try:
            if dataType == "Integer":
                newValue = long(float(value))
            elif dataType == "Decimal":
                newValue = float(value)
            elif dataType == "String":
                newValue = str(value)
        except ValueError:
            # Cast failed
            newValue = None
        except TypeError:
            # Cast failed
            newValue = None

        Util.debug(3, "Wave.castValue", "Converting value " + str(value) + " to type " + str(dataType) + " (" + str(newValue) + ")")
        return newValue

