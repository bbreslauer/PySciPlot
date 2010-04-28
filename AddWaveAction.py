from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QAction

from Wave import Wave

class AddWaveAction(QAction):
    """
    This class is an action for adding a wave to a table.  It encapsulates the wave in an action.i
    
    Signals that are emitted from this class are:
        addWaveClicked - emitted when the menu item attached to this class is clicked
    """

    # Signals
    addWaveClicked = pyqtSignal(Wave)

    def __init__(self, wave, parent):
        QAction.__init__(self, wave.name(), parent)
        self._wave = wave
        self.triggered.connect(self.addingWave)
    
    def addingWave(self):
        """Convert from a triggered signal to a addWaveClicked signal."""
        self.addWaveClicked.emit(self._wave)

