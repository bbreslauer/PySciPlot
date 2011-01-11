from PyQt4.QtGui import QWidget, QApplication, QDialogButtonBox

import Util
from QEditFigureSubWidget import *

class QFigureOptionsWidget(QEditFigureSubWidget):

    def saveUi(self):
        """Save the UI data to the current Figure object."""
        
        currentFigure = self._editFigureDialogModule.currentFigure()
        for option in currentFigure.properties.keys(): 
            currentFigure.set(option, Util.getWidgetValue(self.getChild(option)))

    def resetUi(self):
        """Set the UI to the current Figure's settings."""
        
        currentFigure = self._editFigureDialogModule.currentFigure()
        for option in currentFigure.properties.keys():
            Util.setWidgetValue(self.getChild(option), currentFigure.get(option))

