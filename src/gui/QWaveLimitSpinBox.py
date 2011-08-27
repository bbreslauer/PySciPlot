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


from PySide.QtGui import QSpinBox, QApplication

class QWaveLimitSpinBox(QSpinBox):
    """
    Extend the QSpinBox so that its upper limit is automatically
    set to the length of a wave (or the min length of a set of waves).
    
    Also, depending on whether this is a start or end limit, determine
    what the default value should be.
    """

    def __init__(self, parent=None):
        QSpinBox.__init__(self, parent)

        self._app = QApplication.instance().window

        self.setRange(0, 0)
        self.setValue(0)
        
        self._waveViews = {}

    def addWaveView(self, view):
        wave = self._app.waves().wave(str(view.currentText()))
        
        if wave:
            self._waveViews[view] = wave
            wave.lengthChanged.connect(self.updateLimits)

        def changeWaveForView(newWaveName):
            self.changeWave(view, newWaveName)

        view.currentIndexChanged[str].connect(changeWaveForView)

        self.updateLimits()

    def changeWave(self, view, waveName):
        if view in self._waveViews.keys():
            try:
                self._waveViews[view].lengthChanged.disconnect(self.updateLimits)
            except:
                pass
        newWave = self._app.waves().wave(str(waveName))
        if newWave:
            self._waveViews[view] = newWave
            newWave.lengthChanged.connect(self.updateLimits)
        self.updateLimits()

    def updateLimits(self, *args):
        """
        Update the limits for the spin box, based on the lengths of
        the waves.
        """
        # This gives the length of the smallest wave
        if len(self._waveViews.keys()) == 0:
            return 0
        
        oldMaximum = self.maximum()
        maximum = min(map(lambda wave: wave.length(), self._waveViews.values())) - 1
        self.setMaximum(maximum)

        self.setCurrentValue(oldMaximum, maximum)
    
    def setCurrentValue(self, oldMaximum, newMaximum):
        """By default, leave the current value at whatever it currently is."""
        pass


class QWaveStartSpinBox(QWaveLimitSpinBox):
    """
    Create a start spin box (defaults to 0).
    """

    def __init__(self, parent=None):
        QWaveLimitSpinBox.__init__(self, parent)

class QWaveEndSpinBox(QWaveLimitSpinBox):
    """
    Create a end spin box (defaults to the min wave length).
    """

    def __init__(self, parent=None):
        QWaveLimitSpinBox.__init__(self, parent)

    def setCurrentValue(self, oldMaximum, newMaximum):
        """
        If the current value is equal to the old maximum, then
        we change it to the new maximum, because we assume that the user
        wanted to go to the end of the list.

        This will only happen if we are increasing the maximum. If the 
        maximum is being decreased and the value was equal to it, then
        qt will have already decreased the value.
        """
        
        if self.value() == oldMaximum:
            self.setValue(newMaximum)



