from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QAction

class AddWaveAction(QAction):
    def __init__(self, text, parent):
        QAction.__init__(self, text, parent)
        self.connect(self, SIGNAL("triggered()"), self.addingWave)
    
    def addingWave(self):
        self.emit(SIGNAL("addWaveClicked"), self.text())