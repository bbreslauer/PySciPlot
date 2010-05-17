from PyQt4.QtCore import QObject, pyqtSignal

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

        self._figures = []
        
        for figure in figuresIn:
            self.addFigure(figure)

    def __str__(self):
        string = "Figures:\n"
        for figure in self._figures:
            string += str(figure) + "\n"
        return string

    def figures(self):
        return self._figures

    def addFigure(self, figure):
        """Add a figure to the object."""
        self._figures.append(figure)
        self.figureAdded.emit()
        return figure
    
    def getFigure(self, index):
        """Get the figure at list index 'index'."""
        return self._figures[index]

    def removeFigure(self, position):
        """Remove a figure from the object, based on the position in the _figures list."""
        removedFigure = ""
        try:
            removedFigure = self._figures.pop(position)
        except IndexError:
            return False
        self.figureRemoved.emit()
        return removedFigure

    def length(self):
        return len(self._figures)



