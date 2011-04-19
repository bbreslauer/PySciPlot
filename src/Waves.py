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
    waveRemoved = pyqtSignal(Wave)
    allWavesRemoved = pyqtSignal()
    waveRenamed = pyqtSignal(Wave)

    #def __init__(self, wavesIn=[], uniqueNames=True):
    def __init__(self, wavesIn=[]):
        """
        Initialize a waves.  Add the initial set of wave(s) to the list.
        
        wavesIn is a list of Wave objects to be populated in the Waves object.
        uniqueNames determines whether the Wave objects in this Waves should have unique names.  Default is true.
        """

        QObject.__init__(self)
 
        Util.debug(1, "Waves.init", "Creating waves object")

        self._waves = dict()
        
        if isinstance(wavesIn, dict):
            wavesIn = wavesIn.values()

        for wave in wavesIn:
            self.addWave(wave)

    def __str__(self):
        string = "Waves:\n"
        for waveName in self.waveNames():
            string += str(self.wave(waveName))
        return string

    def __reduce__(self):
        return tuple([self.__class__, tuple([self.waves()])])

    def waves(self):
        """Return the waves list."""
        return self._waves

    def waveNames(self):
        """Return the names of all the waves, in no particular order."""
        return self.waves().keys()

    def length(self):
        """Return the number of waves."""
        return len(self.waves())

    def wave(self, waveName):
        """Return the wave with name waveName. Return None if wave does not exist."""
        try:
            return self.waves()[waveName]
        except KeyError:
            return None
        return None

    def findGoodWaveName(self, baseName="Wave"):
        """
        Find an unused wave name in this Waves object and return that name.  If baseName is provided, then it will be used as the beginning of the name.
        """
        
        Util.debug(3, "Waves.findGoodWaveName", "Finding acceptable wave name with base " + str(baseName))

        counter = 1
        while True:
            testName = str(baseName) + str(counter)
            if self.wave(testName) is None:
                Util.debug(3, "Waves.findGoodWaveName", "Found acceptable wave name: " + str(testName))
                return testName
            else:
                counter += 1

    def findGoodWaveNames(self, numWaves=1, baseName="Wave"):
        """
        Find numWaves unused wave names in this Waves object and return that name.  If baseName is provided, then it will be used as the beginning of the name.
        """
        
        goodWaveNames = []
        counter = 1
        while numWaves > 0:
            testName = str(baseName) + str(counter)
            if self.wave(testName) is None:
                goodWaveNames.append(testName)
                numWaves -= 1
            counter += 1
        return goodWaveNames

    def goodWaveName(self, name):
        """
        Determine if name is a good Wave name for this Waves object.  Returns False if name is an empty string.  Returns True if name is not an empty string and is unique.
        """
        
        name = Wave.validateWaveName(name)
        if name == "":
            return False
        return self.uniqueWaveName(name)

    def uniqueWaveName(self, name):
        """Return True if name is neither an empty string nor an existing Wave name in this object.  Return False otherwise."""

        if name == "":
            return False
        if self.wave(name) is None:
            return True
        return False

    def uniqueWave(self, wave):
        """Return True if wave's name is neither an empty string nor an existing Wave name in this object.  Return False otherwise."""
        return self.uniqueWaveName(wave.name())

    # Modifying methods
    def addWave(self, wave):
        """
        Add wave to dict of waves.  Return wave if wave is added, False otherwise.

        Emits the waveAdded signal if the wave is added.
        """
        Util.debug(2, "Waves.addWave", "Adding wave")

        if self.uniqueWaveName(wave.name()):
            Util.debug(2, "Waves.addWave", "Adding wave " + str(wave.name()) + ".")
            self.waves()[wave.name()] = wave
            #wave.nameChanged.connect(self.emitWaveRenamed)
            wave.nameChanged.connect(self.moveWave)
            self.waveAdded.emit(wave)
            return wave
        return False

    def moveWave(self, oldName, wave):
        """
        Move the wave from its old dictionary key to its current name.

        If the current name is already taken, then we need to fail and change the wave's name back to its original value.
        To do this, we disconnect the Waves signals, revert the wave's name, and then reconnect the Waves signals.
        """

        if self.wave(wave.name()) is None:
            if self.removeWave(oldName, True):
                self.waves()[wave.name()] = wave
                self.waveRenamed.emit(wave)
                return True
        wave.nameChanged.disconnect(self.moveWave)
        wave.setName(oldName)
        wave.nameChanged.connect(self.moveWave)
        return False

    def removeWave(self, name, movingWave=False):
        """
        Remove wave from Waves with the given name.  Return the wave if the wave is removed, False otherwise.  If the wave is being moved (i.e. being called from moveWave) then waveRemoved will not be emitted.

        Emits the waveRemoved signal if the wave is removed.
        """
        name = str(name)
        if self.wave(name):
            wave = self.wave(name)
            del self.waves()[name]
            if not movingWave:
                wave.nameChanged.disconnect(self.moveWave)
                self.waveRemoved[Wave].emit(wave)
            return wave
        return False

    def removeAllWaves(self):
        """
        Remove all waves from this object.

        Emits the waveRemoved signal after all waves are removed.
        """

        self._waves = dict()
        self.allWavesRemoved.emit()
        Util.debug(2, "Waves.removeAllWaves", "Removed all waves")
        return True


