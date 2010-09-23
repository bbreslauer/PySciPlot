from PyQt4.QtCore import QObject, pyqtSignal

import Util

from Figure import Figure

class Figures(QObject):
    """
    A list of Figure objects with some helper methods.

    A Figures object contains a list of Figure(s).

    Signals that are emitted from this class are:
        figureAdded   - emitted when a Figure is added
        figureRemoved - emitted when a Figure is removed
    """

    # Signals
    figureAdded   = pyqtSignal()
    figureRemoved = pyqtSignal()

    def __init__(self, figuresIn=[]):
        """
        Initialize a Figures object.  Add the initial set of Figure(s) to the list.
        
        figuresIn is a list of Figure objects to be populated in the Figures object.
        """

        QObject.__init__(self)
        
        Util.debug(2, "Figures.init", "Creating figures object")

        self._figures = []
        
        for figure in figuresIn:
            self.addFigure(figure)
        
        Util.debug(2, "Figures.init", "Created figures object")

    def __str__(self):
        string = "Figures:\n"
        for figure in self._figures:
            string += str(figure) + "\n"
            for plot in figure.plots():
                string += "  Plot: " + str(plot) + "\n"
            string += "\n"
        return string

    def figures(self):
        return self._figures

    def addFigure(self, figure):
        """Add a figure to the object."""
        self._figures.append(figure)
        self.figureAdded.emit()
        Util.debug(2, "Figures.addFigure", "Added figure " + figure.get('figureName') + " to figures object")
        return figure
    
    def getFigure(self, index):
        """Get the figure at list index 'index'."""
        if index >= 0 and index < len(self._figures):
            return self._figures[index]
        return False

    def removeFigure(self, figure):
        """Remove a figure from the object."""
        removedFigure = None
        try:
            removedFigure = self._figures.remove(figure)
        except IndexError:
            return False
        self.figureRemoved.emit()
        Util.debug(2, "Figures.removeFigure", "Removed figure " + figure.get('figureName') + " from figures object")
        return removedFigure

    def removeAllFigures(self):
        """
        Remove all figures from this object.
        """

        self._figures = []
        self.figureRemoved.emit()
        Util.debug(2, "Figures.removeAllFigures", "Removed all figures from figures object")
        return True

    def length(self):
        return len(self._figures)




