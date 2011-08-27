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


from PySide.QtCore import QObject, Signal

import Util

from Figure import Figure

class Figures(QObject):
    """
    A list of Figure objects with some helper methods.

    A Figures object contains a list of Figure(s).

    Signals that are emitted from this class are:
        figureAdded   - emitted when a Figure is added
        figureRemoved - emitted when a Figure is removed
        figureRenamed - emitted when a Figure's window is renamed
    """

    # Signals
    figureAdded   = Signal()
    figureRemoved = Signal()
    figureRenamed = Signal()

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

    def __reduce__(self):
        return tuple([self.__class__, tuple([self.figures()])])

    def figures(self):
        return self._figures

    def addFigure(self, figure):
        """Add a figure to the object."""
        self._figures.append(figure)
        figure.properties['windowTitle'].modified.connect(self.emitFigureRenamed)
        self.figureAdded.emit()
        Util.debug(2, "Figures.addFigure", "Added figure " + figure.get('windowTitle') + " to figures object")
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
            figure.properties['windowTitle'].modified.disconnect(self.emitFigureRenamed)
            self.figureRemoved.emit()
            Util.debug(2, "Figures.removeFigure", "Removed figure " + figure.get('windowTitle') + " from figures object")
            del figure
        except IndexError:
            return False
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

    def emitFigureRenamed(self):
        self.figureRenamed.emit()



