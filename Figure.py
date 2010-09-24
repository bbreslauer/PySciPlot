from PyQt4.QtCore import QObject, pyqtSignal, Qt
from PyQt4.QtGui import QAction

import matplotlib.pyplot as plot
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure as MPLFigure
from mpl_toolkits.axes_grid.axislines import Axes

import Util
from Waves import Waves
from Wave import Wave
from Plot import Plot
from Gui import FigureSubWindow

class Figure(QObject):
    """
    Encapsulates all data for a figure, including all the plots within it.

    Signals that are emitted from this class are:
        figureRenamed - emitted whenever the figure name is changed
    """

    # Signals
    figureRenamed  = pyqtSignal(str)
    plotRenamed    = pyqtSignal(int, str)
    propertyChanged = pyqtSignal()

    # Properties
    properties = {  
                'figureName':               { 'type': str,   'default': '' },
                'figureTitle':              { 'type': str,   'default': '' },
                'figureRows':               { 'type': int,   'default': 1 },
                'figureColumns':            { 'type': int,   'default': 1 },
                'figureAxesPadding':        { 'type': float, 'default': 0.1 },
                'figureBackgroundColor':    { 'type': str,   'default': '#ffffff' },
                 }

    def __init__(self, app, name, nrows=1, ncols=1, padding=0.1):
        QObject.__init__(self)
        
        Util.debug(2, "Figure.init", "Creating figure")

        self.initializeProperties()

        self._app = app

        self.set_('figureRows', nrows)
        self.set_('figureColumns', ncols)
        self.set_('figureAxesPadding', padding)
        self.set_('figureBackgroundColor', '#ffffff')

        # Graphical stuff
        self._figure = MPLFigure()
        self._canvas = FigureCanvas(self._figure)
        self._figureSubWindow = FigureSubWindow(self._app.ui.workspace)
        self._figureSubWindow.setWidget(self._canvas)
        self._app.ui.workspace.addSubWindow(self._figureSubWindow)
        self._canvas.setParent(self._figureSubWindow)
        self.showFigure()
        
        self.set_('figureName', name)

        self._plots = []
        self.extendPlots(1)

        self.refresh()

        # Connect signals
        self.propertyChanged.connect(self.refresh)
        
        Util.debug(1, "Figure.init", "Created figure " + self.get('figureName'))

    def __str__(self):
        return "name: %s, rows: %s, columns: %s" % (self.get('figureName'), self.get('figureRows'), self.get('figureColumns'))

    def initializeProperties(self):
        Util.debug(2, "Figure.initializeProperties", "Initializing properties for new figure")
        for prop in self.properties.keys():
            vars(self)["_" + prop] = self.properties[prop]['default']

    def get(self, variable):
        try:
            return vars(self)["_" + variable]
        except AttributeError:
            return self.properties[variable]['default']

    def set_(self, variable, value):

        if value != "" and value != vars(self)["_" + variable]:
            if variable in self.properties.keys():
                if self.properties[variable]['type'] == bool:
                    # Need to do specialized bool testing because bool('False') == True
                    if value == "True":
                        vars(self)["_" + variable] = True
                    else:
                        vars(self)["_" + variable] = False
                else:
                    vars(self)["_" + variable] = self.properties[variable]['type'](value)
            else:
                vars(self)["_" + variable] = value

            Util.debug(2, "Figure.set", "Setting " + str(variable) + " to " + str(value) + " for figure " + str(self.get('figureName')))

            # See if we should emit any signals
            if variable == 'figureName':
                self._figureSubWindow.setWindowTitle(value)
                self.figureRenamed.emit(value)
            else:
                self.propertyChanged.emit()

            return True
        return False

    def mplFigure(self):
        return self._figure

    def numPlots(self):
        return self.get('figureRows') * self.get('figureColumns')

    def getPlot(self, plotNum):
        if plotNum <= self.numPlots():
            return self._plots[plotNum - 1]
        return None
    
    def plots(self):
        return self._plots

    def extendPlots(self, plotNum):
        Util.debug(2, "Figure.extendPlots", "Extending plots on figure to contain " + str(plotNum + 1) + " plots")
        for i in range(len(self._plots), plotNum):
            plot = Plot(self, i + 1)
            self.appendPlot(plot)

    def appendPlot(self, plot):
        """Append a single plot onto the figure."""

        # This must be done in a separate function, as opposed to included in extendPlots
        # because the emitPlotRenamed method would be redefined in the for loop in 
        # extendPlots and only the last version would be connected, even if you connect
        # it within the for loop.  Strange, but true.  So the way to work around that
        # is to have a separate method be called.
        self._plots.append(plot)

        Util.debug(2, "Figure.appendPlot", "Added plot " + str(plot.get('plotNum')))
        
        def emitPlotRenamed(name):
            self.plotRenamed.emit(plot.get('plotNum'), name)
        
        plot.plotRenamed.connect(emitPlotRenamed)

    def replacePlot(self, plotNum, plot):
        """Replace the current plot in plotNum with a new plot."""
        if plotNum <= self.numPlots():
            # Disconnect current signals
            self.getPlot(plotNum).plotRenamed.disconnect()

            # Replace with new plot
            self._plots[plotNum - 1] = plot

            Util.debug(2, "Figure.replacePlot", "Replaced plot " + str(plotNum))
        
            def emitPlotRenamed(name):
                self.plotRenamed.emit(plot.get('plotNum'), name)
            
            plot.plotRenamed.connect(emitPlotRenamed)

        return False


    def refreshPlot(self, plotNum, drawBool=True):
        Util.debug(1, "Figure.refreshPlot", "Refreshing plot " + str(plotNum))
        self.getPlot(plotNum).refresh(drawBool)
        Util.debug(1, "Figure.refreshPlot", "Refreshed plot " + str(plotNum))

    def refresh(self, *args):
        """
        Refresh everything related to the figure display, including plots and text.
        """
        
        Util.debug(1, "Figure.refresh", "Refreshing all plots")

        displayedPlots = self.numPlots()

        self.extendPlots(displayedPlots)

        Util.debug(3, "Figure.refresh", "Clearing figure")
        self.mplFigure().clf()

        self.mplFigure().suptitle(str(self.get('figureTitle')))
        
        self.mplFigure().set_facecolor(str(self.get('figureBackgroundColor')))

        for plotNum in range(1, displayedPlots + 1):
            self.refreshPlot(plotNum, False)

        Util.debug(3, "Figure.refresh", "Drawing canvas")
        self._canvas.draw()
        
        Util.debug(1, "Figure.refresh", "Finished refreshing all plots")

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



