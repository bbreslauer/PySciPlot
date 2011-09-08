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


from PySide.QtCore import Qt
from PySide.QtGui import QAction, QColor, QApplication

from pygraphene import figure as pgf
from pygraphene import plot as pgp
from pygraphene import font as pgfont

import Util, Property
from FigureObject import *
from Waves import Waves
from Wave import Wave
from Plot import Plot
from gui.SubWindows import FigureSubWindow

class Figure(FigureObject):
    """
    Encapsulates all data for a figure, including all the plots within it.

    plotNum is 0-based.
    """

    def __init__(self, windowTitle=""):
        
        Util.debug(2, "Figure.init", "Creating figure")

        # Properties
        properties = {  
                            'windowTitle':        Property.String(''),
                            'title':              Property.String(''),
                            'titleFont':          Property.TextOptions({'size': 20, 'rotation': 'horizontal', 'verticalalignment': 'top'}),
                            'rows':               Property.Integer(1),
                            'columns':            Property.Integer(1),
                            'axesPadding':        Property.Float(0.5),
                            'backgroundColor':    Property.Color(QColor(255,255,255,255)),
                            'linkPlotAxes':       Property.Boolean(False),
                          }

        self._app = QApplication.instance().window

        # Graphical stuff
        width=600
        height=400
        self._figure = pgf.Figure(width, height)
        self._canvas = self._figure.canvas().widget()
        self._figureSubWindow = FigureSubWindow(self._app.ui.workspace)
        self._figureSubWindow.setWidget(self._canvas)
        self._figureSubWindow.resize(width+10, height+31) # resize includes the window frame, for some reason, so we need to add some pixels
        self._app.ui.workspace.addSubWindow(self._figureSubWindow)
        self._canvas.setParent(self._figureSubWindow)
        self.showFigure()
        
        FigureObject.__init__(self, properties)

        self.set('windowTitle', windowTitle)

        self._plots = []
        self.extendPlots(0)
        
        self.refresh()

        Util.debug(1, "Figure.init", "Created figure " + self.get('windowTitle'))

    def __del__(self):
        self._figureSubWindow.setAttribute(Qt.WA_DeleteOnClose)
        self._figureSubWindow.close()

    def __str__(self):
        return "name: %s, rows: %s, columns: %s" % (self.get('windowTitle'), self.get('rows'), self.get('columns'))

    def __reduce__(self):
        return tuple([self.__class__, tuple(), tuple([self.properties, self.plots()])])

    def __setstate__(self, state):
        properties = state[0]
        plots = state[1]

        self.setMultiple(properties)
        self._plots = []
        
        for plot in plots:
            self.plots().append(plot)

        self.refreshPlots()

    def pgFigure(self):
        return self._figure
    
    def plots(self):
        return self._plots

    def numPlots(self):
        return self.get('rows') * self.get('columns')

    def getPlot(self, plotNum):
        if plotNum < self.numPlots():
            return self.plots()[plotNum]
        return None

    def addPlot(self, plot, refresh=True):
        self.plots().append(plot)  # Keep reference to the PSP plot around
        plot.addFigure(self)  # Need the plot to keep the PSP figure reference
        plot.initPgPlot()  # Create the PG plot in the PSP plot
        self.pgFigure().addPlot(plot.pgPlot())  # Add the PG plot to the PG figure
        plot.pgPlot().setPlotLocation(self.getPg('rows'), self.getPg('columns'), self.numPlots())

        if refresh:
            self.refreshPlots()  # Update the screen

    def extendPlots(self, maxPlotNum=-1):
        """
        If maxPlotNum < 0, then it will be equal to numPlots() - 1.
        """
        if maxPlotNum < 0:
            maxPlotNum = self.numPlots() - 1

        Util.debug(2, "Figure.extendPlots", "Extending figure to contain " + str(maxPlotNum + 1) + " plots")
        for i in range(len(self.plots()), maxPlotNum + 1):
            plot = Plot()
            self.addPlot(plot, False)

    #################################
    # Handlers for when a property is modified
    #################################

    def update_windowTitle(self):
        Util.debug(3, "Figure.update_windowTitle", "")
        self._figureSubWindow.setWindowTitle(self.getPg('windowTitle'))

    def update_title(self):
        Util.debug(3, "Figure.update_title", "")
        self.pgFigure().setTitle(self.getPg('title'), pgfont.Font(**self.getPg('titleFont')))
        self.pgFigure().title().draw()

    def update_titleFont(self):
        Util.debug(3, "Figure.update_titleFont", "")
        self.pgFigure().setTitle(font=pgfont.Font(**self.getPg('titleFont')))
        self.pgFigure().title().draw()

    def update_rows(self):
        Util.debug(3, "Figure.update_rows", "")
        # TODO
        #self.refreshPlots()

    def update_columns(self):
        Util.debug(3, "Figure.update_columns", "")
        # TODO
        #self.refreshPlots()

    def update_linkPlotAxes(self):
        Util.debug(3, "Figure.update_linkPlotAxes", "")
        # TODO
        #self.refreshPlots()
    
    def update_axesPadding(self):
        Util.debug(3, "Figure.update_axesPadding", "")
        # TODO
#        if self.getMpl('linkPlotAxes'):
#            self.grid.set_axes_pad(self.getMpl('axesPadding'))
#        else:
#            self.mplFigure().subplots_adjust(wspace=self.getMpl('axesPadding'), hspace=self.getMpl('axesPadding'))
        #self.redraw()

    def update_backgroundColor(self):
        Util.debug(3, "Figure.update_backgroundColor", "")
        # TODO
#        self.mplFigure().set_facecolor(self.getMpl('backgroundColor'))
        #self.redraw()
        
    def refreshPlots(self):
        Util.debug(3, "Figure.refreshPlots", "")
        
        # Create any new plots that might be necessary
        self.extendPlots()

        # Refresh the plots
        for plot in self.plots():
            plot.refresh()

    def redraw(self):
        Util.debug(3, "Figure.redraw", "Drawing canvas")
        print 'figure redraw'
        self.pgFigure().draw()


    def refresh(self):
        self.refreshPlots()
        self.update_backgroundColor()
        self.update_title()
        self.update_windowTitle()


    def showFigure(self):
        self._figureSubWindow.show()

    def hideFigure(self):
        self._figureSubWindow.hide()

#    def createRightClickActions(self):
#
#        def createEditPlotDialog():
#            self._app._windows["EditPlotDialog"].show()
#            pass
#
#        editPlotAction = QAction("Edit Plot", self._figureSubWindow)
#        editPlotAction.triggered.connect(createEditPlotDialog)
#        self._figureSubWindow.setContextMenuPolicy(Qt.ActionsContextMenu)
#        self._figureSubWindow.insertAction(QAction(self._figureSubWindow), editPlotAction)



