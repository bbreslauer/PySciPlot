from PyQt4.QtCore import QObject, pyqtSignal

import matplotlib.pyplot as plot
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

from Waves import Waves
from Wave import Wave
from Plot import Plot
from PlotData import PlotData
from DialogSubWindow import DialogSubWindow

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
        self.rename(name)
        self.setNumberOfRows(nrows)
        self.setNumberOfColumns(ncols)
        self.setAxesPadding(padding)

        # this is a 2d array of plots.  first index is for row, second index is for column
        # the first row and first column is always zeroes, so that the row and column indices
        # are the same as used for matplotlib

        self._figure = plot.figure(1)
        self._canvas = FigureCanvas(self._figure)
        self._figureSubWindow = DialogSubWindow(self._app.ui.workspace)
        self._figureSubWindow.setWidget(self._canvas)
        self._app.ui.workspace.addSubWindow(self._figureSubWindow)
        self.showFigure()

        self._plots = [[]]
        self.addMorePlots()

        self.refresh()

        # Connect signals
        self.rowsChanged.connect(self.refresh)
        self.columnsChanged.connect(self.refresh)

        self.rowsChanged.connect(self.addMorePlots)
        self.columnsChanged.connect(self.addMorePlots)
    
    def __str__(self):
        return "name: %s, rows: %s, columns: %s" % (self._name, self._rows, self._columns)

    def name(self):
        return self._name

    def rows(self):
        return self._rows

    def columns(self):
        return self._columns

    def rename(self, newName):
        self._name = newName
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

    def getPlot(self, row, col):
        #print "row: " + str(row)
        #print "col: " + str(col)
        return self._plots[row][col]

    def addMorePlots(self):
        """Add more blank plots to the _plots 2d array, so that we can manipulate them later."""

        # Make the rows for Plot objects
        additionalRows = self._rows - len(self._plots) + 1
        self._plots.extend([[]] * additionalRows)

        for i in range(1, len(self._plots)):
            if len(self._plots[i]) == 0:
                self._plots[i].append(0)

            lastColumn = len(self._plots[i])

            for j in range(len(self._plots[i]), self._columns + 1):
                def buildPlotHelper():
                    self.refresh()

                newPlot = Plot()
                self._plots[i].append(newPlot)
                newPlot.traceAdded.connect(self.refresh)
                buildPlotHelper()
        
        return True

    def showFigure(self):
        self._figureSubWindow.show()

    def refresh(self, *args):
        """
        Refresh everything related to the figure display, including plots and text.
        """

        self.addMorePlots()

        # Clear the figure
        plot.clf()
        
        for row in range(1, self._rows + 1):
            for col in range(1, self._columns + 1):
                print "row: " + str(row) + ", col: " + str(col)
                self.makePlot(row, col)
        
        print ""
        self._canvas.draw()
        
        return

    def makePlot(self, row, column):
        plotNum = column + ((row - 1) * self._columns)
        #print "rows: " + str(self._rows) + ", cols: " + str(self._columns)
        #print "row: " + str(row) + ", col: " + str(column) + ", plotNum: " + str(plotNum)
        if row == 0 or column == 0:
            return


        plot.subplot(self._rows, self._columns, plotNum)
        self.getPlot(row, column).buildPlot(plot)












#    def setupPlotDataList(self):
#        if len(self.plotData) == self.numCols * self.numRows:
#            return
#        elif len(self.plotData) < self.numCols * self.numRows:
#            for i in range((self.numCols * self.numRows) - len(self.plotData)):
#                self.plotData.append(PlotData())
#            return
#        elif len(self.plotData) > self.numCols * self.numRows:
#            for i in range(len(self.plotData) - (self.numCols * self.numRows)):
#                self.plotData.pop()
#            return
#        return
#    
#    def addPlotData(self, plotNum, x, y):
#        return self.plotData[self.plotIndex(plotNum)].addData(x, y)
#        
#    def plotIndex(self, plotNum):
#        return plotNum - 1
#    
#    def plotNum(self, plotIndex):
#        return plotIndex + 1
#    
#    def makePlots(self):
#        plot.clf()
#        for plotIndex in range(self.numCols * self.numRows):
#            plot.subplot(self.numRows, self.numCols, self.plotNum(plotIndex))
#            self.plotData[plotIndex].buildPlot(plot)
#        
#        self.drawPlots()
#        return True
#        
#    def drawPlots(self):
#        print "drawing plots"
#        self.canvas.draw()
#        return
#        
#    def getCanvas(self):
#        return self.canvas
