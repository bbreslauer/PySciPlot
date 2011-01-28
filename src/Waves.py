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


from PyQt4.QtCore import QObject, pyqtSignal

import Util

from Wave import Wave

class Waves(QObject):
    """
    A list of Wave objects with some helper methods.

    A Waves object contains a list of Wave(s) and additional methods for making sure that the waves are unique.

    Signals that are emitted from this class are:
        waveAdded   - emitted when a Wave is added to the Waves object
        waveRemoved - emitted when a Wave is removed from the Waves object
    """

    # Signals
    waveAdded   = pyqtSignal(Wave)
    waveRemoved = pyqtSignal((), (Wave, ))
    waveRenamed = pyqtSignal()

    def __init__(self, wavesIn=[], uniqueNames=True):
        """
        Initialize a waves.  Add the initial set of wave(s) to the list.
        
        wavesIn is a list of Wave objects to be populated in the Waves object.
        uniqueNames determines whether the Wave objects in this Waves should have unique names.  Default is true.
        """

        QObject.__init__(self)

        Util.debug(1, "Waves.init", "Creating waves object")

        self._waves = []
        
        self._uniqueNames = uniqueNames
        for wave in wavesIn:
            self.addWave(wave)

    def __str__(self):
        string = "Waves:\n"
        for wave in self._waves:
            string += str(wave)
        return string

    def __reduce__(self):
        return tuple([self.__class__, tuple([self.waves(), self.uniqueNames()])])

    def waves(self):
        """Return the waves list."""
        return self._waves

    def length(self):
        """Return the number of waves."""
        return len(self._waves)

    def uniqueNames(self):
        """Return uniqueNames variable."""
        return self._uniqueNames

    def getWaveByName(self, name):
        """
        Return the wave with the given name, if it exists.  Return False if no such wave is found.
        """

        Util.debug(2, "Waves.getWaveByName", "Getting the wave with name " + str(name))

        for wave in self._waves:
            if Wave.getName(wave) == name:
                return wave
        return False

    def findGoodWaveName(self, baseName="Wave"):
        """
        Find an unused wave name in this Waves object and return that name.  If baseName is provided, then it will be used as the beginning of the name.
        """
        
        Util.debug(3, "Waves.findGoodWaveName", "Finding acceptable wave name with base " + str(baseName))

        allWaveNames = map(Wave.getName, self._waves)
        counter = 1
        while True:
            testName = str(baseName) + str(counter)
            if testName not in allWaveNames:
                Util.debug(3, "Waves.findGoodWaveName", "Found acceptable wave name: " + str(testName))
                return testName
            else:
                counter += 1

    def findGoodWaveNames(self, numWaves, baseName="Wave"):
        """
        Find numWaves unused wave names in this Waves object and return that name.  If baseName is provided, then it will be used as the beginning of the name.
        """
        allWaveNames = map(Wave.getName, self._waves)
        goodWaveNames = []
        counter = 1
        while numWaves > 0:
            testName = str(baseName) + str(counter)
            if testName not in allWaveNames:
                goodWaveNames.append(testName)
                allWaveNames.append(testName)
                counter += 1
                numWaves -= 1
            else:
                counter += 1
        return goodWaveNames

    def goodWaveName(self, name):
        """
        Determine if name is a good Wave name for this Waves object.  Returns False if name is an empty string.  If wave names can be duplicates, then return True.  If wave names must be unique and this name is, then return True.  Otherwise return False.
        """
        
        name = Wave.validateWaveName(name)
        if name == "":
            return False
        if self._uniqueNames:
            return self.uniqueWaveName(name)
        return True

    def uniqueWaveName(self, name):
        """Return True if name is neither an empty string nor an existing Wave name in this object.  Return False otherwise."""

        if name == "":
            return False
        for wave in self._waves:
            if name == wave.name():
                return False
        return True

    def uniqueWave(self, wave):
        """Return True if wave's name is neither an empty string nor an existing Wave name in this object.  Return False otherwise."""
        return self.uniqueWaveName(wave.name())

    def emitWaveRenamed(self):
        """Emit the wave renamed signal."""
        self.waveRenamed.emit()

    # Modifying methods
    def addWave(self, wave):
        """
        Add wave to list of waves.  Before doing so, check to see if this Waves needs unique wave names, and if so, check if the wave name is unique.  Return wave if wave is added, False otherwise.

        Emits the waveAdded signal if the wave is added.
        """
        Util.debug(2, "Waves.addWave", "Adding wave")
        return self.insertWave(len(self._waves), wave)

    def insertWave(self, position, wave):
        """
        Insert a wave at the given position.  Before doing so, check to see if this Waves needs unique wave names, and if so, check if the wave name is unique.   Return wave if insert succeeded, False otherwise.

        Emits the waveAdded signal if the wave was added.
        """

        if self._uniqueNames and not self.uniqueWave(wave):
            return False
        Util.debug(2, "Waves.insertWave", "Inserting wave " + str(wave.name()) + " at position " + str(position))
        self._waves.insert(position, wave)
        wave.nameChanged.connect(self.emitWaveRenamed)
        self.waveAdded.emit(wave)
        return wave

    def insertNewWave(self, position):
        """
        Create a new wave and insert it at the given position.  Return wave if insert succeeded, False otherwise.

        Emits the waveAdded signal if the wave is added.
        """
        Util.debug(2, "Waves.insertNewWave", "Inserting new wave")
        return self.insertWave(position, Wave(self.findGoodWaveName()))

    def removeWave(self, name):
        """
        Remove wave from Waves with the given name.  Return the wave if the wave is removed, False otherwise.

        Emits the waveRemoved signal if the wave is removed.
        """
        
        for index in range(len(self._waves)):
            if self._waves[index].name() == name:
                wave = self._waves.pop(index)
                wave.nameChanged.disconnect(self.emitWaveRenamed)
                self.waveRemoved[Wave].emit(wave)
                Util.debug(2, "Waves.removeWave", "Removed wave " + str(wave.name()))
                return wave
        return False

    def removeAllWaves(self):
        """
        Remove all waves from this object.

        Emits the waveRemoved signal after all waves are removed.
        """

        self._waves = []
        self.waveRemoved.emit()
        Util.debug(2, "Waves.removeAllWaves", "Removed all waves")
        return True


