import matplotlib.pyplot as plot
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

from Waves import Waves
from Wave import Wave
from PlotData import PlotData


class Figure():
    def __init__(self, nrows=1, ncols=1, padding=0.1):
        self.figure = plot.figure(1)
        self.canvas = FigureCanvas(self.figure)
        self.numRows = nrows
        self.numCols = ncols
        self.axesPadding = padding
        self.plotData = []
        self.setupPlotDataList()
    
    def setupPlotDataList(self):
        if len(self.plotData) == self.numCols * self.numRows:
            return
        elif len(self.plotData) < self.numCols * self.numRows:
            for i in range((self.numCols * self.numRows) - len(self.plotData)):
                self.plotData.append(PlotData())
            return
        elif len(self.plotData) > self.numCols * self.numRows:
            for i in range(len(self.plotData) - (self.numCols * self.numRows)):
                self.plotData.pop()
            return
        return
    
    def addPlotData(self, plotNum, x, y):
        return self.plotData[self.plotIndex(plotNum)].addData(x, y)
        
    def plotIndex(self, plotNum):
        return plotNum - 1
    
    def plotNum(self, plotIndex):
        return plotIndex + 1
    
    def makePlots(self):
        plot.clf()
        for plotIndex in range(self.numCols * self.numRows):
            plot.subplot(self.numRows, self.numCols, self.plotNum(plotIndex))
            self.plotData[plotIndex].buildPlot(plot)
        
        self.drawPlots()
        return True
        
        
    def drawPlots(self):
        print "drawing plots"
        self.canvas.draw()
        return
        
    def getCanvas(self):
        return self.canvas
