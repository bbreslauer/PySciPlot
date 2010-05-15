from PyQt4.QtCore import QObject, pyqtSignal, Qt
from PyQt4.QtGui import QAction

import matplotlib.pyplot as plot
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure as MPLFigure

from Waves import Waves
from Wave import Wave
from Plot import Plot
from PlotData import PlotData
from DialogSubWindow import DialogSubWindow
from modules.EditPlotDialog import EditPlotDialog

class Figure(QObject):
    """
    Encapsulates all data for a figure, including all the plots within it.

    Signals that are emitted from this class are:
        figureRenamed - emitted whenever the figure name is changed
    """

    # Signals
    figureRenamed  = pyqtSignal(str)
    rowsChanged    = pyqtSignal(int)
    columnsChanged = pyqtSignal(int)
    axesPaddingChanged = pyqtSignal(float)

    def __init__(self, app, name, nrows=1, ncols=1, padding=0.1):
        QObject.__init__(self)
        
        self._app = app
        self.setNumberOfRows(nrows)
        self.setNumberOfColumns(ncols)
        self.setAxesPadding(padding)

        self._figure = MPLFigure()
        self._canvas = FigureCanvas(self._figure)
        self._figureSubWindow = DialogSubWindow(self._app.ui.workspace)
        self._figureSubWindow.setWidget(self._canvas)
        self._app.ui.workspace.addSubWindow(self._figureSubWindow)
        self._canvas.setParent(self._figureSubWindow)
        self.showFigure()

        self.rename(name)

        self._plots = []
        self.extendPlots(1)

        self.createRightClickActions()

        self.refresh()

        # Connect signals
        self.rowsChanged.connect(self.refresh)
        self.columnsChanged.connect(self.refresh)

    def __str__(self):
        return "name: %s, rows: %s, columns: %s" % (self._name, self._rows, self._columns)

    def name(self):
        return self._name

    def rows(self):
        return self._rows

    def columns(self):
        return self._columns

    def mplFigure(self):
        return self._figure

    def rename(self, newName):
        self._name = newName
        self._figureSubWindow.setWindowTitle(newName)
        self.figureRenamed.emit(self._name)
        return True

    def setNumberOfRows(self, nrows):
        self._rows = nrows
        self.rowsChanged.emit(self._rows)

    def setNumberOfColumns(self, ncols):
        self._columns = ncols
        self.columnsChanged.emit(self._columns)

    def setAxesPadding(self, padding):
        self._axesPadding = padding
        self.axesPaddingChanged.emit(self._axesPadding)

    def numPlots(self):
        return self._rows * self._columns

    def getPlot(self, plotNum):
        return self._plots[plotNum - 1]
    
    def extendPlots(self, plotNum):
        for i in range(len(self._plots), plotNum):
            self._plots.append(Plot(self, i + 1))

    def refreshPlot(self, plotNum):
        print "refreshing #: " + str(plotNum)
        plot = self.getPlot(plotNum)
        plot.refresh()

    def refresh(self, *args):
        """
        Refresh everything related to the figure display, including plots and text.
        """
        
        displayedPlots = self.rows() * self.columns()

        self.extendPlots(displayedPlots)

        self.mplFigure().clf()

        for plotNum in range(displayedPlots):
            self.refreshPlot(plotNum + 1)

    def showFigure(self):
        self._figureSubWindow.show()

    def createRightClickActions(self):

        def createEditPlotDialog():
            self._app._windows["EditPlotDialog"].show()

        editPlotAction = QAction("Edit Plot", self._figureSubWindow)
        editPlotAction.triggered.connect(createEditPlotDialog)
        self._figureSubWindow.setContextMenuPolicy(Qt.ActionsContextMenu)
        self._figureSubWindow.insertAction(QAction(self._figureSubWindow), editPlotAction)



