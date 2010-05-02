from PyQt4.QtCore import QObject, pyqtSignal

import matplotlib.pyplot as plot
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

from Waves import Waves
from Wave import Wave
from PlotData import PlotData

class Figure(QObject):
    """
    
    Signals that are emitted from this class are:
        figureRenamed - emitted whenever the figure name is changed
    """

    # Signals
    figureRenamed  = pyqtSignal()
    rowsChanged    = pyqtSignal(int)
    columnsChanged = pyqtSignal(int)

    def __init__(self, name, nrows=1, ncols=1, padding=0.1):
        QObject.__init__(self)
        
        self.rename(name)
        self.changeNumberOfRows(nrows)
        self.changeNumberOfColumns(ncols)
        #self._name = name
        #self._rows = nrows
        #self._columns = ncols
        self._axesPadding = padding



#        self.figure = plot.figure(1)
#        self.canvas = FigureCanvas(self.figure)
#        self.plotData = []
#        self.setupPlotDataList()
    
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
        self.figureRenamed.emit()
        return True

    def changeNumberOfRows(self, nrows):
        self._rows = nrows
        self.rowsChanged.emit(self._rows)

    def changeNumberOfColumns(self, ncols):
        self._columns = ncols
        self.columnsChanged.emit(self._columns)























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
