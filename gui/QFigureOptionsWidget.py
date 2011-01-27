from PyQt4.QtGui import QWidget, QApplication, QDialogButtonBox

import Util
from QEditFigureSubWidget import *

class QFigureOptionsWidget(QEditFigureSubWidget):

    properties = (  
                 'windowTitle',
                 'title',
                 'titleFont',
                 'rows',
                 'columns',
                 'axesPadding',
                 'backgroundColor',
                 'linkPlotAxes',
                )

    def saveUi(self):
        """Save the UI data to the current Figure object."""
        
        self._editFigureDialogModule.currentFigure().setMultiple(self.getCurrentUi())

    def resetUi(self):
        """Set the UI to the current Figure's settings."""
        
        self.setCurrentUi(self._editFigureDialogModule.currentFigure().properties)

